from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Configurando o driver do navegador usando webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrindo a página do YouTube
driver.get("https://www.youtube.com/")

# Encontrando o campo de busca
busca = driver.find_element(By.NAME, "search_query")

# Digitando o termo de busca e enviando
busca.send_keys("System of a Down")
busca.send_keys(Keys.RETURN)

# Esperando que os resultados apareçam e clicando no primeiro vídeo
try:
    # Aguarda até que os títulos dos vídeos apareçam nos resultados
    primeiro_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title"))
    )
    # Clicando no primeiro vídeo
    primeiro_video.click()

    # Adicionando um tempo de espera para visualizar o vídeo
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "html5-video-player"))
    )
    print("Vídeo aberto com sucesso.")
finally:
    # Adicionando um tempo de espera para que o vídeo possa ser assistido antes de fechar
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
