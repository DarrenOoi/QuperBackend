import csv
import re

import bs4
import joblib

# from bayesian import clf,tf
from bs4 import BeautifulSoup

# mark_txt = {'0':"personal_information_type.txt",'1':"personal_information_type.txt",'2':"personal_information_type.txt",
#             '3':"share_information.txt",'4':"protect_information.txt",
#             '5':"advertising.txt",'6':"user_right.txt",'7':"special_group.txt",
#             '8':"special_area.txt",'9':"update.txt",'10':"way_to_collect.txt",
#             '11':"provider.txt",'12':"data_retention.txt",'13':"personal_information_type.txt",'14':"thrid_party.txt",'15':"personal_infoinformation_tyoe.txt"}
clf = joblib.load('classifier.pkl')
tf = joblib.load('tf.pkl')
def pre_title(title_list):
    type = 0
    cookie = 0
    share = 0
    security = 0
    right = 0
    children = 0
    specialArea = 0
    update = 0
    how = 0
    provide = 0
    retention = 0
    useData = 0
    # 清除tag是点的内容
    clean_title_list = []
    for title in title_list:
        if title.text != "•":
            clean_title_list.append(title)
    lastMark = ""
    for title in clean_title_list:
        title_Str = re.sub(r'\s+', ' ', str(title))
        title_Str = re.sub(r'<[^<]+?>', '', title_Str).replace('\n', '').strip()
        title_Str = title_Str.lower()
        # print(clf.predict(tf.transform([title.string])))
        # print("----------")
        if title is None:
            continue
        try:
            mark = clf.predict(tf.transform([title_Str]))
            if mark[0] == "1":
                type = 1
            elif mark[0] == "2":
                cookie = 1
            elif mark[0] == "3":
                share = 1
            elif mark[0] == "4":
                security = 1
            elif mark[0] == "6":
                right = 1
            elif mark[0] == "7":
                children = 1
            elif mark[0] == "8":
                specialArea = 1
            elif mark[0] == "9":
                update = 1
            elif mark[0] == "10":
                how = 1
            elif mark[0] == "11":
                provide = 1
            elif mark[0] == "12":
                retention = 1
            elif mark[0] == "13":
                useData = 1
        except Exception as e:
            continue

    return type , cookie , share , security , right , children , specialArea , update , how ,  provide , retention , useData


# def get_text(title_list):
#     type = 0
#     security = 0
#     right = 0
#     specialGroup = 0
#     specialArea = 0
#     update = 0
#     retention = 0
#     useData = 0
#     #清除tag是点的内容
#     clean_title_list = []
#     for title in title_list:
#         if title.text != "•":
#             clean_title_list.append(title)
#     lastMark = ""
#     for title in clean_title_list:
#         title_Str = re.sub(r'\s+', ' ',str(title))
#         title_Str = re.sub(r'<[^<]+?>', '', title_Str).replace('\n','').strip()
#         # print(clf.predict(tf.transform([title.string])))
#         # print("----------")
#         if title is None:
#             continue
#         try:
#             mark = clf.predict(tf.transform([title_Str]))
#         except Exception as e:
#             continue
#         # print(mark)
#         # if mark == "1":
#         #     type = 1
#         # if mark == "4":
#         #     security = 1
#         # if mark == "6":
#         #     right = 1
#         # if mark == "13":
#         #     useData = 1
#         # if mark == "8":
#         #     specialArea = 1
#         # if mark == "9":
#         #     update = 1
#         if mark == "12":
#             retention = 1
#
#         # if mark == "7":
#         #     specialGroup = 1
#         #     # print("这里的数字是"+str(specialGroup))
#         if mark == "0":
#             if lastMark != "":
#                 mark = lastMark
#         lastMark = mark
#         for sibling in title.next_elements:
#             # print(type(sibling))
#                 # 如果碰到了下一个title停止循环
#             try:
#                 if clean_title_list[clean_title_list.index(title) + 1] == sibling:
#                     # if clf.predict(tf.transform([sibling.string])) == "0":
#                     #     print(1)
#                     # else:
#                         break
#             except Exception:
#                 continue
#             if isinstance(sibling, bs4.element.Tag):
#                 continue
#             if str(sibling) == '\n':
#                 continue
#             if sibling == title.string:
#                 continue
#             # 处理最后一段
#             if clean_title_list.index(title) == len(clean_title_list) - 1:
#                 with open(mark_txt.get(mark[0]),"a") as f:
#                     currentSibing = str(sibling)
#                     if currentSibing[-1].isalpha() or currentSibing[-1] == ")":
#                         currentSibing = currentSibing + "."
#                     f.write(currentSibing)
#                     f.close()
#             else:
#                 with open(mark_txt.get(mark[0]),"a") as g:
#                     # print(str(sibling))
#                     # print("------------------------")
#                     currentSibing = str(sibling)
#                     if currentSibing[-1].isalpha() or currentSibing[-1] == ")":
#                         currentSibing = currentSibing + "."
#                     g.write(currentSibing)
#                     g.write("\n")
#                     g.close()
#                 if mark[0] == "15":
#                     with open("use_data.txt", "a") as g:
#                         # print(str(sibling))
#                         # print("------------------------")
#                         currentSibing = str(sibling)
#                         if currentSibing[-1].isalpha() or currentSibing[-1] == ")":
#                             currentSibing = currentSibing + "."
#                         g.write(currentSibing)
#                         g.write("\n")
#                         g.close()
#     return type,security,right,specialArea,specialGroup,update,retention,useData


