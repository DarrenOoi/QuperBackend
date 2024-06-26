from bs4 import BeautifulSoup
import requests
from .predict_content import pre_title
from .find_Title import findTitleLabel


def all_process(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx responses
        soup = BeautifulSoup(response.content, features="html.parser")

        # Perform analysis on the soup object and generate results
        results = analyze_soup(soup)
        soup.decompose()
        return results
    except requests.exceptions.RequestException as e:
        return False


def analyze_soup(soup):
    label = findTitleLabel(soup)
    if label == "TitleWrong":
        print("TitleWrong")
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "N", 0, 1
    title_list = soup.find_all(label)
    # print(title_list)
    type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order = pre_title(
        title_list)

    completeness = {
        "type": type,
        "cookie": cookie,
        "share": share,
        "security": security,
        "right": right,
        "children": children,
        "specialArea": specialArea,
        "update": update,
        "how": how,
        "provide": provide,
        "retention": retention,
        "useData": useData,
        "order": order,
    }
    return completeness
    # return type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order, 0, 0

# print(all_process("https://explore.zoom.us/en/privacy/"))
# print(getFrequency("https://help.abc.net.au/hc/en-us/articles/360001154976-ABC-Privacy-Policy"))


if __name__ == '__main__':
    print(all_process("https://www.stokedskills.com/privacy/escapetheroom.html"))
