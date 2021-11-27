# -*- coding:utf-8 -*-
import selenium
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getTitle():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    url = 'https://dblp.org/db/conf/globecom/globecom2020.html'
    url1 = 'https://nips.cc/Conferences/2020/AcceptedPapersInitia'
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)

    meta_list = []
    wait_time = 0.5
    max_try = 1000

    title_list = []
    total = 915
    # path = "/html/body/div[2]/ul/li[%i]/cite" %i
    element_span = wd.find_elements_by_xpath("/html/body/div[2]/ul/li[3]/cite")
    # element_span = wd.find_elements_by_css_selector("#conf\/globecom\/GuLHT20 > cite > span.title")

    # element_span = wd.find_elements_by_tag_name("cite")
    # element_span = wd.find_element(By.TAG_NAME,"li")
    # element_title = element_span.find_elements(By.CLASS_NAME,'title')

    # wd.fin
    # print(element_span[0].text.split("\n")[1])
    # print(titles[1])
    #

    for i in tqdm(range(2, total)):
        title_name = wd.find_elements_by_xpath("/html/body/div[2]/ul/li[%i]/cite" % i)[0].text.split("\n")[1]
        title_name = title_name.split('.')[0]
        title_list.append(title_name)
    return title_list


title_list = getTitle()


import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

print(stopwords.words('english'))

stopwords_deep_learning = ['learning', 'network', 'neural', 'networks', 'deep', 'via', 'using', 'convolutional',
                           'single']

keyword_list = []

for i, title in enumerate(title_list):

    print(i, "th paper's title : ", title)

    word_list = title.split(" ")
    word_list = list(set(word_list))

    word_list_cleaned = []
    for word in word_list:
        word = word.lower()
        if word not in stopwords.words('english') and word not in stopwords_deep_learning:  # remove stopwords
            word_list_cleaned.append(word)

    for k in range(len(word_list_cleaned)):
        keyword_list.append(word_list_cleaned[k])

# exit(0)

keyword_counter = Counter(keyword_list)
print(keyword_counter)

print('{} different keywords before merging'.format(len(keyword_counter)))

# Merge duplicates: CNNs and CNN
duplicates = []
for k in keyword_counter:
    if k + 's' in keyword_counter:
        duplicates.append(k)
for k in duplicates:
    keyword_counter[k] += keyword_counter[k + 's']
    del keyword_counter[k + 's']
print('{} different keywords after merging'.format(len(keyword_counter)))
print(keyword_counter)

print("")


# Show N most common keywords and their frequencies
num_keyowrd = 75 #FIXME
keywords_counter_vis = keyword_counter.most_common(num_keyowrd)

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(8, 18))

key = [k[0] for k in keywords_counter_vis]
value = [k[1] for k in keywords_counter_vis]
y_pos = np.arange(len(key))
ax.barh(y_pos, value, align='center', color='green', ecolor='black', log=True)
ax.set_yticks(y_pos)
ax.set_yticklabels(key, rotation=0, fontsize=10)
ax.invert_yaxis()
for i, v in enumerate(value):
    ax.text(v + 3, i + .25, str(v), color='black', fontsize=10)
ax.set_xlabel('Frequency')
ax.set_title('NeurIPS 2020 Submission Top {} Keywords'.format(num_keyowrd))

plt.show()


# Show the word cloud forming by keywords
from wordcloud import WordCloud
wordcloud = WordCloud(max_font_size=64, max_words=160,
                      width=1280, height=640,
                      background_color="black").generate(' '.join(keyword_list))
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()