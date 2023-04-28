#import json
import selenium
import time
import nltk
import nltk.sentiment.util
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import googletrans
from googletrans import Translator

translator = Translator()
#pip install --target=/usr/local/lib/python3.9/dist-package selenium

def prevedi(text_sentence):
    prijevod=translator.translate(text_sentence, src='hr', dest='en')
    return str(prijevod.text)

INPUT={}
n=0
fp2 = open("__ENG_new.txt",'a',encoding='utf-8')
fp_input=open('BAZA_JSON2.txt','r', encoding='utf-8')
while n < 700000:
    n+=1
    linija=fp_input.readline()
    linija=linija.replace('\n','')
    word_rijec=linija[:linija.find('{')]
    json_rest=linija[linija.find('{'):]
    #print(word_rijec)
    #print(json_rest)
    if 'XXX' in linija:
        break
    time.sleep(0.5)
    try:
        prijevod=prevedi(word_rijec)  
    except:
        prijevod='HR-'+word_rijec
    INPUT[prijevod]=json_rest+ '#' + word_rijec
    print(prijevod + INPUT[prijevod])   
    fp2.write(prijevod+INPUT[prijevod]+'\n')
    #time.sleep(1)

fp_input.close()
fp2.close()




exit()
jezici=googletrans.LANGUAGES
#probaj
HR={}
LOCAL_LIST=[]

nltk.download('stopwords')

stop = set(stopwords.words("english"))
def extract_words_from_text(text):
    tokens = nltk.word_tokenize(text)
    tokens_neg_marked = nltk.sentiment.util.mark_negation(tokens)
    print(len(tokens))
    print(tokens_neg_marked)
    print(len(tokens_neg_marked))
    return [t for t in tokens_neg_marked
             if t.replace("_NEG", "").isalnum() and
             t.replace("_NEG", "") not in stop]
i=0
while i<10:
    print('---------------------------------')
    print('---------------------------------')
    uuu=input(':')
    print(len(uuu))
    print(extract_words_from_text(uuu))
    i=i+1

