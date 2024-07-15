import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Configurando o driver do navegador usando webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrindo a página do Mercado Livre
driver.get("https://www.mercadolivre.com.br")

try:
    # Esperando até que o campo de busca esteja presente e visível
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )

    # Digitando o termo de busca e enviando
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Esperando até que os resultados estejam presentes
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ui-search-layout"))
    )

    # Capturando os títulos e preços dos primeiros resultados
    results = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")
    
    # Criando uma lista para armazenar os dados
    data = []

    for result in results[:10]:  # Limitando aos primeiros 10 resultados
        title_element = result.find_element(By.CSS_SELECTOR, "h2.ui-search-item__title")
        price_elements = result.find_elements(By.CSS_SELECTOR, "span.price-tag-fraction")

        title = title_element.text
        price = "R$" + ".".join([element.text for element in price_elements])

        data.append([title, price])

except Exception as e:
    print(f"Erro: {e}")
finally:
    # Salvando os dados em um arquivo CSV
    with open('resultados.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])  # Cabeçalho
        writer.writerows(data)
    
    print("Dados salvos em 'resultados.csv'")
    
    # Adicionando um tempo de espera para visualizar a ação antes de fechar
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
