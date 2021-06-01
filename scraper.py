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
from urllib.request import urlopen

#Congiruando o driver 
options = Options()
options.add_argument("--headless")

#Configurando o driver 
driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe',options=options)

#DATA 
## AMAZON ##
Urls_amazon = []
Urls_amazon_more = []
Amazon_price = []
Amazon_seller = []
Amazon_title = []
Amazon_seller_more = []
Amazon_price_more = []
Amazon_title_more = []

## MERCADO LIVRE ##
ml_url_base = 'https://cameras.mercadolivre.com.br/acessorios/estabilizadores/novo/estabilizador-zhiyun_OrderId_PRICE*DESC_NoIndex_True#applied_filter_id%3DITEM_CONDITION%26applied_filter_name%3DCondição%26applied_filter_order%3D8%26applied_value_id%3D2230284%26applied_value_name%3DNovo%26applied_value_order%3D1%26applied_value_results%3D464'
ml_urls = []
ml_price = []
ml_seller = []

## MAGAZINE LUIZA ##
magazine_urls = []
magazine_sellers = []
magazine_price = []

#FUNÇÕES 
## AMAZON ##
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

    #Criando variável global 
    global Urls_amazon

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

        Urls_amazon = [s for s in Urls_amazon if '/dp/' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'DJI' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Dji' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'YIJU' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'dji' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Feiyutech' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'FeiyuTech' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Osmo' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Hohem' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Moza' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'suporte' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Suporte' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'base' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'bolsa' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'motor' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'asixxsix' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'TransMount' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'carregamento' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Controle' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'adaptador' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Sagmei' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Qioniky' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'microfone' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Shara' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'Speedy' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'apc' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'BLUE' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'mobile' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'hubei1' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'rubsy' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'smallrig' in s]
        Urls_amazon = [s for s in Urls_amazon if not 'motor-focus' in s]
        Urls_amazon = [s for s in Urls_amazon if not '#customerReviews' in s]

def amazon_search_atributes(url):
    #Tempo de espera 
    time.sleep(5)

    #Criando o requests e BeautifulSoap
    driver.get(url)
    body_el = driver.find_element_by_css_selector('body')
    html_str = body_el.get_attribute('innerHTML')

    #Criano o soup 
    soup = BeautifulSoup(html_str, 'html.parser')

    #Fazendo o try para pegar o vendedor 
    try:
        seller = soup.find(id='sellerProfileTriggerId').text
        Amazon_seller.append(seller)
    except:
        Amazon_seller.append('Erro')

    #Fazendo o try do preço 
    try:
        price = soup.find(id="price_inside_buybox").text
        Amazon_price.append(price)
    except:
        Amazon_price.append("Erro")

    #Pegando o título do produto 
    try:
        title = soup.find(id='productTitle').text
        Amazon_title.append(title)
    except:
        Amazon_title.append('Erro')

    #Fazendo o try para ver se tem mais ofertas 
    try:
        soup.find(class_='olp-text-box').text

        #Pegando o texto do número de ofertas 
        ofertas = soup.find(class_='olp-text-box').text

        #Pegando apenas o número em parenteses dentro da frase 
        ofertas = ofertas[ofertas.index("(") + 1:ofertas.rindex(")")]

        #Transformando o número em um integer 
        ofertas = int(ofertas)

        #Fazendo o link de mais ofertas do mesmo produto 
        more_offers = 'https://www.amazon.com.br' + soup.find(class_='a-touch-link a-box olp-touch-link')['href']

        #Tempo de espera 
        time.sleep(3)

        #Fazendo o requests com o link de mais ofertas 
        driver.get(more_offers)
        time.sleep(2)
        body_el = driver.find_element_by_css_selector('body')
        html_str = body_el.get_attribute('innerHTML')

        #Criando o soup
        soup = BeautifulSoup(html_str, 'html.parser')

        #Pegando o nome dos sellers 
        for seller in soup.find_all(class_='a-size-small a-link-normal')[3:]:
            Amazon_seller_more.append(seller.text)

        #Limpando o nome dos sellers 
        Amazon_seller_more = [s for s in Amazon_seller_more if not 'política' in s]
        Amazon_seller_more = [s for s in Amazon_seller_more if not '+' in s]
        Amazon_seller_more = [s for s in Amazon_seller_more if not 'Detalhes' in s]
        Amazon_seller_more = [s for s in Amazon_seller_more if not 'Apagar' in s]
        Amazon_seller_more = [s for s in Amazon_seller_more if not 'Política de devolução' in s]

        #Pegando os preços de mais ofertas 
        for price in soup.find_all(class_='a-price-whole')[1:ofertas]:
            Amazon_price_more.append(price.text)
            Urls_amazon_more.append(url)
            Amazon_title_more.append(title)

    except:
        pass

