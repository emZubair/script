from json import dumps, loads
import requests

TOKEN = """

"""

header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "
}

data = {
    "messaging_product": "whatsapp",
    "to": "923336977780",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

URL = "https://graph.facebook.com/v15.0/111283508531530/messages"

response = requests.post(url=URL, headers=header, data=dumps(data), timeout=360)
breakpoint()

