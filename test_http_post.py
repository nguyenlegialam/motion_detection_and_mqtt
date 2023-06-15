import requests
from datetime import datetime

def post_http():
    # int(datetime.timestamp(datetime.now()))
    url = 'http://127.0.0.1:8000'
    myobj = {'date_time': str(datetime.now()),
             'timestamp': int(datetime.timestamp(datetime.now())),
             'id_camera': 2}

    x = requests.post(url, json = myobj)
    print(x.text)

# post_http()