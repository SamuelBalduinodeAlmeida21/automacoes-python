from selenium import webdriver
from selenium.webdriver.common.by import By
# Importações necessárias para a Espera Explícita
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

# abrindo o navegador | recomendado usar o chrome por ter integração nativa - o selenium sempre espera o site esperar de carregar
navegador = webdriver.Chrome()

navegador.get('https://forms.cloud.microsoft/Pages/DesignPageV2.aspx?prevorigin=Marketing&prevsubpage=design')

# colocando o navegador em tela cheia (não é dar f11)
navegador.maximize_window()

# 1. Configura a espera com um tempo limite de 10 segundos
wait = WebDriverWait(navegador, 10)

# 2. Encontra o elemento, mas espera que ele esteja presente (apareça no DOM)
# Se o elemento não for encontrado em 10 segundos, um TimeoutException será lançado.
try:
    botao_forms = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "-pD-187"))
    )
    # 3. Clica no elemento após ele ser encontrado
    botao_forms.click()
    
except Exception as e:
    print(f"Erro ao encontrar ou clicar no elemento: {e}")

# Pausa final (mantive seu time.sleep, mas ele não é mais necessário para a busca)
time.sleep(10)