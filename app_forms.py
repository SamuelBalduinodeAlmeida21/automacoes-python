from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
import time

#abrindo o navegador | recomendado usar o chrome por ter integração nativa - o selenium sempre espera o site esperar de carregar


navegador = webdriver.Chrome()

navegador.get('https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?prevorigin=Marketing&prevsubpage=design')

#colocando o navegador em tela cheia (não é dar f11)
navegador.maximize_window()

#encontrando um elemento na tela do site 
botao_forms = navegador.find_element(By.CLASS_NAME, "-pD-187")
botao_forms.click()

time.sleep(10) 