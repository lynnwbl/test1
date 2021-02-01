from bs4 import BeautifulSoup
from bs4 import element
import requests
import re
bl_chars = ["\n", "\"", "'", "\t"]
def fetch_article(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    all_content = BeautifulSoup(r.content, features="lxml")
    keywords = ""
    p_tags = all_content.find_all('p')
    for p in p_tags:
        ret = extract_content(p.contents)
        if ret is not None:
            keywords += ret + " "

    keywords = re.sub(' +', ' ', keywords)
    print(keywords)

def extract_content(content):
    if isinstance(content, str):
        return parse_string(content)
    elif isinstance(content, element.Tag):
        # Tag class
        extract_content(content.contents)
    elif isinstance(content, list):
        if len(content) == 1:
            return extract_content(content[0])
        ret = ""
        for item in content:
            con = extract_content(item)
            if con is not None:
                ret += con + " "
        return ret
    else:
        raise ValueError("not a valid type")


def parse_string(s):
    for c in bl_chars:
        s = s.replace(c, "")
    return s
# if __name__ == "__main__":
#     url = "https://www.businessinsider.com/video-games-2020-xbox-playstation-nintendo-2020-1"
#     fetch_article(url)

urls=['https://www.stuff.tv/features/most-anticipated-games',
     'https://www.esquire.com/lifestyle/a30284795/best-video-games-2020/',
     'https://www.denofgeek.com/games/best-video-games-2020/',
     'https://www.goodhousekeeping.com/life/entertainment/g30910862/best-video-games/',
     'https://www.wired.com/story/most-anticipated-videogames-2020/',
     'https://www.pcgamer.com/best-pc-games/']
for i in urls:
    fetch_article(i)
# import pandas as pd
# import numpy as np
# import nltk
# import os
# import matplotlib
# import nltk.corpus
# nltk.download('punkt')
# nltk.download('wordnet')
# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist
# from nltk.stem import PorterStemmer
#
# # lemmatizer = WordNetLemmatizer()
# # print('rocks:', lemmatizer.lemmatize('rocks'))
# # print('corpora:', lemmatizer.lemmatize('corpora'))
# # # f = open("testfile1.txt", "r")
# list_a=[]
# list_signs = [',', ':', '|', '.', ')', '(', ';', '’', '!', '-', "'s", '—', '"', '?', "'", "''", '``', '/']
# from itertools import islice
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# with open("testfile1.txt", encoding="utf-8") as lines:
#     for line in islice(lines, 0, 500, 1):
#         txt = line.strip()
#         tokens = word_tokenize(txt.lower())
#         if tokens != []:
#             for token in tokens:
#                 if token not in list_signs:
#                     list_a.append(token)
#                     # print(token)
#              # fdist = FreqDist(pst1)
#              # fdist1 = fdist.most_common(10)
# #
#              # print(fdist1)
# # #         list_a.append(txt)
#
# # fdist = FreqDist(list_a)
# # # print(fdist.most_common(50))
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# a = set(stopwords.words('english'))
# stopwords = [x for x in list_a if x not in a]
# # print(stopwords[0:100])
# # list_b=[]
# # for i in stopwords:
# #     list_b.append(lemmatizer.lemmatize(i))
# # print(list_b)
#
# # words_df = pd.DataFrame({'word': list(fdist.keys()), 'count': list(fdist.values())})
#
# # import matplotlib.pyplot as plt
# # fig = plt.figure()
# # ax = fig.add_axes([0,0,1,1])
# # ax.bar(words_df.word,words_df.count)
# # plt.show()
#
# # freq_words(df['reviewText'])
# list_b=[]
# for i in list_a:
#     if i in stopwords and not i.isnumeric():
#         list_b.append(lemmatizer.lemmatize(i))
# print(list_b)
# # print('/' in list_b)  #to test whether a sign is in final list
# fdist = FreqDist(list_b)
# print(fdist.most_common(50))
#


# print(len(list_))
# # #
#
# pst = PorterStemmer()
# # pst.stem('waiting')



# token = word_tokenize(txt)
#print(list_a)
# # print(f.readline())
# for x in f:
#   token = word_tokenize(x)
#   fdist = FreqDist(token)
#   fdist1 = fdist.most_common(10)
#   if token != []:
#       print(token)
#       print(fdist1)


  # pst = PorterStemmer()
  # pst.stem('waiting')
#
# # sample text for performing tokenization
# text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America"
# # importing word_tokenize from nltk

# # Passing the string text into word tokenize for breaking the sentences
# token = word_tokenize(text)
# print(token)
#
# # # finding the frequency distinct in the tokens
# # # Importing FreqDist library from nltk and passing token into FreqDist
#
# fdist = FreqDist(token)
# fdist
# #
# #
# # # To find the frequency of top 10 words
# fdist1 = fdist.most_common(10)
# print(fdist1)
# #
# #
# # # Importing Porterstemmer from nltk library
# # # Checking for the word ‘giving’
# from nltk.stem import PorterStemmer
# pst = PorterStemmer()
# pst.stem('waiting')
# #
# #
# #
# # # Importing LancasterStemmer from nltk
# # from nltk.stem import LancasterStemmer
# # lst = LancasterStemmer()
# # stm = ['giving', 'given', 'given', 'gave']
# # for word in stm :
# #  print(word+ ':' +lst.stem(word))
# #
# #
# #
# #  # Importing Lemmatizer library from nltk
# #  from nltk.stem import WordNetLemmatizer
# #
# #  lemmatizer = WordNetLemmatizer()
# #
# #  print('rocks:', lemmatizer.lemmatize('rocks'))
# #  print('corpora:', lemmatizer.lemmatize('corpora'))
# #
# #
# #
# # # Checking for the list of words
# # stm = ['waited', 'waiting', 'waits']
# # for word in stm:
# #    print(word + ':' + pst.stem(word))