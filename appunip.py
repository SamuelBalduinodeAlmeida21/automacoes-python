from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
import time

# abrindo o navegador | recomendado usar o chrome por ter integração nativa - o selenium sempre espera o site esperar de carregar
navegador = webdriver.Chrome()

navegador.get('https://www.unip.br/aluno/central/')

# colocando o navegador em tela cheia (não é dar f11)
navegador.maximize_window()

# encontrando um elemento na tela do site
# CORREÇÃO: "id name" foi substituído por By.ID
botao_forms = navegador.find_element(By.ID, "btn_enviar")
botao_forms.click()

time.sleep(10)