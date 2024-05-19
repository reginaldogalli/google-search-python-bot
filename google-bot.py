from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import random
import time

contador = 0
options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
options.add_argument("--headless=new")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
while contador <= 50:
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?q=lightcodeapps")
    print('driver.get("https://www.google.com/search?q=lightcodeapps")')
    time.sleep(2)
    #driver.find_element(By.XPATH, '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a/span').click()
    #print('driver.find_element(By.XPATH, //*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a/span).click()')
    #time.sleep(2)
    #driver.find_element("xpath", '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[3]/a').click()
    #driver.find_element("xpath", '//*[@id="rso"]/div[8]/div/div/div[1]/div/a/div/div/span').click()
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Lightcode Apps').click()
        print('driver.find_element(By.PARTIAL_LINK_TEXT, https://msaccb.com.br).click()')
        tempo = random.randint(5,20)
        time.sleep(tempo)
        driver.find_element(By.XPATH, '/html/body/header/nav/div/ul/div/li[2]/a').click()
        print('driver.find_element(By.XPATH, /html/body/main/section[2]/a).click()')
        time.sleep(5)
        iframe = driver.find_element(By.XPATH, "/html/body/main/section[5]")
        ActionChains(driver)\
            .scroll_to_element(iframe)\
            .perform()

        time.sleep(180)
    finally:
        driver.close()
        contador = contador + 1
        print(contador)