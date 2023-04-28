
INPUT={}
n=0
fp_input=open('BAZA_JSON.txt','r', encoding='utf-8')
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
    INPUT[word_rijec]=json_rest

    #time.sleep(1)

fp_input.close()


INPUT_1=[]
field_1={}
fp = open("ENG_v1_sorted.txt",'r',encoding='utf-8')
for i in fp:
    linija=fp.readline()
    if linija=='XXX\n':
        break
    if '%' not in linija:
        linija=linija+'%[]\n'
    poz=linija.find('%')

    poz2=linija.find(']   ')
    hr_word=linija[poz2+4:].replace('\n','')


    ključ=linija[:poz].replace('\n','')
    if ključ not in field_1.keys():
        print(ključ)
        try:
            field_1[ključ]=INPUT[hr_word]+'  #  '+hr_word+'\n'
        except:
            pass
        INPUT_1.append(linija)
fp.close()
#print(field_1)

fp2 = open("ENG_v2_X_sorted.txt",'w',encoding='utf-8')
for i in field_1.keys():
    fp2.write(i+field_1[i])
fp2.close()