from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

contador = 3
driver = webdriver.Chrome()
driver.get("http://192.168.3.182:5001/#/instalacao/2d6b657f-2ee3-4221-b1f4-17760d399f17/supervisao/a288703c-5c3b-42e4-bbf9-b544c3269c27/sensor/C03162B0-3DD2-4B47-A046-54AA412E014C")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("eg.engenharia")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/input').send_keys("Teste.engenharia1")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[4]/button').click()
time.sleep(5)
while contador <= 3:
    i = 0
    while i <= 29:   
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/nav/div/div/ul/li[1]/div/div/a/span').send_keys(Keys.TAB)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/nav/div/div/ul/li[1]/div/div/a/span').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/span/div/div[1]/div/ul/li[5]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/footer/div[1]/div[2]/button').click()
    time.sleep(4)
    #driver.find_element(By.XPATH, '//*[@id="signin"]').click()
    #time.sleep(1)
    #driver.find_element("xpath", '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a').click()
    #driver.find_element("xpath", '//*[@id="rso"]/div[8]/div/div/div[1]/div/a/div/div/span').click()
    driver.close()