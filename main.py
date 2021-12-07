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
import os



def logging(title,code):
    flag = os.path.isdir("logDir")
    if flag == True:
        sys.path.append("../logDir")

        f = open("logDir/%s.txt"%title , "a",encoding='utf-8')
        f.write("  %s \n " % (code))
    else:
        os.mkdir("logDir")
        sys.path.append("../logDir")

        f = open("logDir/%s.txt"%title , "a",encoding='utf-8')
        f.write("%s   \n " % (code))


def getTitle():
    """
    globecom's get title
    :return:
    """
    name = 'GLOBECOM2020'
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



def getTitleNIPS2021():
    url = 'https://neurips.cc/Conferences/2021/Schedule?type=Poster'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)
    meta_list = []
    wait_time = 0.5
    max_try = 1000

    title_list = []
    total = 2337

    title_name = wd.find_elements_by_xpath("/html/body/div[5]/div/main/div[3]/div[6]/div/div[3]" )[0].text
    # title_name = wd.find_elements_by_class_name("maincardBody" )[8].text


    # print(title_name)
    # exit(0)


    for i in tqdm(range(5, total)):
        # title_name = wd.find_elements_by_xpath("/html/body/div[5]/div/main/div/div/div[3]/div[%i]/div/div[3]" % i)[0].text.split("\n")[1]
        title_name = wd.find_elements_by_xpath("/html/body/div[5]/div/main/div[3]/div[%i]/div/div[3]" % i)[0].text
        # title_name = wd.find_elements_by_class_name("maincardBody" )[0].text

        # print(title_name)


        # print(i)
        # title_name = title_name.split('.')[0]
        title_list.append(title_name)
    return title_list



def getTitleICML():
    name = 'ICML2021'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    url = 'https://icml.cc/Conferences/2021/AcceptedPapersInitial'
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)

    meta_list = []
    wait_time = 0.5
    max_try = 1000

    title_list = []
    total = 1186
    element_span = wd.find_elements_by_xpath("/html/body/div[2]/ul/li[3]/cite")
    path = '/html/body/div[5]/div/main/div/div/div[3]/div[1186]/div/div[3]'

    for i in tqdm(range(4, total)):
        # title_name = wd.find_elements_by_xpath("/html/body/div[5]/div/main/div/div/div[3]/div[%i]/div/div[3]" % i)[0].text.split("\n")[1]
        title_name = wd.find_elements_by_xpath("/html/body/div[5]/div/main/div/div/div[3]/div[%i]/div/div[3]" % i)[0].text
        # print(title_name)
        # print(i)
        # title_name = title_name.split('.')[0]
        title_list.append(title_name)
    return title_list




url1 = 'https://globecom2021.ieee-globecom.org/program/technical-symposium-program/symposia-tuesday-7-december'
url2 = 'https://globecom2021.ieee-globecom.org/program/technical-symposium-program/symposia-wednesday-8-december'
url3 = 'https://globecom2021.ieee-globecom.org/program/technical-symposium-program/symposia-thursday-9-december'
url4 = 'https://globecom2021.ieee-globecom.org/program/technical-symposium-program/symposia-friday-10-december'
url5 = 'https://globecom2021.ieee-globecom.org/program/technical-symposium-program/symposia-saturday-11-december'

def getTitleGlobeCom2021(url):
    name = 'GLOBECOM2021'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)
    element_span = wd.find_elements_by_class_name("papertitle ")
    title_list = []

    for i in tqdm(range(len(element_span))):
        title = element_span[i].text
        title_list.append(title)
    return title_list




def getTitleWWW2021():
    url = 'https://dblp.org/db/conf/www/www2021.html'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)
    title_list = []

    element_span = wd.find_elements_by_class_name("title")
    total = len(element_span)
    for i in tqdm(range(total)):
        title_name = wd.find_elements_by_class_name("title")[i].text
        # print(title_name)
        # exit()
        # title_name = wd.find_elements_by_xpath("/html/body/div[2]/ul/li[%i]/cite" % i)[0].text.split("\n")[1]
        title_name = title_name.split('.')[0]
        title_list.append(title_name)
    return title_list




def getTitleICC2021():
    url = 'https://dblp.org/db/conf/icc/icc2021.html'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(executable_path=r"D:\install_dir\code\webTest\chromedriver.exe",
                          chrome_options=chrome_options)
    wd.get(url)
    title_list =[]
    #
    # tmp =len( wd.find_elements_by_class_name("title"))
    # print(tmp )
    #
    # exit()
    total = 759
    for i in tqdm(range(total)):
        title_name = wd.find_elements_by_class_name("title")[i].text
        # print(title_name)
        # exit()
        # title_name = wd.find_elements_by_xpath("/html/body/div[2]/ul/li[%i]/cite" % i)[0].text.split("\n")[1]
        title_name = title_name.split('.')[0]
        title_list.append(title_name)
    return title_list
# title_list1 = getTitleGlobeCom2021(url1)
# title_list2 = getTitleGlobeCom2021(url2)
# title_list3 = getTitleGlobeCom2021(url3)
# title_list4 = getTitleGlobeCom2021(url4)
# title_list5 = getTitleGlobeCom2021(url5)
#
#
# title_list = title_list1+title_list2+title_list3+title_list4+title_list5
#

# title_list = getTitleNIPS2021()

title_list = getTitleWWW2021()
# title_list = getTitleICML()

# title_list = getTitle()




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
    logging('www2021',title)
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
ax.set_title('GLOBECOM 2020 Submission Top {} Keywords'.format(num_keyowrd))

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