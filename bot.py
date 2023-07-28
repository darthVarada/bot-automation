#passo a passo do projeto
#passo 1: entrar no sistema da empresa
# link do sistema
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui as pa
import time
import pandas as pd
import keyboard

def parar_looping():
    return keyboard.is_pressed("Esc")
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.click -> clicar em algum lugar na tela
#pyautogui.hotkey -> combinacao de teclas

pa.press("win")
pa.write("chrome")
pa.press("enter")
time.sleep(3)
pa.hotkey("ctrl", "shift", "n")
time.sleep(0.5)
pa.hotkey("ctrl", "l")
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(2)
pa.press("tab")
#passo 2: logar no sistema
pa.write("pythonimpressionandor@gmail.com")
pa.press("tab")
pa.write("12345")
pa.press("tab")
pa.press("enter")
#passo 3: cadastrar no sistema
time.sleep(0.5)

pa.press("tab")
# pegando tabela
tabela = pd.read_csv("C:/Users/fafap/Desktop/pc/estudos/QUINTOANO/IADeepLeaning/meu aprendizado/Tratamento_de_dados/video2_hashtag/produtos.csv")
print(tabela)

linha = 0
for linha in range(len(tabela)):
    if parar_looping():
        break

    codigo = tabela.loc[linha, "codigo"]
    #escrever campo
    pa.write(str(codigo))
    #proximo marca
    pa.press("tab")
    marca = tabela.loc[linha, "marca"]
    pa.write(str(marca))
    #proximo tipo
    pa.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pa.write(str(tipo))
    #campo categoria
    pa.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pa.write(str(categoria))
    #campo preco unitario
    pa.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pa.write(str(preco_unitario))
    #campo custo
    pa.press("tab")
    custo = tabela.loc[linha, "custo"]
    pa.write(str(custo))
    #campo obs
    pa.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pa.write(str(obs))
    pa.press("tab")
    pa.press("enter")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
    pa.hotkey("shift", "tab")
#repetir processo de cadastro ate o fim dos produtos    
