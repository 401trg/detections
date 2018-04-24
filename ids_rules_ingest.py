import csv
import requests

__author__ = "Chris Womack"
__copyright__ = "Copyright 2017, ProtectWise"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__status__ = "Prototype"

ids_rules_list_url = 'https://raw.githubusercontent.com/401trg/detections/master/ids_rules_urls.txt'

ids_list_request_data = requests.get(ids_rules_list_url)
ids_rules_urls = ids_list_request_data.text.splitlines()

for ids_rules_url in ids_rules_urls:
    ids_rules_request_data = requests.get(ids_rules_url)
    ids_rules_list = ids_rules_request_data.text.splitlines()

    for row in ids_rules_list:
        print(row)