# soup1 = BeautifulSoup(open("./Alexa-privacy-policy-main/Privacy-policy-all/29463.html"),features="lxml")
# title_list = soup1.find_all('h2')
# print(title_list)
#
# soup1 = BeautifulSoup(open("./Alexa-privacy-policy-main/test/57040.html"),features="lxml")
# title_list = soup1.find_all('strong')
# print(title_list)

# #
# soup2 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Disclosures, Privacy Policy, & Agreements | Cutting Edge FCU.html"),features="lxml")
# title_list = soup2.find_all('th')
# title_list2 = soup2.find_all('h4')
# for title in title_list2:
#     title_list.append(title)
# print(title_list)
# get_text(title_list)
#
soup3 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/House Hacker - Privacy Policy.html"),features="html.parser")
title_list = soup3.find_all('h3')
print(title_list)
a = pre_title(title_list)
print(a)
#
# soup4 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/index.html"),features="lxml")
# title_list = soup4.find_all('h1')
# get_text(title_list)
#
# soup5 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Notice – Wes Moss.html"),features="lxml")
# [s.extract() for s in soup5('script')]
# title_list = soup5.find_all('h4')
# # print(title_list)
# get_text(title_list)
#
# soup6 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Notice – Wes Moss.html"),features="lxml")
# title_list = soup6.find_all('strong')
# get_text(title_list)
#
# soup7= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy - MRI Software.html"),features="lxml")
# title_list = soup7.find_all('strong')
# print(title_list)
# get_text(title_list)
#
# soup8= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy - Rheem HVAC Websuite.html"),features="lxml")
# title_list = soup8.find_all('strong')
# get_text(title_list)
#
# soup9= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy – SpokenLayer.html"),features="lxml")
# title_list = soup9.find_all('h2')
# get_text(title_list)
#
# soup10= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy | Smartkarma.html"),features="lxml")
# title_list = soup10.find_all('strong')
# get_text(title_list)
#
# soup11= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/PRIVACY POLICY | The Franchise Lady.html"),features="lxml")
# title_list = soup11.find_all('h2')
# title_list1 = []
# for title in title_list:
#     title_list1.append(title.string)
# get_text(title_list1)
# get_text(title_list1)