## MERCADO LIVRE ##
def ml_search_links(url):
    #Colocando a variável como global 
    global ml_urls
    
    #Tempo mínimo
    time.sleep(2)

    #Fazendo o response 
    response = urlopen(url)
    html = response.read()

    #Criando o soup 
    bs = BeautifulSoup(html, 'html.parser')

    #Pegando todos os links da página 
    for link in bs.find_all('a', href=True):
        ml_urls.append(link['href'])

    #Fazendo o try para próximas páginas
    try:
        next_page_link = bs.find_all(class_='andes-pagination__arrow-title')[-1].text

        #Vendo se na seta está escrito 'Seguinte'
        if next_page_link == 'Seguinte':
            next_url = bs.find_all(class_='andes-pagination__link ui-search-link')[-1]['href']

            #Realizando o loop da função com o link da próxima página
            ml_search_links(next_url)
    except:
        pass

    #Limpando os links 
    ml_urls = [s for s in ml_urls if 'tracking_id' in s]
    ml_urls = [s for s in ml_urls if not 'suporte' in s]

    #Criar o Dataset com as url
    Dataset = pd.DataFrame()

    #Colocando as urls dentro do DataFrame
    Dataset['Urls'] = ml_urls

    #Tirando as duplicadas
    Dataset = Dataset.drop_duplicates()

    #Retornando o Dataset 
    return Dataset

def ml_search_attributes(url):
    #Tempo
    time.sleep(2)

    #Fazendo o response 
    response = urlopen(url)
    html = response.read()

    #Criando o soup
    bs = BeautifulSoup(html, 'html.parser')

    #Buscando o preço 
    try:
        price = bs.find(class_='price-tag-fraction').text
        ml_price.append(price)
    except:
        ml_price.append('Erro')

    #Vendedor
    try:
        seller_link = bs.find(class_='ui-pdp-media__action ui-box-component__action')['href']

        #Entrando na página do vendedor
        response = urlopen(seller_link)
        html = response.read()

        #Criando o soup
        bs = BeautifulSoup(html, 'html.parser')

        #Achando o nome do seller 
        seller_name = bs.find(class_='store-info__name').text

        #Append do nome do seller 
        ml_seller.append(seller_name)
    except:
        ml_seller.append("Erro")

## MAGAZINE LUIZA ##
def magazine_search_links():
    #Passando a variável global 
    global magazine_urls
    
    #Criando o tempo 
    time.sleep(0.3)

    #Criando a variável da página 
    pagina = 0 

    #Fazendo o loop 
    while pagina <= 4:
        
        #Pegando a url base 
        url = 'https://www.magazineluiza.com.br/busca/estabilizador%20Zhiyun/{}/?ordem=maior-preco'.format(pagina)

        #Fazendo o requests 
        response = urlopen(url)
        html = response.read()

        #Criando o soup 
        soup = BeautifulSoup(html, 'html.parser')

        #Achando todos os links 
        for link in soup.find_all("a", href=True):
            magazine_urls.append(link['href'])

        #Adicionando a página na url principal 
        pagina = pagina + 1

    #Limpando todos os links
    magazine_urls = [s for s in magazine_urls if '/p/' in s]
    magazine_urls = [s for s in magazine_urls if not 'parafuso' in s]
    magazine_urls = [s for s in magazine_urls if not 'controle' in s]
    magazine_urls = [s for s in magazine_urls if not 'extensor' in s]
    magazine_urls = [s for s in magazine_urls if not 'extensao' in s]
    magazine_urls = [s for s in magazine_urls if not 'carregador' in s]

def magazine_search_attributes(url):
    #Tempo 
    time.sleep(10)

    #Fazendo o requests 
    response = urlopen(url)
    html = response.read()

    #Criando o soup 
    bs = BeautifulSoup(html, 'html.parser')

    #try do preço 
    try: 
        price = bs.find(class_='price-template__text').text
        magazine_price.append(price)
    except:
        dispo = bs.find(class_="unavailable__product-title").text
        magazine_price.append(dispo)

    #Fazendo o try do seller 
    try: 
        seller = bs.find(class_="seller-info-button js-seller-modal-button").text
        magazine_sellers.append(seller)
    except:
        magazine_sellers.append("Erro")


#APLICATIVO 

