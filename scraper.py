#Sraper de estabilizador zhiyun

#Importando as bibliotecas 
import pandas as pd 
import requests 
import time
from requests.models import Response 
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from tqdm import tqdm
from urllib.request import urlopen
import json as JSON

#Congiruando o driver 
options = Options()
options.add_argument("--headless")
options.add_argument('--log-level=3')

#Configurando o driver 
driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe',options=options)

#Configurando os headers 
header_carrefour_base = {'authority':'www.carrefour.com.br','path':'/busca/estabilizador%20zhiyun?order=OrderByTopSaleDESC&page=1','scheme':'https','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.154'}
header_carrefour_produtos = {'authority':'www.carrefour.com.br','scheme':'https','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.154'}

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

## CARREFOUR ##
carrefour_links = []
carrefour_links_certo = []
carrefour_sellers = []
carrefour_price = []

## SHOPEE ##
shopee_products_links = []
shopee_seller = []
shopee_price = []

## EXTRA ##
extra_urls = []
extra_sellers = []
extra_price = []
extra_sellers_ofertas = []
extra_price_ofertas = []
extra_urls_ofertas = []

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

    #Limpando os links
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
    Urls_amazon = [s for s in Urls_amazon if not 'Mobile-3' in s]
    Urls_amazon = [s for s in Urls_amazon if not 'KIICN' in s]
    Urls_amazon = [s for s in Urls_amazon if not 'Motor' in s]
    Urls_amazon = [s for s in Urls_amazon if not 'Sunbacas' in s]

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
    ml_urls = [s for s in ml_urls if not 'dslr' in s]
    ml_urls = [s for s in ml_urls if not 'controle' in s]
    ml_urls = [s for s in ml_urls if not 'smallrig' in s]
    ml_urls = [s for s in ml_urls if not 'alca-dupla' in s]
    ml_urls = [s for s in ml_urls if not 'feiyutech' in s]
    ml_urls = [s for s in ml_urls if not 'dji' in s]
    ml_urls = [s for s in ml_urls if not 'base' in s]
    ml_urls = [s for s in ml_urls if not 'quickengate' in s]
    ml_urls = [s for s in ml_urls if not 'configuraco' in s]
    ml_urls = [s for s in ml_urls if not 'h4' in s]

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
    magazine_urls = [s for s in magazine_urls if not 'gyro' in s]

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

## carrefour ## 
def carrefour_page_urls():

    #Variável de página 
    pagina = 1 

    #Fazendo loop para fazer a função de pegar links 
    while pagina <= 4: 

        #Criando url base 
        url_base = 'https://www.carrefour.com.br/busca/estabilizador%20zhiyun?order=OrderByTopSaleDESC&page={}'.format(pagina)

        #Fazer a função 
        carrefour_search_link(url_base)

        #Acrescentando o número da página 
        pagina = pagina + 1 

        #Fazendo um tempo antes de fazer a função novamente 
        time.sleep(10)

def carrefour_search_link(url):
    #Tornando as variáveis globais
    global carrefour_chaves
    global carrefour_links
    
    #Faazendo o tempo 
    time.sleep(10)

    #Fazendo o requests 
    response = requests.get(url, headers=header_carrefour_base)
    html = response.text 

    #Criando o beautifulSoap 
    bs = BeautifulSoup(html, 'html.parser')

    #Pegar o template com o json 
    template = bs.find('template', attrs={'data-type':'json', 'data-varname':'__STATE__'})

    #Pegando o texto dentro do template 
    text = template.contents[1].string

    #Fazendo o json
    json = JSON.loads(text)

    #Criando variável para as chaves 
    carrefour_chaves = []

    #Pegando as chaves dentro da página
    for key in json:
        carrefour_chaves.append(key)

    #Limpando as chaves 
    carrefour_chaves = [s for s in carrefour_chaves if 'Product' in s]
    carrefour_chaves = [s for s in carrefour_chaves if not 'properties' in s]
    carrefour_chaves = [s for s in carrefour_chaves if not '$' in s]
    carrefour_chaves = [s for s in carrefour_chaves if not 'specificationGroups' in s]
    carrefour_chaves = [s for s in carrefour_chaves if not 'items' in s]

    #Construindo os links 
    #Pegando os links dentro de cada chave de produto e construindo o link
    for chave in carrefour_chaves:
        carrefour_links.append('https://www.carrefour.com.br/'+ json[chave]['link'] + '/p')
    
