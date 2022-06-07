from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pandas as pd
import threading



data = pd.DataFrame(columns=['title','environment','social','governance','rating'])
data.to_csv('data.csv',index=False)

companies_list = [] 
companies_set = set()
url = 'https://www.refinitiv.com/en/sustainable-finance/esg-scores'


driver = webdriver.Firefox(executable_path = 'geckodriver')
driver.get(url)
    
def crawl(name):
    element = driver.find_element(by=By.CLASS_NAME, value="SearchInput-input")
    element.clear()
    element.send_keys(name)
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="accept-recommended-container"]')))
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="vendors-list-text"]')))
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'onetrust-pc-dark-filter ot-fade-in')))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="esg-data-body"]/div[1]/div/div/div[1]/div/button[2]'))).click()
    time.sleep(2) 
    
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/h3'))).text
    environment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div[2]/b'))).text
    social = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[5]/div[2]/b'))).text
    governance = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[10]/div[2]/b'))).text
    rating = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="esg-data-body"]/div[2]/div/div/div/div/div/div[2]/div[3]/h4'))).text
    
    data = pd.DataFrame({
        'title':[title],
        'environment':[environment],
        'social':[social],
        'governance':[governance],
        'rating':[rating]
    })
    data.to_csv('data.csv',mode='a',index=False, header=False)
    
    
   
def get_name(alpha):
    driver = webdriver.Firefox(executable_path = 'geckodriver')
    driver.get("https://www.refinitiv.com/en/sustainable-finance/esg-scores")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "SearchInput-input")))
    for i in alpha:
        element.clear()    
        element.send_keys(i)
        found = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "SearchInputTypeaheadItem-button")))
        for i in found:
            i = i.text
            companies_set.add(i)
    print(companies_set)
    driver.close()
    


alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_list = []
for i in alpha:
    list1 = []
    for j in alpha:
        list1.append(i+j)
    alpha_list.append(list1)

   
for i in range(0,4):
    while len(companies_set) < 102:
        thread1 = threading.Thread(target=get_name(alpha_list[i]))
        thread2 = threading.Thread(target=get_name(alpha_list[i+4]))
        thread3 = threading.Thread(target=get_name(alpha_list[i+8]))
        thread4 = threading.Thread(target=get_name(alpha_list[i+12]))
        thread5 = threading.Thread(target=get_name(alpha_list[i+16]))
        thread6 = threading.Thread(target=get_name(alpha_list[i+20]))
        if i < 3:
            thread7 = threading.Thread(target=get_name(alpha_list[i+24])) 
            thread7.start()
            
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
    

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()    



for j in companies_set:
    crawl(j)
    time.sleep(2)


driver.close()
    
    





