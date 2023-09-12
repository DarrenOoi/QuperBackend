import csv
import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from waybackpy import WaybackMachineSaveAPI
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"


def getFrequency(url):
    options = Options()
    options.add_argument('--headless')
    bor = webdriver.Chrome(options=options)
    bor.maximize_window()
    bor.get('https://archive.org/web/')
    # positioning input boxes
    input_box = bor.find_element(by=By.ID, value='wwmurl')
    try:
        input_box.send_keys(url)
    except Exception:
        pass
    # locate the search button
    button = bor.find_element(by=By.NAME, value='type')
    try:
        button.click()
    except Exception:
        pass

    sleep(3)
    startTime = None
    endTime = None
    captures = None
    duplicates = None
    uniques = None
    try:
        url_button = bor.find_element(by=By.ID, value='react-wayback-search').find_element(
            by=By.CLASS_NAME, value='view-navbar').find_elements(by=By.TAG_NAME, value='a')
        url_button[-1].click()
    except:
        pass
        print("could not find urlbutton")

        # Create a WebDriverWait instance with a maximum wait time of 30 seconds (adjust as needed)
    wait = WebDriverWait(bor, 100)

    try:
        wait.until(lambda bor: len(bor.find_elements(
            By.CSS_SELECTOR, '#resultsUrl tbody tr')) > 1)
        root = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '#url-query-result #resultsUrl_wrapper .row:nth-child(2) .col-sm-12 #resultsUrl tbody .odd')))
        alldata = root[0].find_elements(By.TAG_NAME, 'td')

        startTime = alldata[2]
        endTime = alldata[3]
        captures = alldata[4]
        duplicates = alldata[5]
        uniques = alldata[6]
    except Exception as e:
        print("Could not find content:", str(e))

    timeline = {
        "start": startTime.text if startTime else None,
        "end": endTime.text if endTime else None,
        "captures": captures.text if captures else None,
        "duplicates": duplicates.text if duplicates else None,
        "uniques": uniques.text if uniques else None,
    }

    return timeline


def Find(string):
    # findall() Finding strings that match a regular expression
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


def Find_kuohao(string):
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    list1 = re.findall(p1, string)
    # print(list1)
    result = []
    for i in list1:
        index_douhao = i.index(",")
        g = i[:index_douhao]
        result.append(g)
        result = list(set(result))
    return result


# print(getFrequency("https://explore.zoom.us/en/privacy/"))
