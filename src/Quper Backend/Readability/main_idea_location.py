import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy


def calculate_ic(sentence, nlp):
    doc = nlp(sentence)
    nsubj_indices = [token.i for token in doc if token.dep_ == "nsubj"]
    root_index = [token.i for token in doc if token.dep_ == "ROOT"][0]

    if not nsubj_indices:
        return None

    ic = sum(nsubj_indices) / len(nsubj_indices) + root_index
    return ic


def is_center_preposed(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    if len(doc) < 5:
        return False
    elif 5 <= len(doc) < 20:
        ic_threshold = len(doc) / 2
    elif 20 <= len(doc) < 27:
        ic_threshold = len(doc) / 3
    else:
        ic_threshold = len(doc) / 4

    ic = calculate_ic(sentence, nlp)

    if ic is not None and ic > ic_threshold:
        return True
    else:
        return False


if __name__ == "__main__":
    with open("./pp_example/69_Developer Privacy Policy.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    sentences = sent_tokenize(text)

    true_count = 0
    for sentence in sentences:
        if is_center_preposed(sentence):
            true_count += 1

    print("Number of Sentences with Center Preposing:", true_count)