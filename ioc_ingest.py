import csv
import requests

__author__ = "Chris Womack"
__copyright__ = "Copyright 2017, ProtectWise"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__status__ = "Prototype"

ioc_list_url = 'https://raw.githubusercontent.com/401trg/detections/master/ioc_urls.txt'

ioc_list_request_data = requests.get(ioc_list_url)
ioc_urls = ioc_list_request_data.text.splitlines()

for ioc_url in ioc_urls:
    ioc_request_data = requests.get(ioc_list_url)
    ioc_dict = csv.DictReader(ioc_request_data.text)

    for row in ioc_dict:
        print(row)