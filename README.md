## Script ![Code Quality](https://github.com/emZubair/script/actions/workflows/code_quality.yml/badge.svg)

A sample python project that uses `requests` package to place different request at different endpoints.
The request response is saved in `.csv` files, files are named by the dates, which is passed as param to 
the endpoints.

### Environment Variables 
Declare the following environment variables

`URL`: The URL to access

`DISCREPANCIES_ENDPOINT`: The Discrepancies endpoint

`SALES_ENDPOINT`: Sales Endpoint

`TOKEN`: Token required by the endpoints

### Details

The following endpoints can be triggered by this script
1. `download_payment_lines_for_data`: Fetches the payment lines for the respective day
2. `download_sale_lines_for_data`: Fetches the sale lines for the respective day
3. `download_nth_day_discrepancy_data`: Fetches the order data along with discrepancy status for each order

Set the following variables in `variables.py`

`DOWNLOAD_PAYMENTS` -> should download the payment data or not, defaults to `True`

`DOWNLOAD_SALES` -> should download the sale data or not, defaults to `True`

`DOWNLOAD_DISCREPANCIES_DATA` -> should download the discrepancy data or not, defaults to `False`

`START_DATE` -> Start date in string following ISO format `%Y-%m-%d` defaults to "2024-1-1"

`END_DATE` -> End date in string following ISO format `%Y-%m-%d` defaults to "2024-1-1"


### Install the Requirements
Run the following command to install the requirements
```python
pip install -r requirements.txt
```

### Execution

`utils.py` contains a function named `trigger_job`, run the following command to trigger the job.
```python
python utils.py
```