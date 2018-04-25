#! /usr/bin/env python3

import sys
import csv
import json
import requests

__author__ = "Chris Womack"
__copyright__ = "Copyright 2017, ProtectWise"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__status__ = "Prototype"

IOC_URL_LIST_URL = 'https://raw.githubusercontent.com/401trg/detections/master/ioc_urls.txt'
IDS_RULES_URL_LIST_URL = 'https://raw.githubusercontent.com/401trg/detections/master/ids_rules_urls.txt'


def get_urls_list(url_list_url):
    """ Takes in a url and returns list of urls for IOCs and IDS Rules
    :param url_list_url: URL from 401TRG github with list of urls for IOC files and IDS files
    :return: List of file URLS
    """
    url_list_request_data = requests.get(url_list_url, timeout=1)
    list_of_urls = url_list_request_data.text.splitlines()
    return list_of_urls


def get_ioc_list(ioc_urls):
    """ Gets a list of IOCs in Key:Value format
    :param ioc_urls: list of urls for IOC files
    :return: list of IOCs in Key:Value format
    """

    ioc_list = list()
    for ioc_url in ioc_urls:
        ioc_request_data = requests.get(ioc_url, timeout=1)
        tmp_dict = csv.DictReader(ioc_request_data.text.splitlines())
        for ioc in tmp_dict:
            ioc_list.append(json.dumps(ioc))
    return ioc_list


def get_ids_rules_list(ids_rules_urls):
    """ Gets a list of IOCs in Key:Value format
    :param ids_rules_urls: list of urls for IOC files
    :return: list of IOCs in Key:Value format
    """

    ids_rules_list = list()
    for ids_rules_url in ids_rules_urls:
        ids_rules_request_data = requests.get(ids_rules_url, timeout=1)
        tmp_list = ids_rules_request_data.text.splitlines()
        ids_rules_list.extend(tmp_list)

    return ids_rules_list


if __name__ == "__main__":
    # IOC Example
    ioc_urls = get_urls_list(IOC_URL_LIST_URL)
    ioc_list = get_ioc_list(ioc_urls)
    #for ioc in ioc_list:
    #    print(ioc)

    # IDS Example
    ids_rules_urls = get_urls_list(IDS_RULES_URL_LIST_URL)
    ids_rules_list = get_ids_rules_list(ids_rules_urls)
    #for ids_rule in ids_rules_list:
    #    print(ids_rule)
