import requests
from bs4 import BeautifulSoup
import re

def find_external_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    external_links = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        if re.match(r'^https?://', href):
            external_links.append(href)

    return external_links

def check_status_codes(links):
    status_codes = {}

    for link in links:
        try:
            response = requests.get(link)
            status_codes[link] = response.status_code
        except requests.exceptions.RequestException:
            status_codes[link] = 'Error'

    return status_codes

if __name__ == "__main__":
    html_file_path = "./pp_example/30952.html"

    external_links = find_external_links(html_file_path)
    status_codes = check_status_codes(external_links)

    for link, status_code in status_codes.items():
        print(f"Link: {link} - Status Code: {status_code}")