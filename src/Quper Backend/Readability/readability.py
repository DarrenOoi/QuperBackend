import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.sonority_sequencing import SyllableTokenizer
from bs4 import BeautifulSoup
import requests
nltk.download('punkt')


def calculate_ari(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_characters = sum(len(word) for word in words)
    num_words = len(words)
    num_sentences = len(sentences)

    ari = 4.71 * (num_characters / num_words) + 0.5 * \
        (num_words / num_sentences) - 21.43
    return ari


def calculate_fres(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_words = len(words)
    num_sentences = len(sentences)
    syllable_tokenizer = SyllableTokenizer()

    syllable_count = sum(len(syllable_tokenizer.tokenize(word))
                         for word in words)
    fres = 206.835 - 1.015 * (num_words / num_sentences) - \
        84.6 * (syllable_count / num_words)
    # fres = 206.835 - 1.015 * (num_words / num_sentences) - \
    #     84.6 * (sum(len(word) for word in words) / num_words)
    return fres


def calculate_lix(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_long_words = len([word for word in words if len(word) > 6])
    num_words = len(words)
    num_sentences = len(sentences)

    lix = (num_words / num_sentences) + (num_long_words * 100 / num_words)
    return lix


def calculate_metrics(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_words = len(words)
    num_sentences = len(sentences)
    num_characters = sum(len(word) for word in words)
    num_syllables = sum([syllable_count(word) for word in words])

    avg_syllables_per_word = num_syllables / num_words
    avg_words_per_sentence = num_words / num_sentences
    avg_letters_per_word = num_characters / num_words

    reading_time = num_words / 238
    speaking_time = num_words / 183

    return avg_syllables_per_word, avg_words_per_sentence, avg_letters_per_word, num_sentences, num_words, reading_time, speaking_time


def syllable_count(word):
    vowels = "aeiouAEIOU"
    count = 0
    in_word = False

    for char in word:
        if char in vowels:
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    if word.endswith("e"):
        count -= 1

    return count if count > 0 else 1


def calculate_readability(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx responses
    soup = BeautifulSoup(response.content, features="html.parser")
    # with open("./pp_example/69_Developer Privacy Policy.html", "r", encoding="utf-8") as file:
    #     html_content = file.read()

    # soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    soup.decompose()
    ari = calculate_ari(text)
    fres = calculate_fres(text)
    lix = calculate_lix(text)
    avg_syllables_per_word, avg_words_per_sentence, avg_letters_per_word, num_sentences, num_words, reading_time, speaking_time = calculate_metrics(
        text)

    metrics = {
        "ARI": round(ari, 2),
        "FRES": round(fres, 2),
        "LIX": round(lix, 2),
        "Average Syllables per Word": round(avg_syllables_per_word, 2),
        "Average Words per Sentence": round(avg_words_per_sentence, 2),
        "Average Letters per Word": round(avg_letters_per_word, 2),
        "Sentence Count": round(num_sentences, 2),
        "Word Count": round(num_words, 2),
        "Reading Time (minutes)": round(reading_time, 2),
        "Speaking Time (minutes)": round(speaking_time, 2)
    }

    return metrics


if __name__ == "__main__":
    print(calculate_readability("https://www.adobe.com/privacy/policy.html"))