def carrefour_search_attributes(url):
    global carrefour_links_certo
    global carrefour_price
    global carrefour_sellers
    
    #Fazendo o tempo 
    time.sleep(12)

    #Fazendo o requests 
    response = requests.get(url, headers=header_carrefour_produtos)
    html = response.text

    #Fazendo o beautiful 
    bs = BeautifulSoup(html, 'html.parser')

    #Achando o template 
    template = bs.find('template', attrs={'data-type':'json','data-varname':'__STATE__'})

    #Pegando o texto dentro 
    text = template.contents[1].string

    #Carregando como json 
    json = JSON.loads(text)

    #Pegar a chave principal com o nome da key 
    try:
        principal_key = list(json.keys())[0]

        #Criar a chave para pegar todos os sellers 
        seller_key = principal_key + ".items.0"

        #Pegando o total de sellers
        #Variável para pegar os ids
        i = 0 

        #Variável com o total de sellers do mesmo produto
        sellers = []

        #Pegando a quantidade sellers da oferta 
        for id in json[seller_key]['sellers'][i]['id']:
            try:
                sellers.append(json[seller_key]['sellers'][i]['id'])
                i = i + 1 
            except:
                pass

        #Pegando a quantidade certa de urls
        for seller in sellers:
            carrefour_links_certo.append("https://www.carrefour.com.br/"+json[principal_key]['linkText']+'/p')

        s = 0

        #Pegando os sellers 
        for seller in sellers: 
            carrefour_sellers.append(json[seller_key+'.sellers.'+str(s)]['sellerName'])
            s = s + 1 

        a = 0

        #Pegando os preços 
        for seller in sellers: 
            carrefour_price.append(json["$"+seller_key+".sellers."+str(a)+".commertialOffer"]['Price'])
            a = a + 1 
    except:
        pass          

