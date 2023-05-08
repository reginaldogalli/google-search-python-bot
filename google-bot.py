from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

contador = 0
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
while contador <= 30:
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/search?q=msa+ccb")
    driver.find_element(By.XPATH, '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a/span').click()
    #driver.find_element("xpath", '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a').click()
    #driver.find_element("xpath", '//*[@id="rso"]/div[8]/div/div/div[1]/div/a/div/div/span').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'https://msaccb.com.br').click()
    tempo = random.randint(5,20)
    time.sleep(tempo)
    driver.find_element(By.XPATH, '/html/body/main/section[2]/a').click()
    time.sleep(600)
    driver.close()
    contador = contador + 1