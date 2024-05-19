# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
#options.add_argument("--headless=new")
print('\nATIVADOR DE ALARMES SDG/SD+')
navegador = webdriver.Chrome(service=service, options=options)
print('\nAbrindo navegador')
ip = input('Digite o IP do SDG/SD+: ')
url = 'http://' + ip
# %%
navegador.get(url)
print('\nAcessando página web:', url)
time.sleep(2)
# %%
print('\nRealizando login')
entrar = '//*[@id="buttonEntrar"]' 
campoUsuario = '//*[@id="inputUsuario"]'
campoSenha = '//*[@id="inputSenha"]'
entrarForm = '//*[@id="btn-submit"]'
menuHamburger = '//*[@id="divNavbar"]/nav/div/div[1]/button'
usuario = input('Digite o usuário: ')
if usuario == '':
    usuario = 'TTadmin'
senha = input('Digite a senha: ')
if senha == '':
    senha = 'senh@Intern@'
incorreto = '//*[@id="error-alert"]/div/div/span[1]'

try:
    navegador.find_element(By.XPATH, entrar).click()
except:
    navegador.find_element(By.XPATH, menuHamburger).click()
    time.sleep(2)
    navegador.find_element(By.XPATH, entrar).click()
while 1:
    time.sleep(2)
    navegador.find_element(By.XPATH, campoUsuario).clear()
    navegador.find_element(By.XPATH, campoUsuario).send_keys(usuario)
    navegador.find_element(By.XPATH, campoSenha).clear()
    navegador.find_element(By.XPATH, campoSenha).send_keys(senha)
    navegador.find_element(By.XPATH, entrarForm).click()
    time.sleep(2)
    try:
        navegador.find_element(By.XPATH, incorreto).click()
        print('\nDados incorretos. Tente novamente')
        usuario = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
    except:
        break
