from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

contatos = ['+55 61 9999-9999', '+55 61 9999-9999']
msg = 'Isso é um Teste!'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(30)

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
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
    time.sleep(5)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(msg)
# Campo de Mensagem 'copyable-text selectable-text'



