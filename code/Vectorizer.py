from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def Vectorizing(text):
    # text - ������ ��������� ������, �������� �������� ������������ ������ � ���������������� ������� ������
    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(text)
    fn = vectorizer.get_feature_names()

    #for col in tfidf.nonzero()[1]:
        #print(fn[col], " ", tfidf[0, col])
    # tfidf - ������� ���� ���� � �� ����
    return tfidf, fn
