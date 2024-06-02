from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"


def getFrequency(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    bor = webdriver.Chrome(options=options)
    bor.maximize_window()
    wayback_url = f'https://web.archive.org/web/*/{url}*'
    bor.get(wayback_url)

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


# print(getFrequency("https://www.allianz.com/en/privacy-statement.html"))
# print(getFrequency("https://explore.zoom.us/en/privacy/"))