# soup12= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy for Flash News with River Waters.html"),features="lxml")
# title_list = soup12.find_all('h2')
# title_list1 = soup12.find_all('h1')
# for title in title_list1:
#     title_list.append(title)
# get_text(title_list)
#
# soup13= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Privacy Policy.html"),features="lxml")
# title_list = soup13.find_all('strong')
# title_list1 = []
# for title in title_list:
#     title_list1.append(title.string)
# get_text(title_list1)
# get_text(title_list1)
#
# soup14= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/privacypolicy.htm"),features="lxml")
# title_list = soup14.find_all(name="div", attrs={"class" :"grayText"})
# get_text(title_list)
#
#
# soup15= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/SIXTHBLOCK.html"),features="lxml")
# title_list = soup15.find_all('h2')
# title_list1 = []
# for title in title_list:
#     title_list1.append(title.string)
# get_text(title_list1)
# get_text(title_list1)
#
# soup16= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/Termly.html"),features="lxml")
# title_list = soup16.find_all(name="span", attrs={"data-custom-class" :"heading_1"})
# title_list1 = []
# for title in title_list:
#     title_list1.append(title.string)
# get_text(title_list1)
# get_text(title_list1)
#
# soup17= BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/voboai.html"),features="lxml")
# title_list = soup17.find_all('h3')
# get_text(title_list)
#
# soup18 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/TIAA/Online privacy notice | TIAA.html"),features="lxml")
# title_list = soup18.find_all('h3')
# title_list1 = []
# for title in title_list:
#     title_list1.append(title.string)
# get_text(title_list1)
#
# soup19 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/TIAA/TIAA Bank Online Privacy Practices TIAA Bank.html"),features="lxml")
# title_list = soup19.find_all('h4')
# get_text(title_list)
#
# soup20 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/TIAA/escapetheroomPrivacy Policy.html"),features="lxml")
# title_list = soup20.find_all('strong')
# get_text(title_list)
#
# soup21 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/TIAA/Privacy Policy - EnergyHub.html"),features="lxml")
# title_list = soup21.find_all('h3')
# get_text(title_list)
#
# soup22 = BeautifulSoup(open("./Alexa-privacy-policy-main/PrivacyPolicyData(0-50)/TIAA/matchboxPrivacy Policy.html"),features="lxml")
# title_list = soup22.find_all('strong')
# get_text(title_list)

# soup23 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/5086.html"),features="lxml")
# title_list = soup23.find_all('b')
# get_text(title_list)

# soup24 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/59.html"),features="lxml")
# title_list = soup24.find_all('h2')
# get_text(title_list)

# soup25 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/548.html"),features="lxml")
# title_list = soup25.find_all('strong')
# get_text(title_list)

# soup26 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/572.html"),features="lxml")
# title_list = soup26.find_all('h2')
# get_text(title_list)
#
# soup27 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/809.html"),features="lxml")
# title_list = soup27.find_all('h3')
# get_text(title_list)
#
# soup28 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/853.html"),features="lxml")
# title_list = soup28.find_all('strong')
# get_text(title_list)
#
# soup29 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/877.html"),features="lxml")
# title_list = soup29.find_all('h4')
# get_text(title_list)
#
# soup30 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/1192.html"),features="lxml")
# title_list = soup30.find_all('h3')
# get_text(title_list)
#
# soup31 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/1875.html"),features="lxml")
# title_list = soup31.find_all('h4')
# get_text(title_list)
#
# soup32 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2012.html"),features="lxml")
# title_list = soup32.find_all('h2')
# get_text(title_list)
#
# soup33 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2177.html"),features="lxml")
# title_list = soup33.find_all('h2')
# get_text(title_list)
#
# soup34 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2337.html"),features="lxml")
# title_list = soup34.find_all('h4')
# get_text(title_list)
#
# soup35 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2510.html"),features="lxml")
# title_list = soup35.find_all('h3')
# get_text(title_list)
#
# soup36 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2596.html"),features="lxml")
# title_list = soup36.find_all('strong')
# get_text(title_list)
#
# soup37 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/2838.html"),features="lxml")
# title_list = soup37.find_all('strong')
# get_text(title_list)
#
# soup38 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/3008.html"),features="lxml")
# title_list = soup38.find_all('strong')
# get_text(title_list)
#
# soup39 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/4054.html"),features="lxml")
# title_list = soup39.find_all('h5')
# get_text(title_list)
#
# # soup40 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/4844.html"),features="lxml")
# # title_list = soup40.find_all('h3')
# # get_text(title_list)
#
# soup41 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/6116.html"),features="lxml")
# title_list = soup41.find_all('h2')
# get_text(title_list)
#
# soup42 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/6268.html"),features="lxml")
# title_list = soup42.find_all('h5')
# get_text(title_list)
#
# soup43 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/6655.html"),features="lxml")
# title_list = soup43.find_all('strong')
# get_text(title_list)
#
# soup44 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/6734.html"),features="lxml")
# title_list = soup44.find_all('h6')
# get_text(title_list)
#
# soup45 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/7494.html"),features="lxml")
# title_list = soup45.find_all('strong')
# get_text(title_list)
#
# soup46 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/7833.html"),features="lxml")
# title_list = soup46.find_all('h2')
# get_text(title_list)
#
# soup47 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/10200.html"),features="lxml")
# title_list = soup47.find_all('h2')
# get_text(title_list)
#
# soup48 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/11536.html"),features="lxml")
# title_list = soup48.find_all('h2')
# get_text(title_list)

