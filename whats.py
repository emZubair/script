from json import dumps, loads
import requests

TOKEN = """
EAARw9rV5Fy4BAHwvcIEbWpdhAGLOU9CFE742y7GWTEVOaBLVPbXBr8dpL3hNeYg5MkTa3gcsfERWntgq83bfzWmLvBIQqhAyxSMzl0JuSapJIgzfMDBVBjAYX6PaK1lLdEG0G6UWVYfPUvYMGlET1QUEhE3vOexSA7L4z1qwZCIh45J1I
"""

user_token = "EAARw9rV5Fy4BAEAKREEaKIBujQzbZC8ZAQZAo8IeKQCONQ2UncDAVWI4cqrZAU5kC8482ky4jZCkBDOfpK8v9p1esPEkXWfKQ711wUFZBvkhl6FEvVE7ZBvd7fJZByhp9jWquONXUOjyvN8UpGRHplLtPNczB8Q5wShVhCQ2gr1SZAZBYZBlhNxUfAsFLAbzZB78sUksAY2LG0KBRgZDZD"
d_token = "EAARw9rV5Fy4BAGqMzTdF0fZBYVXhxCC1MDvXhGETB3I0xNofq28sAnO3Jn6hWW1n3XyRRtZBmZB2YEgwjfuy0ATZB2WT7ln6vthwqTnYuKyHrSveyfZCsY60KLcD6JmOAa8xdnlqISXHrl9NPTklL4bwITbarTFnOwAh78NdQPzaT3sud4bckO3HL4jZACne1of7o2HZBZAltQZDZD"
header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer EAARw9rV5Fy4BAGqMzTdF0fZBYVXhxCC1MDvXhGETB3I0xNofq28sAnO3Jn6hWW1n3XyRRtZBmZB2YEgwjfuy0ATZB2WT7ln6vthwqTnYuKyHrSveyfZCsY60KLcD6JmOAa8xdnlqISXHrl9NPTklL4bwITbarTFnOwAh78NdQPzaT3sud4bckO3HL4jZACne1of7o2HZBZAltQZDZD"
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

