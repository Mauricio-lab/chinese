#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from bs4 import BeautifulSoup
import requests
#language_code = "te"
options = Options()
options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get('https://translate.google.com/?sl=en&tl=hr&text=car%0A&op=translate')

fp=open('__2.txt','w', encoding='utf-8')
try:
    driver.get(f"https://translate.google.com/?sl=en&tl=hr&text=car%20is%20red%20and%20nobody%20knows%20how%20to%20drive.%0A&op=translate")
    soup=BeautifulSoup(driver.page_source, "html.parser")
    #print(str(driver.page_source))
    tt=soup.find_all('div')
    for i in tt:
        fp.write(str(i))
        print(i.text)
    #time.sleep(2)
except Exception:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Something went wrong at: ", current_time)   

exit()
fp.close()



#wait = WebDriverWait(driver, 5)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tw-source-text-ta')))
#time.sleep(1)
#rrr=driver.find_element(By.CLASS_NAME, "ryNqvb"
#rrr=driver.find_element_by (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/")
#ttt=driver.find_element(By.ID,"source")
#time.sleep(3)
#ActionChains(driver).move_to_element(ttt).send_keys('car').perform()
time.sleep(10)
output = driver.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]").text
print(output)
driver.quit()
exit()
ActionChains(driver).move_to_element(ttt).send_keys('MAURICIO').perform()
time.sleep(0.3)
print(ttt.text)
#rrr.send_keys('mauricio')
#time.sleep(1)
#rrr=driver.find_element("xpath", '//*[@id="tw-target-text"]/span')


#//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span













exit()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--no-sandbox')
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=options)
#driver.get('https://www.google.com/search?q=google+translate&rlz=1C1CAFC_enHR893HR893&oq=google+tra&aqs=chrome.0.69i59i131i433i512j69i57j69i59l2j0i67i650j69i60l3.2296j0j4&sourceid=chrome&ie=UTF-8')
driver.get('https://translate.google.com/?sl=en&tl=hr&text=car&op=translate')
#                                       /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea
#/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/g-expandable-container/div/div/div[3]/div[1]/div[1]/div[1]/textarea
#//*[@id="tw-source-text-ta"] 
time.sleep(10)

#search1 = driver.find_element('xpath','/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]')
#result1 = driver.find_element('xpath',".//span[@id='result_box']/span")
#search1.send_keys('building')
#search1.send_keys(Keys.ENTER)
#time.sleep(1)

output1 = driver.find_element(By.CLASS_NAME,'HwtZe').text
#print(result1.text)
print(output1.text)
exit()
try:
    search2 = driver.find_element(by=By.XPATH,value='/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/g-expandable-container/div/div/div[3]/div[3]/div/div[2]/div[1]/pre/span')
    print(search2.text)
except:
    pass


#search1 = driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')

#//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span
#try:
#    search2 = driver.find_element('xpath',"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span")
#    print(search2.text)
#except:
#    pass
#search3 = driver.find_element('xpath',"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[1]/div/div/span/button/div[3]")
#search3.click()
#time.sleep(0.2)


#driver.close()