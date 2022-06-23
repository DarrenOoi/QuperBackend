from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from waybackpy import WaybackMachineSaveAPI
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
def getFrequency(url):
    bor = webdriver.Chrome(executable_path='chromedriver')
    bor.get('https://archive.org/web/')
    # bor.get('https://www.getbring.com/en/privacy-policy')
    # 定位输入框
    input_box = bor.find_element(by=By.ID,value='wwmurl')
    try:
        input_box.send_keys(url)
    except Exception:
        pass
    # 定位搜索按钮
    button = bor.find_element(by=By.NAME , value='type')
    try:
        button.click()
    except Exception:
        pass

    sleep(5)
    times = None
    interval = None
    # newOne = None
    # 定位时间戳位置
    try:
        times = bor.find_element(by=By.CLASS_NAME , value='captures-range-info').find_element(by=By.TAG_NAME , value='strong').text
        interval = bor.find_element(by=By.CLASS_NAME , value='captures-range-info').find_element(by=By.TAG_NAME , value='span').text
        # save_api = WaybackMachineSaveAPI(url, USER_AGENT)
        # save_api.save()
        # newOne = save_api.timestamp()
    except Exception:
        print(111)
        pass
    print(times)
    print(interval)
    # print(newOne)
    return times , interval

# getFrequency("https://www.energyhub.com/privacy")
getFrequency('https://www.allegion.com/corp/en/footer/privacy-statement/da.html')