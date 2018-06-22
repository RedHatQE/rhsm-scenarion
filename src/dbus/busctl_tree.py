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
result = run_cmd("busctl",["tree","--no-pager"],workdir)
send_message(result)
send_message(EndOfScenario(scenario,timestamp))
