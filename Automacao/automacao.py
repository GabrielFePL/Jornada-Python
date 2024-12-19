import pyautogui as pa
import time
pa.PAUSE = 1.5
pa.press("win")
pa.write("chrome") 
pa.press("enter")
time.sleep(5)
pa.click(x=418, y=449)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(4)
pa.click(x=386, y=321)
pa.write("seuemail@dominio.com")
pa.press("tab")
pa.write("suaSenha")
pa.press("tab")
pa.press("enter")
time.sleep(4)
import pandas as pd
import numpy as np
import openpyxl as op
base_prod = pd.read_csv("C:\\repJornadaPython\Jornada-Python\Automacao\produtos.csv")
pa.PAUSE = 0.5
for register in base_prod.index:
    pa.click(x=298, y=228)
    pa.write(str(base_prod.loc[register, "codigo"]))
    pa.press("tab")
    pa.write(str(base_prod.loc[register, "marca"]))
    pa.press("tab")
    pa.write(str(base_prod.loc[register, "tipo"]))
    pa.press("tab")
    pa.write(str(base_prod.loc[register, "categoria"]))
    pa.press("tab")
    pa.write(str(base_prod.loc[register, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(base_prod.loc[register, "custo"]))
    pa.press("tab")
    obs = str(base_prod.loc[register, "obs"])
    if obs != "nan":
        pa.write(obs)
    pa.press("tab")
    pa.press("enter")
    pa.scroll(5000)