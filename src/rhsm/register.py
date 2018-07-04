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
send_message(run_cmd("subscription-manager",
                     ["register",
                      "--username",os.environ.get("SUBSCRIPTION_USER_NAME"),
                      "--password",os.environ.get("SUBSCRIPTION_PASSWORD"),
                      "--org",os.environ.get("SUBSCRIPTION_ORG_ID")],workdir))
send_message(EndOfScenario(scenario,timestamp))
