from src.testware.message import send_message
import paramiko
import os.path
import tempfile
from time import time
from src.shell import run_cmd
from src.testware.message import send_message
from src.types import (StartOfScenario,
                       NewProductInstalled,
                       EndOfScenario)

product_id="37060"
cert_name = "37060.pem"
remote_cert_path="/vagrant/generated_certs/"

timestamp=int(time())
scenario=os.path.basename(__file__)
workdir=tempfile.mkdtemp(prefix="{0}-{1}.".format(scenario,timestamp))
print("working directory: {0}".format(workdir))

send_message(StartOfScenario(scenario,timestamp))
client = paramiko.SSHClient()
client.load_system_host_keys()

client.connect(hostname="candlepin.example.com",
               username="root")
sftp = client.open_sftp()
sftp.get(os.path.join(remote_cert_path,cert_name),
         os.path.join("/etc/pki/product",cert_name))
send_message(NewProductInstalled(product_id=product_id))
send_message(EndOfScenario(scenario,timestamp))