# soup49 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/11618.html"),features="lxml")
# title_list = soup49.find_all('strong')
# get_text(title_list)

# soup50 = BeautifulSoup(open("./Alexa-privacy-policy-main/PP/11898.html"),features="lxml")
# title_list = soup50.find_all('b')
# get_text(title_list)

# soup51= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/45808.html"),features="lxml")
# title_list = soup51.find_all('h2')
# get_text(title_list)

#加强点，离谱
# soup52= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/62551.html"),features="lxml")
# title_list = soup52.find_all('strong')
# get_text(title_list)

# soup53= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/64520.html"),features="lxml")
# title_list = soup53.find_all('strong')
# get_text(title_list)

# soup54= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/62239.html"),features="lxml")
# title_list = soup54.find_all('h4')
# get_text(title_list)

# soup55= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/62182.html"),features="lxml")
# title_list = soup55.find_all('strong')
# get_text(title_list)

# soup56= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/61934.html"),features="lxml")
# title_list = soup56.find_all('h2')
# get_text(title_list)

# soup57= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/61384.html"),features="lxml")
# title_list = soup57.find_all('h2')
# get_text(title_list)

# soup58= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/61357.html"),features="lxml")
# title_list = soup58.find_all('h3')
# get_text(title_list)

# soup59= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/58621.html"),features="lxml")
# title_list = soup59.find_all('strong')
# get_text(title_list)

# soup60= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/58282.html"),features="lxml")
# title_list = soup60.find_all('h3')
# get_text(title_list)
#
# soup61= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57983.html"),features="lxml")
# title_list = soup61.find_all('h2')
# get_text(title_list)

# soup62= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57978.html"),features="lxml")
# title_list = soup62.find_all('h2')
# get_text(title_list)

# soup63= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57917.html"),features="lxml")
# title_list = soup63.find_all('h3')
# get_text(title_list)
#
# soup64= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57879.html"),features="lxml")
# title_list = soup64.find_all('h3')
# get_text(title_list)
#
# soup65= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57799.html"),features="lxml")
# title_list = soup65.find_all('strong')
# get_text(title_list)
#
# soup66= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57786.html"),features="lxml")
# title_list = soup66.find_all('h2')
# get_text(title_list)
#
# soup67= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57743.html"),features="lxml")
# title_list = soup67.find_all('h3')
# get_text(title_list)

# soup68= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57543.html"),features="lxml")
# title_list = soup68.find_all('h2')
# get_text(title_list)

# soup69= BeautifulSoup(open("./Alexa-privacy-policy-main/PP/57539.html"),features="lxml")
# title_list = soup69.find_all('h3')
# get_text(title_list)

# soup70= BeautifulSoup(open("./Alexa-privacy-policy-main/PP-standard/56085.html"),features="lxml")
# title_list = soup70.find_all('h2')
# get_text(title_list)






# print(type_list)