# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=service, options=options)

# %%
navegador.get('http://192.168.3.128')

# %%
time.sleep(2)
try:
    navegador.find_element(By.XPATH,'//*[@id="buttonEntrar"]').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="inputUsuario"]').send_keys('TTadmin')
    navegador.find_element(By.XPATH, '//*[@id="inputSenha"]').send_keys('senh@Intern@')
    navegador.find_element(By.XPATH, '//*[@id="btn-submit"]').click()
except:
    navegador.find_element(By.XPATH, '//*[@id="divNavbar"]/nav/div/div[1]/button').click()
    time.sleep(2)
    navegador.find_element(By.XPATH,'//*[@id="buttonEntrar"]').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="inputUsuario"]').send_keys('TTadmin')
    navegador.find_element(By.XPATH, '//*[@id="inputSenha"]').send_keys('senh@Intern@')
    navegador.find_element(By.XPATH, '//*[@id="btn-submit"]').click()

# %%
time.sleep(2)
navegador.get('http://192.168.3.128/menu/online/index.php?ied=BM')
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_length"]/label/select').send_keys('t')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').send_keys('"desativado"')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()


# %%
i = 201
while i > 0:
    try:
        navegador.find_element(By.CLASS_NAME, 'sorting_1').click()
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="divToggle"]/div/div/label[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').send_keys('\ue00c')
        i = i - 1
        time.sleep(2)
        print('Alterações restantes', i)
    finally:
        continue

# %%
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').send_keys('"não acionado"')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()

# %%
i = 93
while i > 0:
    try:
        navegador.find_element(By.CLASS_NAME, 'sorting_1').click()
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="divToggle"]/div/div/label[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').send_keys('\ue00c')
        i = i - 1
        time.sleep(2)
        print('Alterações restantes', i)
    finally:
        continue

# %%
time.sleep(2)
navegador.get('http://192.168.3.128/menu/online/index.php?ied=TM')
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_length"]/label/select').send_keys('t')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').send_keys('"desativado"')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()

# %%
i = 50
while i > 0:
    try:
        navegador.find_element(By.CLASS_NAME, 'sorting_1').click()
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="divToggle"]/div/div/label[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').send_keys('\ue00c')
        i = i - 1
        time.sleep(2)
        print('Alterações restantes', i)
    finally:
        continue

# %%
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').send_keys('"aberto"')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()

# %%
i = 16
while i > 0:
    try:
        navegador.find_element(By.CLASS_NAME, 'sorting_1').click()
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="divToggle"]/div/div/label[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').click()
        navegador.find_element(By.XPATH, '//*[@id="change"]').send_keys('\ue00c')
        i = i - 1
        time.sleep(2)
        print('Alterações restantes: ', i)
    finally:
        continue


