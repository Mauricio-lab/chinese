import requests
from bs4 import BeautifulSoup
import time
import nltk
import nltk.sentiment.util
from nltk.corpus import stopwords



nltk.download('punkt')

# https:||www.chinadaily.com.cn|a|202304|26|WS6448decfa310b6054facfef4.html
#https://www.chinadaily.com.cn/a/202304/26/WS64487d85a310b6054facfcf5.html
#url=ticker.replace('|','/')
url='https://www.chinadaily.com.cn/a/202305/01/WS644fb676a310b6054fad0a6f.html'
print('____________________________________________')
print(url)
print('____________________________________________')
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
text_link=''
els = soup.find_all("p")
for el in els:
    text_link=text_link+el.text
nltk_riječi = nltk.sent_tokenize(text_link)

#print(nltk_riječi)
#input('OOOO')
b1=[]
#text_link=''
start_time = time.time()
for sentence in nltk_riječi:
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