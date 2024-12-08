import pyautogui
from time import sleep

# https://pyautogui.readthedocs.io/en/latest/quickstart.html#general-functions
# pyautogui.click = clicar com o mouse
# pyautogui.write = escrever um texto
# pyautogui.press = apertar tecla
# pyautogui.hootkeys = combinação de teclas
# pyautogui.scroll = rolar a tela com o mouse
pyautogui.PAUSE = 0.5
# Passo 1.1 - Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
          
           
# Passo 1.2. Abrir o link do sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
sleep(1)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3)


# Passo 2 - Fazer o login
pyautogui.press('tab')
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab')
pyautogui.hotkey("ctrl", "a")
pyautogui.write("*******")
pyautogui.press('enter') 

# Passo 3 - Pegar os dados
import pandas as pd
dados = pd.read_csv('produtos.csv')

# Passo 4 - Cadastrar um produto
sleep(1)
for linha in range(0,5): # substituir range(0,5) por dados.index:
    pyautogui.click(x=471, y=249) #configurar em sua tela a posição do mouse sobre o campo Código utilizando o programa position.py

    codigo = str(dados.loc[linha,'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(dados.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(dados.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(dados.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    preco_unitario = str(dados.loc[linha,'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(dados.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(dados.loc[linha,'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.click(x=457, y=291)
    pyautogui.scroll(1000)
    pyautogui.click(x=457, y=291)
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

sleep(4)
pyautogui.hotkey('ctrl', 'F4')