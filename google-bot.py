from selenium import webdriver
import random
import time

contador = 0

while contador <= 30:

    navegador = webdriver.Chrome()
    navegador.get("https://www.google.com/search?q=msa+ccb")
    navegador.find_element("xpath", '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a').click()
    navegador.find_element("xpath", '//*[@id="rso"]/div[7]/div/div/div[1]/div/a/h3').click()
    tempo = random.randint(5,20)
    time.sleep(tempo)
    navegador.find_element("xpath", '/html/body/main/section[2]/a').click()
    time.sleep(600)
    navegador.close()
    contador = contador + 1