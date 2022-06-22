import pandas as pd
from selenium import webdriver
from time import sleep

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ChromeOptions
# 拿到所有非英语的语言
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def get_language():
    df = pd.read_excel('language.xlsx',usecols=[2])
    data = df.values
    types = []
    for dt in data:
        if "," in dt[0]:
            templatearray = dt[0].split(',')
            for lang in templatearray:
                if lang[:3] != "Eng" and lang[:3] != " En":
                    if lang not in types:
                        types.append(lang)
    print(types)

# [' Italian (IT)', ' German (DE)', ' French (CA)', ' French (FR)', ' Japanese (JP)', ' Portuguese (BR)',
# ' Spanish (ES)', ' Spanish (MX)', ' Spanish (US)', ' Hindi (IN)', 'Spanish (ES)', 'Spanish (MX)', 'Arabic (SA)',
# 'French (FR)', 'French (CA)', 'Portuguese (BR)']

def get_url():
    df = pd.read_excel('language.xlsx', usecols=[1])
    data = df.values
    format = ": \""
    for dt in data:
        index = dt[0].index(format)
        index = index + 2
        url = dt[0][index:]
        url = url.strip('\"}')
        if "Developer Privacy Policy" in url:
            for i in url:
                if i == "\"":
                    iconIndex = url.index(i)
                    url = url[:iconIndex]
                    break
        print(url)
# get_url()

def selectFunction():
    language = []
    bor = webdriver.Chrome(executable_path='chromedriver')
    # bor.get('https://www.nordlux.com/legal/privacy-policy/')
    # bor.get('https://www.getbring.com/en/privacy-policy')
    # bor.get('https://www.mbusa.com/en/legal-notices/privacy-statement')
    # bor.get('https://s3.amazonaws.com/pvoutput/pvoutput+privacy.html')
    # bor.get('https://www.freeprivacypolicy.com/privacy/view/dc6236d2134910777ccc7c83056aa1dd')
    # bor.get('https://halomesh.com/MeshClouds/Privacy.html')
    bor.get('https://www.home-connect.com/us/en/app-legal/legal/app-data-protection')
    # bor.get('https://www.google.com/')
    # a = bor.page_source
    bor.refresh()
    try:
        languageButton = bor.find_element(by=By.XPATH , value="//*[contains(text(),'English')]").click()
    except Exception:
        return language
    # 德语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Deutsch')]")
        language.append("Deutsch")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'German')]")
        language.append("Deutsch")
    except Exception:
        pass


    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Italian')]")
        language.append("Italian")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'French')]")
        language.append("French")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Japanese')]")
        language.append("Japanese")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Portuguese')]")
        language.append("Portuguese")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Spanish')]")
        language.append("Spanish")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Hindi')]")
        language.append("Hindi")
    except Exception:
        pass
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Arabic')]")
        language.append("Arabic")
    except Exception:
        pass

    return language

a = selectFunction()
print(a)
