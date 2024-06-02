import re
import pandas as pd
from selenium import webdriver
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook


def get_language():
    df = pd.read_excel('language.xlsx', usecols=[2])
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


def selectFunction(url):
    language = []
    options = Options()
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    bor = webdriver.Chrome(options=options)
    # bor = webdriver.Chrome('chromium.chromedriver', options=options)
    bor.maximize_window()
    # bor = webdriver.Chrome(executable_path='chromedriver')
    # bor.get('https://www.nordlux.com/legal/privacy-policy/')
    # bor.get('https://www.allegion.com/corp/en/footer/privacy-statement/da.html')
    try:
        bor.get(url)
    except Exception:
        return "The path error"
    # bor.get('https://www.nordlux.com/legal/privacy-policy/')
    # bor.get('https://www.mbusa.com/en/legal-notices/privacy-statement')
    # bor.get('https://s3.amazonaws.com/pvoutput/pvoutput+privacy.html')
    # bor.get('https://www.freeprivacypolicy.com/privacy/view/dc6236d2134910777ccc7c83056aa1dd')
    # bor.get('https://halomesh.com/MeshClouds/Privacy.html')
    # bor.get('https://www.home-connect.com/us/en/app-legal/legal/app-data-protection')
    # bor.get('https://www.google.com/')
    # a = bor.page_source
    bor.refresh()
    try:
        languageButton = bor.find_element(
            by=By.XPATH, value="//*[contains(text(),'English')]").click()
    except Exception:
        try:
            languageButton = bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Australia')]").click()
        except Exception:
            try:
                languageButton = bor.find_element(
                    by=By.XPATH, value="//*[contains(text(),'English')]")
            except Exception:
                try:
                    languageButton = bor.find_element(
                        by=By.XPATH, value="//*[contains(text(),'Australia')]")
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

    # 意大利语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Italian')]")
        language.append("Italian")
    except Exception:
        pass
    # 法语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'French')]")
        language.append("French")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Français')]")
            language.append("French")
        except Exception:
            pass
        pass
    # 日语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Japanese')]")
        language.append("Japanese")
    except Exception:
        pass
    # 葡萄牙语
    try:
        bor.find_element(
            by=By.XPATH, value="//*[contains(text(),'Portuguese')]")
        language.append("Portuguese")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Português')]")
            language.append("Portuguese")
        except Exception:
            pass
        pass
    # 西班牙语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Spanish')]")
        language.append("Spanish")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Español')]")
            language.append("Spanish")
        except Exception:
            pass
        pass
    # 海地语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Hindi')]")
        language.append("Hindi")
    except Exception:
        pass
    # 阿拉伯语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Arabic')]")
        language.append("Arabic")
    except Exception:
        pass
    # 中文
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'中文')]")
        language.append("Chinese")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Chinese')]")
            language.append("Chinese")
        except Exception:
            pass
        pass
    # 丹麦语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Dansk')]")
        language.append("Dansk")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Danish')]")
            language.append("Dansk")
        except Exception:
            pass
        pass
    # 韩语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'한국어')]")
        language.append("Korean")
    except Exception:
        try:
            bor.find_element(by=By.XPATH, value="//*[contains(text(),'한국어')]")
            language.append("Korean")
        except Exception:
            pass
        pass
    # 荷兰语
    try:
        bor.find_element(
            by=By.XPATH, value="//*[contains(text(),'Nederlands')]")
        language.append("Dutch")
    except Exception:
        pass

    # 挪威语
    try:
        bor.find_element(
            by=By.XPATH, value="//*[contains(text(),'Norwegian')]")
        language.append("Norsk")
    except Exception:
        pass

    # 波兰语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'POLSKI')]")
        language.append("Polish")
    except Exception:
        pass
    # 瑞典语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Svenska')]")
        language.append("Swedish")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Swedish')]")
            language.append("Swedish")
        except Exception:
            pass
        pass
    # 土耳其语
    try:
        bor.find_element(by=By.XPATH, value="//*[contains(text(),'Türkçe')]")
        language.append("Turkish")
    except Exception:
        try:
            bor.find_element(
                by=By.XPATH, value="//*[contains(text(),'Turkish')]")
            language.append("Turkish")
        except Exception:
            pass
        pass

    language = list(set(language))
    bor.quit()
    return language


def Find(string):
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


# if __name__ == '__main__':
    # a = selectFunction("https://docs.google.com/document/d/1kNx08hnAqT9GYH-SKV77uxG3YCHGizuKgHLNLOd9L2g/edit")
    # url = "https://www.nordlux.com/legal/privacy-policy/"
    # test_sup_languages = selectFunction(url)
    # print(test_sup_languages)
