from src.testware.message import send_message
import paramiko

remote_cert_path="/candlepin/server/generated_certs/37060.pem"

import os.path
import tempfile
from time import time
from src.shell import run_cmd
from src.testware.message import send_message
from src.types import (StartOfScenario, EndOfScenario)

timestamp=int(time())
scenario=os.path.basename(__file__)
workdir=tempfile.mkdtemp(prefix="{0}-{1}.".format(scenario,timestamp))
print("working directory: {0}".format(workdir))

send_message(StartOfScenario(scenario,timestamp))
client = paramiko.SSHClient()
ssh_client =paramiko.SSHClient()
client.connect(hostname="candlepin.example.com",
               username="root")
sftp = client.open_sftp()
sftp.get(remote_cert_path,"/tmp/")

send_message(EndOfScenario(scenario,timestamp))
