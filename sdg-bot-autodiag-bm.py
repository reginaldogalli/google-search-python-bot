from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import concurrent.futures
service = Service()
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=service, options=options)
print('EXECUTANDO ROBÔ ATIVADOR DE AUTODIAGNÓSTICOS - BM')
navegador.get('http://192.168.3.128')
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

time.sleep(2)
navegador.get('http://192.168.3.128/menu/online/index.php?ied=BM')
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_length"]/label/select').send_keys('t')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').clear()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato_filter"]/label/input').send_keys('"desativado"')
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()

def alteracoes():
    navegador.find_element(By.CLASS_NAME, 'sorting_1').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="divToggle"]/div/div/label[2]').click()
    navegador.find_element(By.XPATH, '//*[@id="change"]').click()
    navegador.find_element(By.XPATH, '//*[@id="change"]').send_keys('\ue00c')

i = 0
while 1:
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(alteracoes)
            future.result(timeout=10)
        i = i + 1
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="tableAbstrato"]/thead/tr/th[2]').click()
        print('Alterações realizadas: ', i)
    except concurrent.futures.TimeoutError:
        print("O tempo limite foi excedido.")
        input('aperte uma tecla para fechar o programa...')
        break

print('Alterações concluídas')
input('aperte uma tecla para fechar o programa...')