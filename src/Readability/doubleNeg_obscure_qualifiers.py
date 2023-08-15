import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import re


def count_double_negatives(text):
    sentences = sent_tokenize(text)
    double_negatives_count = 0

    for sentence in sentences:
        if has_double_negatives(sentence):
            double_negatives_count += 1

    return double_negatives_count


def has_double_negatives(sentence):
    # Match double negatives pattern
    pattern = r"\b(?:not|n't|never|no)\s+\b(?:\w+\s+)?(?:not|n't|never|no)\b"
    return re.search(pattern, sentence, re.I) is not None


def count_obscure_language_qualifiers(text):
    sentences = sent_tokenize(text)
    obscure_qualifiers_count = 0
    obscure_words = ["possibly", "perhaps", "maybe", "might", "could", "potentially","may"]

    for sentence in sentences:
        if has_obscure_qualifiers(sentence, obscure_words):
            obscure_qualifiers_count += 1

    return obscure_qualifiers_count


def has_obscure_qualifiers(sentence, obscure_words):
    words = nltk.word_tokenize(sentence.lower())
    return any(word in obscure_words for word in words)


if __name__ == "__main__":
    with open("pp_example/69_Developer Privacy Policy.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()

    double_negatives_count = count_double_negatives(text)
    obscure_qualifiers_count = count_obscure_language_qualifiers(text)

    print("Double Negatives Count:", double_negatives_count)
    print("Obscure Language Qualifiers Count:", obscure_qualifiers_count)