#Printando as instruções iniciais 
print("Selecione quais são os marketplaces que irá realizar a busca:")
print("1 - Amazon\n2 - Americanas\n3 - Carrefour\n4 - Extra\n5 - Mercado Livre\n6 - Magazine Luiza\n7 - Shopee\n8 - Todos")

#Pegando a escolha do usuário 
escolha = int(input("Coloque o código do Marketplaces: "))


#Fazendo as situações de escolha do usuário
if escolha == 1:
    print("Você escolheu AMAZON, espere alguns minutos enquanto o sistema pega as informações")

    #Fazendo o while da página da Amazon 
    amazon_pages_url()

    #Printando que os links foram adquiridos
    print("Os links foram adquiridos, pegando informações\n Isso pode demorar alguns minutos")

    #Fazendo a função de atributos com o carregamento 
    for url in tqdm(Urls_amazon):
        amazon_search_atributes(url)

    #Criando Dataset 
    Dataset = pd.DataFrame()

    #Colocano os valores na colunas
    Dataset['Urls'] = Urls_amazon + Urls_amazon_more
    Dataset['Sellers'] = Amazon_seller + Amazon_seller_more
    Dataset['Preço'] = Amazon_price + Amazon_price_more
    Dataset['Loja'] = 'AMAZON'
    Dataset['ASIN'] = Dataset['Urls'].str.partition('/dp/')[2].str.partition('/')[0]

    #Limpando a caluna de preço 
    Dataset['Preço'] = Dataset['Preço'].str.replace("R","")
    Dataset['Preço'] = Dataset['Preço'].str.replace("$","")
    Dataset['Preço'] = Dataset['Preço'].str.replace(r"\n","")
    Dataset['Preço'] = Dataset['Preço'].str.replace(" ","")
    Dataset['Preço'] = Dataset['Preço'].str.replace(".","")
    Dataset['Preço'] = Dataset['Preço'].str.replace(",",".")
    Dataset['Preço'] = Dataset['Preço'].str.replace("Erro","0")

    #Passando o preço para float
    Dataset['Preço'] = Dataset['Preço'].astype('float64')

    #Aviso exportação 
    print("O ARQUIVO COM OS ANÚNCIOS FOI TRANSFERIDO NA PASTA DE DOWNLOADS DA FERRAMENTA")

    #Exportando o arquivo
    Dataset.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\amazon.xlsx', index=False)
elif escolha == 2:
    print("O site americanas ainda não está operacional")
elif escolha == 3:
    print("O site carrefour ainda não está operacional")
elif escolha == 4:
    print("O site Extra ainda não está operacional")
elif escolha == 5:
    print("Você escolheu MERCADO LIVRE, espera alguns minutos para a ferramenta começar a busca dos anúncios")

    #Fazendo a função para pegar todos os links de todas as páginas
    ml_search_links(ml_url_base)

    #Pegando todos os atributos 
    for url in tqdm(Dataset['Urls']):
        ml_search_attributes(url)

    #Colocando os valores nas colunas
    Dataset['Seller'] = ml_seller
    Dataset['Preço'] = ml_price
    Dataset['Loja'] = 'MERCADO LIVRE'

    #Colocando a coluna de preço em números 
    Dataset['Preço'] = Dataset['Preço'].str.replace('.','')
    Dataset['Preço'] = Dataset['Preço'].astype('int64')

    #Pegando apenas as informações que tem o preço maior que 200
    Dataset = Dataset[Dataset['Preço'] > 200]

    #Exportando o dataset 
    Dataset.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\mercado_livre.xlsx', index=False)
elif escolha == 6:
    print("Você escolheu MAGAZINE LUIZA, espera alguns minutos para a ferramenta começar a busca dos anúncios")

    #Fazendo a função 
    magazine_search_links()

    #Pegando todos os atributos 
    for url in tqdm(magazine_urls):
        magazine_search_attributes(url)

    #Criando o DataFrame 
    Dataset = pd.DataFrame()

    #Colocando os resultados na coluna
    Dataset['Urls'] = magazine_urls
    Dataset["Sellers"] = magazine_sellers
    Dataset["Preço"] = magazine_price
    Dataset["Loja"] = 'MAGAZINE LUIZA'
    
    #Fazendo a limpeza de espaços dentro dos sellers 
    Dataset['Sellers'] = Dataset['Sellers'].str.replace(" ","",1)

    #Exportando o Dataset 
    Dataset.to_excel(r"C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\magalu.xlsx", index=False)
elif escolha == 7:
    print("O site Shopee ainda não está operacional")
elif escolha == 8:
    print("Todos os marketplaces serão iniciados, isso demorará algumas horas")