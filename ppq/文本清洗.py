import re

from 获取文本 import get_text
from nltk.corpus import stopwords
from nltk import word_tokenize,pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# spacy.cli.download("en_core_web_sm")下载模型
# text = "This is Allen's text,    isn't      it?"
text1 = get_text("https://www.stokedskills.com/privacy/escapetheroom.html")
text2 = get_text("https://www.energyhub.com/privacy")
text3 = get_text("https://www.matchbox.io/privacy-policy/")
text4 = get_text("https://www.stokedskills.com/privacy/fiveminuteworkout.html")
text5 = get_text("https://www.pandora.com/privacy")
text6 = get_text("https://www.iubenda.com/privacy-policy/304647")

def tokenize(sentence):
    '''
        去除多余空白、分词、词性标注
    '''
    sentence = re.sub(r'\s+', ' ', sentence) #使用通配符消除重复的空白
    token_words = word_tokenize(sentence)
    token_words = pos_tag(token_words)
    return token_words


wordnet_lematizer = WordNetLemmatizer()
def stem(token_words):
    '''
        词形归一化
    '''
    words_lematizer = []
    for word, tag in token_words:
        if tag.startswith('NN'):
            word_lematizer =  wordnet_lematizer.lemmatize(word, pos='n')  # n代表名词
        elif tag.startswith('VB'):
            word_lematizer =  wordnet_lematizer.lemmatize(word, pos='v')   # v代表动词
        elif tag.startswith('JJ'):
            word_lematizer =  wordnet_lematizer.lemmatize(word, pos='a')   # a代表形容词
        elif tag.startswith('R'):
            word_lematizer =  wordnet_lematizer.lemmatize(word, pos='r')   # r代表代词
        else:
            word_lematizer =  wordnet_lematizer.lemmatize(word)
        words_lematizer.append(word_lematizer)
    return words_lematizer

def delete_invalid_word(token_words):
    valid_word = []
    for word in token_words:
        if len(wordnet.synsets(word)) > 0:
            valid_word.append(word)
    return valid_word

sr = stopwords.words('english')
sr.append("limited")
sr.append("additionnaly")
sr.append("e.g")
sr.remove("other")
sr.remove("than")
sr.remove("not")
sr.remove("you")
sr.remove("and")
sr2 = stopwords.words('english')
def delete_stopwords(token_words):
    '''
        去停用词
    '''
    cleaned_words = [word for word in token_words if word not in sr]
    return cleaned_words

def delete_stopwords2(token_words):
    '''
        去停用词
    '''
    cleaned_words = [word for word in token_words if word not in sr2]
    return cleaned_words

def delete_adjwords(token_words):
    '''
        去adj
    '''
    cleaned_words = [word for word in token_words if word not in sr]
    return cleaned_words


def is_number(s):
    '''
        判断字符串是否为数字
    '''
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
characters_title = [' ','.',',','|' , ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','...','^','{','}']
characters = [' ','|' , ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','...','^','{','}']
characters_proposal = [' ','|' , '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','...','^','{','}']
def delete_characters(token_words):
    '''
        去除特殊字符、数字
    '''
    words_list = [word for word in token_words if word not in characters]
    return words_list
def delete_characters_proposal(token_words):
    '''
        去除特殊字符、数字
    '''
    words_list = [word for word in token_words if word not in characters_proposal and not is_number(word)]
    return words_list

def delete_characters_title(token_words):
    '''
        去除特殊字符、数字
    '''
    words_list = [word for word in token_words if word not in characters and not is_number(word)]
    return words_list


def to_lower(token_words):
    '''
        统一为小写
    '''
    words_lists = [x.lower() for x in token_words]
    return words_lists

def pre_process_title(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    # token_words = delete_stopwords(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_invalid_word(token_words)

    token_words = delete_characters_title(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    return ' '.join(token_words)

def pre_process(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    token_words = delete_stopwords(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_characters(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    return ' '.join(token_words)

def pre_process_type(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    token_words = delete_stopwords2(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_characters(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    return ' '.join(token_words)


def pre_process_proposal(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    token_words = delete_stopwords(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_characters_proposal(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    return ' '.join(token_words)

def pre_process_list(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    token_words = delete_stopwords(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_characters(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    return token_words

def pre_process_stop(text):
    '''
        文本预处理
    '''
    token_words = tokenize(text)
    # print("分词标记词性：")
    # print(token_words)
    token_words = stem(token_words)
    # print("词性还原：")
    # print(token_words)
    # token_words = delete_stopwords(token_words)
    # print("去停用词：")
    # print(token_words)
    token_words = delete_characters(token_words)
    # print("删除字符：")
    # print(token_words)
    token_words = to_lower(token_words)
    # print("小写全部：")
    # print(token_words)
    text = ' '.join(token_words)
    final_text = text.split(".")
    return final_text
# print(pre_process(text1))
# text7 = "To communicate with you.including providing you with notifications on products and services that are updated or launched."
# print(pre_process_stop(text7))