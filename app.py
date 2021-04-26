from selenium import webdriver
import time
import pandas as pd
import urllib
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

msg = urllib.parse.quote("Isso é um Teste! Esse texto está sendo escrito pelo Robô Boladão \\n Você é uma Cobaia %0D Liga Noix qualquer coisa %0D Ihuuuuu %0D Isso ainda é um teste!")
contatos_df = pd.read_excel(r"C:\Users\Will\Downloads\ContatosEnvia.xlsx", usecols=[0], names=["Numeros"])
cont = int(len(contatos_df.index))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

while len(driver.find_elements_by_id("side")) < 1:
    time.sleep(1)

def buscar_contato(contatos):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    time.sleep(8)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

def enviar_mensagem(msg):
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click()
    time.sleep(3)
    campo_msg[1].send_keys(msg)
    time.sleep(5)
    campo_msg[1].send_keys(Keys.ENTER)
    time.sleep(10)

for num in range(cont):
    if num != ' ':
        contatos = contatos_df.iloc[num].loc["Numeros"]
        buscar_contato(contatos)
        enviar_mensagem(msg)
    else:
        exit(0)