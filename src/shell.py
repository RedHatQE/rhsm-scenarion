from src.types import (CmdResult)
import unicodedata
import os.path, subprocess
from time import time

def run_cmd(cmd,args,workdir):
    exitcode = 0
    normalized_name = unicodedata.normalize('NFKD',"+".join([cmd]+args))+str(time())
    stdout_fname = os.path.join(workdir,normalized_name+".stdout")
    stderr_fname = os.path.join(workdir,normalized_name+".stderr")
    with open(stdout_fname,"wt") as stdout:
        with open(stderr_fname,"wt") as stderr:
            exitcode = subprocess.call([cmd]+args,stdout=stdout,stderr=stderr)
    with open(stdout_fname,'rt') as stdout:
        with open(stderr_fname,'rt') as stderr:
            return CmdResult(cmd=cmd,
                             args=args,
                             exitcode=exitcode,
                             stdout=stdout.read(),
                             stderr=stderr.read())
