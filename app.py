from selenium import webdriver
import time
import pandas as pd
import urllib

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

msg = "asdasdasdasd!"

contatos_df = pd.read_excel(r"C:\Users\Will\Downloads\ContatosEnvia.xlsx", usecols=[0], names=["Numeros"])
cont = int(len(contatos_df.index))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

while len(driver.find_elements(By.ID, "side")) < 1:
    time.sleep(5)


def buscar_contato(contatos):
    campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    time.sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    time.sleep(8)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)


def enviar_mensagem(msg):
    campo_msg = driver.find_element(By.XPATH,
                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    campo_msg.click()
    time.sleep(7)
    for m in msg:
        if m == "&":
            campo_msg.send_keys(Keys.SHIFT + Keys.ENTER)
        else:
            campo_msg.send_keys(m)
    campo_msg.send_keys(Keys.ENTER)
    time.sleep(10)


for num in range(cont):
    if num != ' ':
        contatos = contatos_df.iloc[num].loc["Numeros"]
        buscar_contato(contatos)
        enviar_mensagem(msg)
    else:
        exit(0)
