# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
options.add_argument("--headless=new")
print('EXECUTANDO ROBÔ DE CONFIGURAÇÃO SDG')
navegador = webdriver.Chrome(service=service, options=options)
print('Abrindo Navegador', navegador)
ip = 'http://192.168.3.128'
# %%
navegador.get(ip)
print('Acessando página web:', ip)
time.sleep(2)
# %%
print('Realizando login')
entrar = '//*[@id="buttonEntrar"]' 
campoUsuario = '//*[@id="inputUsuario"]'
campoSenha = '//*[@id="inputSenha"]'
entrarForm = '//*[@id="btn-submit"]'
menuHamburger = '//*[@id="divNavbar"]/nav/div/div[1]/button'
usuario = 'TTadmin'
senha = 'senh@Intern@'
try:
    navegador.find_element(By.XPATH, entrar).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, campoUsuario).send_keys(usuario)
    navegador.find_element(By.XPATH, campoSenha).send_keys(senha)
    navegador.find_element(By.XPATH, entrarForm).click()
except:
    navegador.find_element(By.XPATH, menuHamburger).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, entrar).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, campoUsuario).send_keys(usuario)
    navegador.find_element(By.XPATH, campoSenha).send_keys(senha)
    navegador.find_element(By.XPATH, entrarForm).click()
# %%
print('Acessando área de configuração')
time.sleep(2)
#ip = 'http://192.168.3.128'
editaApp = ip + '/menu/configuracao/'
clonar = '//*[@id="liClonar"]'
aceitaClonar = '//*[@id="modalBotaoSim"]'
editar = '//*[@id="liEditar"]'
aceitaEditar = '//*[@id="modalBotaoOk"]'
navegador.get(editaApp)
try:
    navegador.find_element(By.XPATH, clonar).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, aceitaClonar).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, editar).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, aceitaEditar).click()
except:
    print('Falha ao acessar a área de configuração. Verifique se as informações de login estão corretas')
    time.sleep(10)
    exit()
# %%
print('Acessando área de configurações da saída modbus')
time.sleep(1)
modbusSaida = ip + '/config/modbus/saida/'
campoIED = '/html/body/div[4]/div/div/form[1]/div/span/span[1]/span/span[1]'
idIED = '/html/body/span/span/span[2]/ul/li[4]'
navegador.get(modbusSaida)
time.sleep(2)
navegador.find_element(By.XPATH, campoIED).click()
time.sleep(2)
navegador.find_element(By.XPATH, idIED).click()

# %%
print('Desabilitando "desconsidera qualidade"')
time.sleep(1)
checked = 'glyphicon-check'
editar = '//*[@id="initial-state"]/button[2]'
checkbox = 'checkboxDesconsideraQualidade'
confirmar = '//*[@id="btn-update"]/span[2]'
proximo = '//*[@id="tableMbSlave_next"]/a'
j = 1
while 1:
    print('Página atual: ', j)
    i = 0
    while i < 10:
        try:
            navegador.find_element(By.CLASS_NAME, checked).click()
            time.sleep(1)
            navegador.find_element(By.XPATH, editar).click()
            time.sleep(2)
            navegador.find_element(By.ID, checkbox).click()
            time.sleep(1)
            navegador.find_element(By.XPATH, confirmar).click()
            time.sleep(3)
            i = i + 1
            print('Alterações realizadas: ', i)
        except:
            break
    try:
        navegador.find_element(By.XPATH, proximo).click()
        j = j + 1
        print('acessando a próxima página...')
    except:
        break
print('Alterações concluídas')
# %%
print('Saindo da tela de edição')
time.sleep(1)
linkAdmin = '//*[@id="aUsuario"]/span[2]'
menuHamburger = '/html/body/nav/div/div[1]/button'
sairEdicao = '//*[@id="li-exit-config"]/a'

try:
    navegador.find_element(By.XPATH, linkAdmin).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, sairEdicao).click()
except:
    navegador.find_element(By.XPATH, menuHamburger).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, linkAdmin).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, sairEdicao).click()
# %%
print('Aplicando configurações')
time.sleep(2)
aplicar = '//*[@id="liAplicar"]'
sim = '//*[@id="modalBotaoSim"]'

navegador.find_element(By.XPATH, aplicar).click()
time.sleep(2)
navegador.find_element(By.XPATH, sim).click()


