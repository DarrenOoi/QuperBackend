import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
nltk.download('punkt')

def calculate_ari(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_characters = sum(len(word) for word in words)
    num_words = len(words)
    num_sentences = len(sentences)

    ari = 4.71 * (num_characters / num_words) + 0.5 * (num_words / num_sentences) - 21.43
    return ari


def calculate_fres(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    num_words = len(words)
    num_sentences = len(sentences)

    fres = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (sum(len(word) for word in words) / num_words)
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

    reading_time = num_words / 200  # Assuming average reading speed of 200 words per minute
    speaking_time = num_words / 150  # Assuming average speaking speed of 150 words per minute

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


if __name__ == "__main__":
    with open("./pp_example/69_Developer Privacy Policy.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()

    ari = calculate_ari(text)
    fres = calculate_fres(text)
    lix = calculate_lix(text)
    avg_syllables_per_word, avg_words_per_sentence, avg_letters_per_word, num_sentences, num_words, reading_time, speaking_time = calculate_metrics(
        text)

    print("ARI:", ari)
    print("FRES:", fres)
    print("LIX:", lix)
    print("Average Syllables per Word:", avg_syllables_per_word)
    print("Average Words per Sentence:", avg_words_per_sentence)
    print("Average Letters per Word:", avg_letters_per_word)
    print("Sentence Count:", num_sentences)
    print("Word Count:", num_words)
    print("Reading Time (minutes):", reading_time)
    print("Speaking Time (minutes):", speaking_time)