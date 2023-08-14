import csv
import os

from bs4 import BeautifulSoup

import pandas as pd
from predict_content import pre_title
from find_Title import findTitleLabel


def all_process(path):
    try:
        soup = BeautifulSoup(open(path),features="html.parser")
    except Exception:
        print('Formatting issues')
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"N",1, 0
    label = findTitleLabel(path)
    if label == "TitleWrong":
        print("TitleWrong")
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"N",0, 1
    title_list = soup.find_all(label)
    # print(title_list)
    type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order = pre_title(title_list)
    return type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order , 0, 0

print(all_process("./pp_example/69_Developer Privacy Policy.html"))

