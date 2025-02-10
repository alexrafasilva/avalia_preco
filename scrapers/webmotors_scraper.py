import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from src.database import inserir_preco
import time
import logging

# Configuração de logging
logging.basicConfig(filename='scraping.log', level=logging.INFO)

def scrape_webmotors():
    base_url = "https://www.webmotors.com.br/suvs"
    modelos_alvo = {
        'Volkswagen T-Cross': 'volkswagen/t-cross',
        'Ford Territory': 'ford/territory',
        'Chevrolet Tracker': 'chevrolet/tracker',
        'Hyundai Creta': 'hyundai/creta',
        'Honda HR-V': 'honda/hr-v'
    }

    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    for modelo, endpoint in modelos_alvo.items():
        try:
            url = f"{base_url}/{endpoint}"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extração de preços (atualizado para estrutura atual do Webmotors)
            cards = soup.find_all('div', class_='card-body')
            
            for card in cards:
                marca_modelo = card.find('h2', class_='title-card').text.strip()
                ano_element = card.find('span', text='Ano')
                ano = ano_element.find_next('strong').text.strip() if ano_element else '2023'
                
                preco_element = card.find('div', class_='price-card')
                preco = preco_element.text.replace('R$', '').replace('.', '').strip() if preco_element else None
                
                if preco:
                    marca = modelo.split()[0]
                    inserir_preco(
                        marca=marca,
                        modelo=marca_modelo,
                        preco=float(preco)
                    )
                    logging.info(f"Dados inseridos: {marca} | {marca_modelo} | R${preco}")
            
            time.sleep(2)  # Respeito ao rate limiting
            
        except Exception as e:
            logging.error(f"Erro ao processar {modelo}: {str(e)}")
            continue

if __name__ == "__main__":
    scrape_webmotors()