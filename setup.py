import requests
from bs4 import BeautifulSoup
import time
import nltk
import nltk.sentiment.util
from nltk.corpus import stopwords
import re


nltk.download('punkt')

# https:||www.chinadaily.com.cn|a|202304|26|WS6448decfa310b6054facfef4.html
#https://www.chinadaily.com.cn/a/202304/26/WS64487d85a310b6054facfcf5.html
#url=ticker.replace('|','/')
url='https://www.liberoquotidiano.it/news/spettacoli/35682988/madonna-di-trevignano-veggente-iene-maiale-verita-test-sangue.html'
print('____________________________________________')
print(url)
print('____________________________________________')
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
text_link=''
els = soup.find_all("p")
for el in els:
    text_link=text_link+el.text

text_link2=''
i=1
#if regex.search(r'\p{Han}', text_link):
#    i=1
if re.search("[\u4e00-\u9FFF]", text_link):
    #print('===============================0')
    i=2
#if i==1:
KIN2=[]
if i==2:
    
    for kineska_recenica in re.findall(u'[^!?。\.\!\?]+[!?。\.\!\?]?', text_link, flags=re.U):
        #print(kineska_recenica+'\n')
        KIN2.append(kineska_recenica)
        #print('------------')
        text_link2=text_link2+kineska_recenica+'\n'
    text_link=text_link2
    
if i==1:
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    KIN2=nltk.sent_tokenize(text_link)
    print('NIJE KINESKI')
    #print(text_link)
    pass 
#nltk_riječi = nltk.sent_tokenize(text_link)
print(KIN2)
#input('OOOO')
b1=[]
#text_link=''
start_time = time.time()
for sentence in KIN2:
    print(sentence)
    url='https://svijezici.onrender.com/process/'+sentence
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    text_link=''
    els = soup.find_all("p")
    for el in els:
        text_link=text_link+el.text
    #print(text_link)
    b1.append(text_link)

for t in b1:
    print('++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++')
    print(t)
    print('++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++')
print(' ')
print(' ')
process_speed='{"time[s]":'+'%s' % round((time.time() - start_time),4)+"}"
print(' ')
print(' ')
print(process_speed)