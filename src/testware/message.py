import requests
import time
from src.types import type_name
from src.types import (TestwareMSG)
import os
from datetime import datetime

def send_message(msg):
    url = os.environ.get('RHSM_SERVICES_URL')+"/testing/message"
    time = str(datetime.now())
    data = TestwareMSG(time = time,
                       type = type_name(msg),
                       msg = msg._asdict())
    r = requests.post(url,json=data._asdict())
    print(r)
