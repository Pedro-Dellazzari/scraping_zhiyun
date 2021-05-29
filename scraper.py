#Sraper de estabilizador zhiyun

#Importando as bibliotecas 
import pandas as pd 
import requests 
import time 
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from tqdm import tqdm

#Congiruando o driver 
options = Options()
options.add_argument("--headless")

#Configurando o driver 
driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe',options=options)

#DATA 
Urls_amazon = []
Amazon_price = []
Amazon_seller = []
Amazon_title = []

#FUNÇÕES 
def amazon_pages_url():
    #Criando a variável da página
    paginas = 1 

    while paginas <= 2:
        url_base = 'https://www.amazon.com.br/s?k=estabilizador+zhiyun&s=price-desc-rank&page={}&__mk_pt_BR=ÅMÅŽÕÑ&qid=1620931072&ref=sr_pg_2'.format(paginas)

        #Realizando a funçaõ 
        amazon_search_links(url_base)

        #Adicionando o número para as páginas
        paginas = paginas + 1
def amazon_search_links(url):

    #Criando o tempo
    time.sleep(3)

    #Criando o requests e fazendo o Beautiful Soap
    driver.get(url)
    body_el = driver.find_element_by_css_selector('body')
    html_str = body_el.get_attribute('innerHTML')
    html_obj = HTML(html=html_str)

    #Pegando todos os links da página
    Links = [x for x in html_obj.links]

    #Criando os links de produtos 
    products_links = [f'https://www.amazon.com.br{x}' for x in Links]

    #Criando o loop para o append das urls 
    for link in products_links:
        Urls_amazon.append(link)
def amazon_clean_links(var_data):
    var_data = [s for s in var_data if '/dp/' in s]
    var_data = [s for s in var_data if not 'DJI' in s]
    var_data = [s for s in var_data if not 'Dji' in s]
    var_data = [s for s in var_data if not 'YIJU' in s]
    var_data = [s for s in var_data if not 'dji' in s]
    var_data = [s for s in var_data if not 'Feiyutech' in s]
    var_data = [s for s in var_data if not 'FeiyuTech' in s]
    var_data = [s for s in var_data if not 'Osmo' in s]
    var_data = [s for s in var_data if not 'Hohem' in s]
    var_data = [s for s in var_data if not 'Moza' in s]
    var_data = [s for s in var_data if not 'suporte' in s]
    var_data = [s for s in var_data if not 'Suporte' in s]
    var_data = [s for s in var_data if not 'base' in s]
    var_data = [s for s in var_data if not 'bolsa' in s]
    var_data = [s for s in var_data if not 'motor' in s]
    var_data = [s for s in var_data if not 'asixxsix' in s]
    var_data = [s for s in var_data if not 'TransMount' in s]
    var_data = [s for s in var_data if not 'carregamento' in s]
    var_data = [s for s in var_data if not 'Controle' in s]
    var_data = [s for s in var_data if not 'adaptador' in s]
    var_data = [s for s in var_data if not 'Sagmei' in s]
    var_data = [s for s in var_data if not 'Qioniky' in s]
    var_data = [s for s in var_data if not 'microfone' in s]
    var_data = [s for s in var_data if not 'Shara' in s]
    var_data = [s for s in var_data if not 'Speedy' in s]
    var_data = [s for s in var_data if not 'apc' in s]
    var_data = [s for s in var_data if not 'BLUE' in s]
    var_data = [s for s in var_data if not 'mobile' in s]
    var_data = [s for s in var_data if not 'hubei1' in s]
    var_data = [s for s in var_data if not 'rubsy' in s]
    var_data = [s for s in var_data if not 'smallrig' in s]
    var_data = [s for s in var_data if not 'motor-focus' in s]
    var_data = [s for s in var_data if not '#customerReviews' in s]




#APLICATIVO 

#Printando as instruções iniciais 
print("Selecione quais são os marketplaces que irá realizar a busca:")
print("1 - Amazon\n2 - Americanas\n3 - Carrefour\n4 - Extra\n5 - Mercado Livre\n6 - Magazine Luiza\n7 - Shopee\n8 - Todos")

#Pegando a escolha do usuário 
escolha = input("Coloque o código do Marketplaces: ")


#Fazendo as situações de escolha do usuário
if escolha == '1':
    print("Você escolheu AMAZON, espere alguns minutos enquanto o sistema pega as informações")

    #Fazendo o while da página da Amazon 
    amazon_pages_url()

    #Fazendo o limpeza dos Links com a função 
    amazon_clean_links(Urls_amazon)

    #Printando que os links foram adquiridos
    print("Os links foram adquiridos, pegando informações\n Isso pode demorar alguns minutos")