print('\nLogin realizado')
# %%
trocaIED = '1'
time.sleep(2)
while trocaIED == '1':
    campoPesquisa = '//*[@id="tableAbstrato_filter"]/label/input'
    ordenaValores = '//*[@id="tableAbstrato"]/thead/tr/th[5]'
    trocaFiltro = '1'
    alerta = ""
    ied = input('Digite o nome do IED (Utilize maiscúlas e minúsculas conforme o nome do IED): ')
    iedOnline = url + '/menu/online/index.php?ied=' + ied
    navegador.get(iedOnline)
    time.sleep(2)
    try:
        alerta = navegador.find_element(By.TAG_NAME, 'body').text
    except:
        time.sleep(2)
        if alerta == '':
            print('\nIED não encontrado')
            continue
    print('\nIED encontrado: ' + iedOnline)
    while trocaFiltro == '1':
        filtroALBM = ''
        time.sleep(2)
        filtroALBM = input ('Digite o filtro a ser utilizado \n(Exemplo - para BM: "não acionado", "desativado", para TM: "aberto", "desativado"): ')
        time.sleep(2)
        navegador.find_element(By.XPATH, campoPesquisa).clear()
        navegador.find_element(By.XPATH,campoPesquisa).send_keys(filtroALBM)
        time.sleep(3)
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.XPATH, ordenaValores).click()
        print('\nAplicado filtro: ', filtroALBM)
        # %%
        elementoLista = 'sorting_1'
        toggle = '//*[@id="divToggle"]/div/div/label[2]'
        alterar = '//*[@id="change"]'
        escape ='\ue00c'
        i = 0
        while 1:
            try:
                navegador.find_element(By.CLASS_NAME, elementoLista).click()
                time.sleep(2)
                navegador.find_element(By.XPATH, toggle).click()
                navegador.find_element(By.XPATH, alterar).click()
                navegador.find_element(By.XPATH, alterar).send_keys(escape)
                time.sleep(0.5)
                navegador.find_element(By.XPATH, ordenaValores).click()
                i = i + 1
                print('\nAlterações realizadas: ', i)
            except:
                print('\nNão há variáveis encontradas com o filtro atual: ', filtroALBM)
                time.sleep(2)
                break
        print('\nAlterações concluídas')
        time.sleep(1)
        trocaFiltro = input('Deseja aplicar outro filtro? \n [1]-SIM \n [2]-NÃO\n:')
        if trocaFiltro == '1':
            continue
        else:
            break
    if ied == 'bm' or 'BM':
        #%%
        print('\nFinalizando ativação de alarmes do BM. Aguarde...')
        time.sleep(1)
        filtroCalc = "calculando"
        navegador.find_element(By.XPATH, campoPesquisa).clear()
        navegador.find_element(By.XPATH, campoPesquisa).send_keys(filtroCalc)
        print('\nAplicado filtro: ', filtroCalc)
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.XPATH, ordenaValores).click()
        i = 2
        while i > 0:
            try: 
                navegador.find_element(By.CLASS_NAME, elementoLista).click()
                time.sleep(2)
                navegador.find_element(By.XPATH, toggle).click()
                navegador.find_element(By.XPATH, alterar).click()
                navegador.find_element(By.XPATH, alterar).send_keys(escape)
                i = i - 1
                time.sleep(2)
                print('\nAlterações restantes: ', i)
            except:
                print('\nNão há variáveis encontradas com o filtro atual: ', filtroCalc)
                break
        print('\nEtapa concluída. Alterando filtro atual...')
        print('\nFinalizando ativação de alarmes do BM. Aguarde...')
        #%%
        time.sleep(1)
        filtroOver = '"Indicação de autodiagnóstico de overflow de tangente delta - Conjunto 2 - Fase"'
        campoValor = '//*[@id="inputValue"]'
        navegador.find_element(By.XPATH, campoPesquisa).clear()
        navegador.find_element(By.XPATH, campoPesquisa).send_keys(filtroOver)
        print('\nAplicado filtro: ', filtroOver)
        time.sleep(3)
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.XPATH, ordenaValores).click()
        i = 3
        while i > 0:
            try:
                navegador.find_element(By.CLASS_NAME, elementoLista).click()
                time.sleep(1)
                navegador.find_element(By.XPATH, campoValor).clear()
                navegador.find_element(By.XPATH, campoValor).send_keys('1')
                navegador.find_element(By.XPATH, alterar).click()
                navegador.find_element(By.XPATH, alterar).send_keys(escape)
                i = i - 1
                time.sleep(2)
                print('\nAlterações restantes: ', i)
            finally:
                continue
        print('\nEtapa concluída. Alterando filtro atual...')
        print('\nFinalizando ativação de alarmes do BM. Aguarde...')
        #%%
        filtroIncon = '"Indicação de autodiagnóstico de inconsistência no cálculo de capacitância - Conjunto 2 - Fase A"'
        time.sleep(3)
        navegador.find_element(By.XPATH, campoPesquisa).clear()
        navegador.find_element(By.XPATH, campoPesquisa).send_keys(filtroIncon)
        time.sleep(3)
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.XPATH, ordenaValores).click()
        navegador.find_element(By.CLASS_NAME, elementoLista).click()
        time.sleep(1)
        navegador.find_element(By.XPATH, campoValor).clear()
        navegador.find_element(By.XPATH, campoValor).send_keys('1')
        navegador.find_element(By.XPATH, alterar).click()
        navegador.find_element(By.XPATH, alterar).send_keys(escape)
        time.sleep(3)
        print('\nAlterações do BM concluídas')
        trocaIED = input('Deseja alterar outro IED? \n [1] - SIM\n [2]- NÃO\n ')
    else:
        trocaIED = input('Deseja alterar outro IED? \n [1] - SIM\n [2]- NÃO\n ')
#%%
input('Programa encerrado. Aperte uma tecla para fechar o programa...')