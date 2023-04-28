from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://translate.google.hr/?hl=hr&tab=wT1#view=home&op=translate&sl=hr&tl=zh-CN&text=p")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()
#time.sleep(1)
actionChains = ActionChains(driver)
for i in range(10):
    start_time = time.time()
    #actionChains = ActionChains(driver)
    elem = driver.find_element("xpath","/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
    actionChains.double_click(elem).perform()
    elem.send_keys(Keys.CONTROL, 'a')
    elem.send_keys(Keys.BACKSPACE)
    INPUT=input(':')
    elem.send_keys(INPUT)
    time.sleep(1)
    try:
        elem = driver.find_element("xpath","/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]")
        time.sleep(1)
        PRIJEVOD=elem.text
        print(PRIJEVOD)
    except:
        print('Nista')
        pass
    print("--- %s seconds ---" % (time.time() - start_time))
      
