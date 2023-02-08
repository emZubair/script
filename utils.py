import os
import re
from glob import glob
import requests
from json import dumps
import pathlib

URL = os.getenv("LOCAL_URL")
DISCREPANCIES_ENDPOINT = "download-order-sales-range"
SALES_ENDPOINT = "download-range-sales"
TOKEN = os.getenv("LOCAL_TOKEN")
header = {
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
}


def download_nth_day_data(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    data = {
        "startDate": parse_date,
        "endDate": parse_date
    }
    response = requests.post(url=URL.format(DISCREPANCIES_ENDPOINT), headers=header, data=dumps(data))
    with open(f"reports/{parse_date}.txt", 'w') as f:
        f.write(response.text)


def download_sale_lines(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    data = {
        "startDate": parse_date,
        "endDate": parse_date
    }
    response = requests.post(url=URL.format(SALES_ENDPOINT), headers=header, data=dumps(data), timeout=360)
    with open(f"sales/{parse_date}.txt", 'w') as f:
        f.write(response.text)


def find_discrepancies():
    p = re.compile('true', re.IGNORECASE)
    path = pathlib.Path(__file__).parent.resolve()
    file_path = os.path.join(path, "reports")
    for file in glob(os.path.join(file_path, '*.txt')):
        with open(file) as logfile:
            for i, line in enumerate(map(str.strip, logfile), 1):
                if p.search(line) is not None:
                    print(line)
