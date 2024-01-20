import os
import re
from glob import glob
import requests
from datetime import datetime, timedelta
from json import dumps
import pathlib

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")
SALES_ENDPOINT = os.getenv("SALES_ENDPOINT")
DISCREPANCIES_ENDPOINT = os.getenv("DISCREPANCIES_ENDPOINT")

header = {
    "Content-Type": "application/json",
    "Authorization": f"token {TOKEN}"
}


def fetch_data_for_date_from(date_to_fetch, endpoint):
    data = {
        "startDate": date_to_fetch,
        "endDate": date_to_fetch
    }
    return requests.post(url=URL.format(endpoint), headers=header, data=dumps(data))


def download_nth_day_discrepancy_data(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    response = fetch_data_for_date_from(start_date, DISCREPANCIES_ENDPOINT)
    with open(f"reports/{parse_date}.txt", 'w') as f:
        f.write(response.text)


def download_sale_lines_for_date(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    response = fetch_data_for_date_from(parse_date, SALES_ENDPOINT)
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


def trigger_job():
    start_date = datetime.strptime("2022-12-29", "%Y-%m-%d").date()
    end_date = datetime.strptime("2022-12-29", "%Y-%m-%d").date()

    while start_date <= end_date:
        start = datetime.now()
        print(f'Fetching data for {start_date} --- {start}')
        # start_date = datetime.strptime("2022-07-21", "%Y-%m-%d").date()
        # download_sale_lines(start_date)
        download_nth_day_discrepancy_data(start_date)
        start_date = start_date + timedelta(days=1)
        print(f'Ending time --- {datetime.now() - start}')


if __name__ == '__main__':
    trigger_job()
