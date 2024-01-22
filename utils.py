# pylint: disable=unused-variable, missing-timeout, unspecified-encoding, wildcard-import, unused-wildcard-import
import os
import pathlib
import re
from datetime import datetime, timedelta
from glob import glob
from json import dumps

import requests

from variables import *

header = {"Content-Type": "application/json", "Authorization": f"token {TOKEN}"}


def create_directories():
    for path in ["reports", "sales", "payments"]:
        if not os.path.exists(path):
            os.makedirs(path)


def fetch_data_for_date_from(date_to_fetch, endpoint):
    data = {"startDate": date_to_fetch, "endDate": date_to_fetch}
    return requests.post(url=f"{URL}{endpoint}/", headers=header, data=dumps(data))


def download_nth_day_discrepancy_data(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    response = fetch_data_for_date_from(start_date, DISCREPANCIES_ENDPOINT)
    with open(f"reports/{parse_date}.csv", "w") as f:
        f.write(response.text)


def download_sale_lines_for_data(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    response = fetch_data_for_date_from(parse_date, SALES_ENDPOINT)
    with open(f"sales/{parse_date}.csv", "w") as f:
        f.write(response.text)


def download_payment_lines_for_data(start_date):
    parse_date = start_date.strftime("%Y-%m-%d")
    response = fetch_data_for_date_from(parse_date, PAYMENTS_ENDPOINT)
    with open(f"payments/{parse_date}.csv", "w") as f:
        f.write(response.text)


def find_discrepancies():
    p = re.compile("true", re.IGNORECASE)
    path = pathlib.Path(__file__).parent.resolve()
    file_path = os.path.join(path, "reports")
    for file in glob(os.path.join(file_path, "*.txt")):
        with open(file) as logfile:
            for i, line in enumerate(map(str.strip, logfile), 1):
                if p.search(line) is not None:
                    print(line)


def trigger_job():
    end_date = datetime.strptime(END_DATE, "%Y-%m-%d").date()
    start_date = datetime.strptime(START_DATE, "%Y-%m-%d").date()
    create_directories()

    while start_date <= end_date:
        start = datetime.now()
        print(f"Fetching data for {start_date} --- {start}")
        if DOWNLOAD_PAYMENTS:
            download_payment_lines_for_data(start_date)
        if DOWNLOAD_SALES:
            download_sale_lines_for_data(start_date)
        if DOWNLOAD_DISCREPANCIES_DATA:
            download_nth_day_discrepancy_data(start_date)
        start_date = start_date + timedelta(days=1)
        print(f"Ending time --- {datetime.now() - start}")


if __name__ == "__main__":
    trigger_job()
