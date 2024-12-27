from selenium import webdriver
from selenium.webdriver.common.by import By

# Função responsável pela coleta de dados financeiros de uma empresa=
def scrapData(enterprise):
    url = f"https://finance.yahoo.com/quote/{enterprise}/history?p={enterprise}"
    driver = webdriver.Chrome()
    driver.get(url)
    rows = driver.find_elements(By.XPATH, '//table//tr')

    if not rows:
        return 404

    data = []
    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, 'td')
        if len(cols) == 7:  # Verificando se a linha é valida (obrigatoriamente deve ter 7 colunas)
            data.append([col.text for col in cols])
    
    driver.quit()
    return data
