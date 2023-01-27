import re
from glob import glob
import os
import requests
from json import dumps
from datetime import date, timedelta, datetime
import pathlib

from django import forms


URL = "https://api.shopraha.com/sap/api/v1/{}/"
# URL = "http://127.0.0.1:8080/sap/api/v1/{}/"
DISCREPANCIES_ENDPOINT = "download-order-sales-range"
SALES_ENDPOINT = "download-range-sales"
TOKEN = ""
header = {
    "Content-Type": "application/json",
    "Authorization": "token "
}


def find_discrepancies():
    p = re.compile('true', re.IGNORECASE)
    path = pathlib.Path(__file__).parent.resolve()
    file_path = os.path.join(path, "reports")
    for file in glob(os.path.join(file_path, '*.txt')):
        with open(file) as logfile:
            for i, line in enumerate(map(str.strip, logfile), 1):
                if p.search(line) is not None:
                    print(line)


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


def download_one():
    for time in ["2022-07-03"]:
        start = datetime.now()
        start_date = datetime.strptime(time, "%Y-%m-%d").date()
        print(f'Fetching data for {start_date} --- {start}')
        download_nth_day_data(start_date)
        print(f'Ending time --- {datetime.now() - start}')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    find_discrepancies()
    return
    start_date = datetime.strptime("2022-12-29", "%Y-%m-%d").date()
    end_date = datetime.strptime("2022-12-29", "%Y-%m-%d").date()
    # end_date = date.today()
    while start_date <= end_date:
        start = datetime.now()
        print(f'Fetching data for {start_date} --- {start}')
        # start_date = datetime.strptime("2022-07-21", "%Y-%m-%d").date()
        # download_sale_lines(start_date)
        download_nth_day_data(start_date)
        start_date = start_date + timedelta(days=1)
        print(f'Ending time --- {datetime.now() - start}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