## shopee ##
def shopee_urls():
    #Criando a variável global 
    global shopee_products_links

    #Variável por página 
    pag = 0 

    while pag <= 4:
        #Tempo
        time.sleep(1)

        #Fazendo o requests com o Chrome Driver 
        url = "https://shopee.com.br/search?keyword=estabilizador%20zhiyun&order=desc&page={}&sortBy=price".format(pag)
        driver = webdriver.Chrome()
        driver.get(url)

        #Aguardando tempo para carregar toda a página
        time.sleep(5)

        #Criando o BeautifulSoup
        bs = BeautifulSoup(driver.page_source, 'lxml')

        #Pegando todos os links
        for link in bs.find_all("a", href=True):
            shopee_products_links.append('https://www.shopee.com.br' + link['href'])

        #Fechando o driver 
        driver.close()

        #Adicioanndo mais uma página na url 
        pag = pag + 1

    #Limpando todos os links 
    shopee_products_links = [s for s in shopee_products_links if '-i' in s]

    #Retirando maioria das urls 
    shopee_products_links = [s for s in shopee_products_links if not 'Ulanzi' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Assento' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Carregador' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Pobe' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Peso' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'DJI' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Pólo' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Yiliwit' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Feiyu' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Teenmix' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Brdynwave1' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Belud' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Zuoy' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Parafuso' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Sling' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Handheld' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Manual' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Fire-Computing' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Travel' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Protetor-Eletrônico' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Feiyutech' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'Laing' in s]
    shopee_products_links = [s for s in shopee_products_links if not '(Enew)' in s]
    shopee_products_links = [s for s in shopee_products_links if not 'ring' in s]

def shopee_search_attributes(url):
    #Fazendo tempo 
    time.sleep(3)

    #Entrando nas páginas 
    driver = webdriver.Chrome()
    driver.get(url)

    #Fazendo tempo para a página carregar inteira 
    time.sleep(5)

    #Fazendo o soup 
    bs = BeautifulSoup(driver.page_source, 'lxml')

    #Fechando o driver
    driver.close()

    #Try do vendedor 
    try:
        shopee_seller.append(bs.find(class_='_3uf2ae').text)
    except:
        shopee_seller.append("Erro")

    #Try do preço 
    try:
        shopee_price.append(bs.find(class_='_3e_UQT').text)
    except:
        shopee_price.append('Erro')

## extra ## 
def extra_search_urls():
    #Colocando a variável como global 
    global extra_urls

    #Inicializando webdriver 
    driver = webdriver.Chrome()

    #Url base 
    url = 'https://www.extra.com.br/estabilizador-zhiyun/b?sortby=descprice'

    #Inicializando o driver na página 
    driver.get(url)

    #Fazendo o while para carregar no botão "Carregar Mais"
    while True:
        try:
            #Encontrando o botão 
            load_more = driver.find_element_by_xpath('//button[text()="Ver mais produtos"]')

            #Esperando carregar o conteúdo da página 
            time.sleep(3)

            #Clicando no botão 
            load_more.click()

            #Experando mais um pouco para carregar o conteúdo do botão 
            time.sleep(2)
        except:
            break

    #Criando o beautiful usando o driver 
    bs = BeautifulSoup(driver.page_source, 'html.parser')

    #Fechando o driver
    driver.close()

    #Pegando os links 
    for link in bs.find_all("a"):
        extra_urls.append(link['href'])

    #Limpando os links para apenas produtos 
    extra_urls = [s for s in extra_urls if 'IdSku=' in s]

def extra_search_attributes(url):
    #Criando o webdriver 
    driver = webdriver.Chrome()
    driver.get(url)

    #Tempo 
    time.sleep(3)

    #Fazendo o soup 
    bs = BeautifulSoup(driver.page_source, 'html.parser')

    #Fechandoo chrome
    driver.close()

    #Fazendo o try do seller 
    try:
        extra_sellers.append(bs.find(class_='text-primary css-fv6pw7 eym5xli0').text)
    except:
        extra_sellers.append("Erro")

    #Fazendo o try do preço 
    try:
        extra_price.append(bs.find(class_='product-price-value').text)
    except:
        extra_price.append("Erro")

    #Vendo se tem mais ofertas do mesmo produto 
    try:
        ofertas = bs.find_all(class_='css-ysnrax eym5xli0')
        for seller_name in ofertas:
            extra_sellers_ofertas.append(seller_name.text)
            extra_urls_ofertas.append(url)
    except:
        pass

    #Fazendo o try para pegar o preço 
    try:
        ofertas = bs.find_all(class_='prod-sellers__seller-price css-11oup1l eym5xli0')
        for oferta in ofertas:
            extra_price_ofertas.append(oferta.text)
    except:
        pass

## Limpeza ##
def limpeza(a):
    if 'smooth-xs' in a:
        return 'Smooth-XS'
    elif 'Suave-Xs' in a:
        return 'Smooth-XS'
    elif 'smooth-x' in a:
        return 'Smooth-x'
    elif 'smooth-X' in a:
        return 'Smooth X'
    elif 'Suave-X' in a:
        return 'Smooth X'
    elif 'smooth-Q2' in a:
        return 'Smooth-Q2'
    elif 'Q2' in a:
        return 'Smooth-Q2'
    elif 'crane-m2' in a:
        return 'Crane-M2'
    elif 'Smooth-4' in a:
        return 'Smooth 4'
    elif 'smooth-4' in a:
        return 'Smooth 4'
    elif 'smooth-3' in a:
        return 'Smooth 3'
    elif 'smooth-q' in a:
        return 'Smooth Q'
    elif 'smooth-2' in a:
        return 'Smooth 2'
    elif 'SMOOTH-X' in a:
        return 'Smooth-c'
    elif 'crane-2s' in a:
        return 'Crane 2s'
    elif 'weebill-s' in a:
        return 'Weebill S'
    elif 'crane-3s' in a:
        return 'Crane 3s'
    elif 'CRANE-3S' in a:
        return 'Crane 3s'
    elif 'CRANE-3S' in a:
        return 'Crane 3s'
    elif 'Crane-3s' in a:
        return 'Crane 3S'
    elif 'Guindaste-3-lab' in a:
        return 'Crane 3 Lab'
    elif 'Crane-3' in a:
        return 'Crane 3S'
    elif 'crane-2' in a:
        return 'Crane 2'
    elif 'Crane-2S' in a:
        return 'Crane 2S'
    elif 'CRANE-2S-COMBO'  in a:
        return 'Crane 2S Combo'
    elif 'CRANE-2S' in a:
        return 'Crane 2S'
    elif 'crane-3-lab' in a:
        return 'Crane 3 Lab'
    elif 'weebill-lab' in a:
        return 'Weebill LAB'
    elif 'Weebil-S' in a:
        return 'Weebil S'
    elif 'Weebill-S' in a:
        return 'Weebil S'
    elif 'weebill-s' in a:
        return 'Weebill-S'
    elif 'crane-plus' in a:
        return 'Crane Plus'
    elif 'crane-m' in a:
        return 'Crane-M'
    elif 'CRANE M2' in a:
        return 'Crane M2'
    elif 'CRANE-M2' in a:
        return 'Crane M2'
    elif 'SMOOTH-4' in a:
        return 'Smooth 4'
    elif 'rider-m' in a:
        return 'Rider-M'
    elif 'evolution' in a:
        return 'Evolution'
    elif 'Lisa-X' in a:
        return 'Smooth X'

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
    print("***************** Você selecinou CARREFOUR **************")

    #Fazendo a função para pegar todos os links 
    carrefour_page_urls()

    #Fazendo a função para pegar os atrributos 
    for url in tqdm(carrefour_links):
        carrefour_search_attributes(url)

    #Criando o DataFrame
    Dataset = pd.DataFrame()

    #Colocando os resultados nas colunas
    Dataset["Urls"] = carrefour_links_certo
    Dataset['Sellers'] = carrefour_sellers
    Dataset['Preços'] = carrefour_price
    Dataset['Loja'] = 'CARREFOUR'

    #Exportando a planilha 
    Dataset.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\carrefour.xlsx', index=False)
elif escolha == 4:
    print("-------- INICIANDO EXTRA -----------")

    #Fazendo a função base 
    extra_search_urls()

    #Fazendo a função para cada url de produto 
    for url in tqdm(extra_urls):
        extra_search_attributes(url)

    #Criando o dataset 
    dataset = pd.DataFrame()

    #Colocando as informações dentro do dataframe 
    dataset['Urls'] = extra_urls + extra_urls_ofertas
    dataset['Seller'] = extra_sellers + extra_sellers_ofertas
    dataset['Price'] = extra_price + extra_price_ofertas

    #Exportando o dataset 
    dataset.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\extra.xlsx', index=False)
elif escolha == 5:
    print("Você escolheu MERCADO LIVRE, espera alguns minutos para a ferramenta começar a busca dos anúncios")

    #Fazendo a função para pegar todos os links de todas as páginas
    ml_search_links(ml_url_base)

    #Limpando os links 
    ml_urls = [s for s in ml_urls if 'tracking_id' in s]
    ml_urls = [s for s in ml_urls if not 'suporte' in s]

    #Criar o Dataset com as url
    Dataset = pd.DataFrame()

    #Colocando as urls dentro do DataFrame
    Dataset['Urls'] = ml_urls

    #Tirando as duplicadas
    Dataset = Dataset.drop_duplicates()

    #Fazendo a função com as urls certas
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
    print("----------- INICIANDO SHOPEE -------------")

    #Fazendo função para pegar urls 
    shopee_urls()

    #Fazendo a função para pegar os atributos 
    for url in tqdm(shopee_products_links):
        shopee_search_attributes(url)

    #Criando o dataset 
    dataset = pd.DataFrame()

    #Colocando os resultados dentro do dataset 
    dataset['Urls'] = shopee_products_links
    dataset['Seller'] = shopee_seller
    dataset['Preço'] = shopee_price

    #Exportando o Dataset 
    dataset.to_excel(r"C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\shopee.xlsx", index=False)
elif escolha == 8:
    print("Todos os marketplaces serão iniciados, isso demorará algumas horas")

    print("\n******************* Iniciando a busca por AMAZON ***************\n")

    #Fazendo as funções de busca da AMAZON 

    #Função para pegar os links 
    amazon_pages_url()

    #Fazendo a função de busca de atributos 
    for url in tqdm(Urls_amazon):
        amazon_search_atributes(url)

    #Colocando as informações no Dataframe da AMAZON 
       
    #Criando Dataset 
    Dataset_amazon = pd.DataFrame()

    #Colocano os valores na colunas
    Dataset_amazon['Urls'] = Urls_amazon + Urls_amazon_more
    Dataset_amazon['Sellers'] = Amazon_seller + Amazon_seller_more
    Dataset_amazon['Preço'] = Amazon_price + Amazon_price_more
    Dataset_amazon['Loja'] = 'AMAZON'
    Dataset_amazon['ASIN'] = Dataset_amazon['Urls'].str.partition('/dp/')[2].str.partition('/')[0]

    #Limpando a caluna de preço 
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace("R","")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace("$","")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace(r"\n","")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace(" ","")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace(".","")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace(",",".")
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].str.replace("Erro","0")

    #Passando o preço para float
    Dataset_amazon['Preço'] = Dataset_amazon['Preço'].astype('float64')
    
    #Passando limpeza 
    Dataset_amazon['Item'] = Dataset_amazon['Urls'].apply(limpeza)

    #Exportando o arquivo
    Dataset_amazon.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\amazon.xlsx', index=False)

    #AVISO 
    print('****************** O ARQUIVO FOI BAIXADO *************************')

    #Inicio MERCADO LIVRE 
    print("************************* INICIALIZANDO MERCADO LIVRE **********************")

    #Criando tempo 
    time.sleep(10)

    #Fazendo a função para pegar todos os links de todas as páginas
    ml_search_links(ml_url_base)

    #Limpando os links 
    ml_urls = [s for s in ml_urls if 'tracking_id' in s]
    ml_urls = [s for s in ml_urls if not 'suporte' in s]

    #Criar o Dataset com as url
    Dataset_mercado_livre = pd.DataFrame()

    #Colocando as urls dentro do DataFrame
    Dataset_mercado_livre['Urls'] = ml_urls

    #Tirando as duplicadas
    Dataset_mercado_livre = Dataset_mercado_livre.drop_duplicates()

    #Fazendo a função com as urls certas
    for url in tqdm(Dataset_mercado_livre['Urls']):
        ml_search_attributes(url)

    #Colocando os valores nas colunas
    Dataset_mercado_livre['Seller'] = ml_seller
    Dataset_mercado_livre['Preço'] = ml_price
    Dataset_mercado_livre['Loja'] = 'MERCADO LIVRE'

    #Colocando a coluna de preço em números 
    Dataset_mercado_livre['Preço'] = Dataset_mercado_livre['Preço'].str.replace('.','')
    Dataset_mercado_livre['Preço'] = Dataset_mercado_livre['Preço'].astype('int64')

    #Pegando apenas as informações que tem o preço maior que 200
    Dataset_mercado_livre = Dataset_mercado_livre[Dataset_mercado_livre['Preço'] > 200]

    #Item
    Dataset_mercado_livre['Item'] = Dataset_mercado_livre['Urls'].apply(limpeza)


    #Exportando o dataset 
    Dataset_mercado_livre.to_excel(r'C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\mercado_livre.xlsx', index=False) 

    #AVISO 
    print('****************** O ARQUIVO FOI BAIXADO *************************')

    #Inicio MERCADO LIVRE 
    print("************************* INICIALIZANDO MAGALU **********************")

    #Fazendo a função 
    magazine_search_links()

    #Pegando todos os atributos 
    for url in tqdm(magazine_urls):
        magazine_search_attributes(url)

    #Criando o DataFrame 
    Dataset_magalu = pd.DataFrame()

    #Colocando os resultados na coluna
    Dataset_magalu['Urls'] = magazine_urls
    Dataset_magalu["Sellers"] = magazine_sellers
    Dataset_magalu["Preço"] = magazine_price
    Dataset_magalu["Loja"] = 'MAGAZINE LUIZA'
    
    #Fazendo a limpeza de espaços dentro dos sellers 
    Dataset_magalu['Sellers'] = Dataset_magalu['Sellers'].str.replace(" ","",1)

    #Item
    Dataset_magalu['Item'] = Dataset_magalu['Urls'].apply(limpeza)

    #Exportando o Dataset 
    Dataset_magalu.to_excel(r"C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\magalu.xlsx", index=False)

    #AVISO 
    print("*********************************** INICIALIZANDO SHOPEE ****************************")

    #Fazendo a função 
    shopee_urls()

    #Pegando os atributos e abrindo as páginas
    for url in tqdm(shopee_products_links):
        shopee_search_attributes(url)

    #Criando o dataset 
    dataset_shopee = pd.DataFrame()

    #Colocando os resultados na coluna
    dataset_shopee['Urls'] = shopee_urls
    dataset_shopee['Seller'] = shopee_seller
    dataset_shopee['Price'] = shopee_price

    #Item
    dataset_shopee['Item'] = dataset_shopee['Urls'].apply(limpeza)

    #exportando o dataset 
    dataset_shopee.to_excel(r"C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\shopee.xlsx", index=False)

    #AVISO 
    print("-=------------------ INICIANDO EXTRA --------------------")

    #Fazendo extra função base 
    extra_search_urls()

    #Fazendo a função para cada url de produto 
    for url in tqdm(extra_urls):
        extra_search_attributes(url)

    #Criando o dataset 
    dataset_extra = pd.DataFrame()

    #Colocando as informações dentro do dataframe 
    dataset_extra['Urls'] = extra_urls + extra_urls_ofertas
    dataset_extra['Seller'] = extra_sellers + extra_sellers_ofertas
    dataset_extra['Price'] = extra_price + extra_price_ofertas

    #Item
    dataset_extra['Item'] = dataset_extra['Urls'].apply(limpeza)

    #Exportando 
    dataset_extra.to_excel(r"C:\Users\pedro\Documents\FIVE-C\Automation\Urls\Scraper - Zhiyun\downloads\extra.xlsx", index=False)