import pyautogui as py
import pandas as pa
import time 

py.PAUSE = 0.5 

py.press('Win')
py.write('Google')
py.press('Enter')

time.sleep(1)

py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('Enter')

time.sleep(1)

py.click(x=512, y=373)
py.write('blablabla@gmail.com')
py.press('Tab')
py.write('12345678')
py.press('Tab')
py.press('Enter')

time.sleep(1)

py.press('Enter')

tabela = pa.read_csv('produtos.csv')

py.click(x=511, y=267)

for linha in tabela.index:
    py.click(x=511, y=267)
    py.write (str(tabela.loc[linha, 'codigo']))
    py.press('Tab')
    py.write(str(tabela.loc[linha, 'marca']))
    py.press('Tab')
    py.write(str(tabela.loc[linha, 'tipo']))
    py.press('Tab')
    py.write(str(tabela.loc[linha, 'categoria']))
    py.press('Tab')
    py.write(str(tabela.loc[linha, 'preco_unitario']))
    py.press('Tab')
    py.write(str(tabela.loc[linha, 'custo']))
    py.press('Tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        py.write(obs)
    py.press('Tab')
    py.press('Enter')
    py.press('home')
    time.sleep(1)

    
