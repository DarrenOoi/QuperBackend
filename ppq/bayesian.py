import csv

from sklearn.naive_bayes import MultinomialNB

from 文本清洗 import pre_process_title
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import joblib
import nltk
nltk.download('omw-1.4')
from sklearn import metrics


def readtrain():
    with open('title.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile)
        column1 = [row for row in reader]
    content_train = [i[0] for i in column1[1:]] #第一列标记
    opinion_train = [i[1] for i in column1[1:]] #第二列为文本内容
    # print ('there has  %s sentences' % len(content_train))
    train = [content_train, opinion_train]
    return train

def segmentWord(cont):
    c = []
    for i in cont:
        clean_text = pre_process_title(i)
        c.append(clean_text)
    return c
train = readtrain()
content = segmentWord(train[1])
# print(content)
textMark = train[0]

train_content = content[:]
# test_content = content[450:508]
train_textMark = textMark[:]
# test_textMark = textMark[450:508]

tf = TfidfVectorizer(max_df=0.5)
# print(train_content)
train_features = tf.fit_transform(train_content)
# test_features = tf.transform(test_content)

clf = MultinomialNB(alpha=0.1)
clf.fit(train_features,train_textMark)
joblib.dump(clf, 'classifier.pkl')
joblib.dump(tf,'tf.pkl')
# print(predicted_labels)
# print(test_textMark)
# print("bayesian:",metrics.accuracy_score(test_textMark,predicted_labels))

