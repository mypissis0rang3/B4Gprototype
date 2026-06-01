
import requests
try:
    r = requests.get("http://#insert ip adress/VOLUME", timeout=5)
    print(r.text)
except Exception as e:
    print(e)

#requests: HELLO,  MIDDLEF, VOLUME, SILENCE
