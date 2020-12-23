import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys

#senha = sys.argv[2]

def busca_mercadolivre(txt) :
        
    strBusca = txt.replace(' ','-')


    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies
    browser.set_handle_robots(False)

    # carrega a pagina
    browser.open('https://lista.mercadolivre.com.br/'+strBusca)

    # carrega a pagina do perfil logado

    pagina = browser.response().read()  # pega o HTML 

    #print(pagina)
    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all(True,{"class":"ui-search-result__content ui-search-link"})

    if len(codigo) == 0 :
        codigo = soup.find_all(True,{"class":"item__info"})
     
    #print(codigo)

    strResultado = ""
    listaResultado = []
    
    for dados in codigo :
        print("---------------------------------")
        print(dados.find(class_='ui-search-item__group ui-search-item__group--title').text)
        nomeProduto = dados.find(class_='ui-search-item__group ui-search-item__group--title').text
        precoProduto = ""

            #print(dados.find(class_='item__price').find(class_='price__symbol').text)
        precoProduto = dados.find(class_='ui-search-price ui-search-price--size-medium ui-search-item__group__element')
            #precoValorProduto = dados.find(class_='item__price').find(class_='price__fraction').text
        print("Preço do produto:")
        simboloMoeda = dados.find(class_="price-tag-symbol").text
        preco = dados.find(class_="price-tag-fraction").text
        
        try:
            centavos = dados.find(class_="price-tag-cents").text
        except AttributeError :
            centavos = "00"

        precoProduto = simboloMoeda + " " + preco +","+centavos

        print(precoProduto)
        
        #nomeProduto = dados.text
        linkProduto = ""

        try:
            linkProduto = dados.get("href")

            if linkProduto is None :
                linkProduto = dados.find(class_='item__info-title').get("href")    
        except AttributeError :
            print(dados)
            #linkProduto = dados.find(class_='item__info-title').get("href")
        
        print(linkProduto)

        try:
            listaResultado.append( nomeProduto +"\n"+precoProduto+"\n"+linkProduto+"\n")
        except TypeError :
            #print(dados.find(class_='item__info-title').get("href"))
            pass
    return listaResultado


if __name__ == "__main__" :
    #print(sys.argv)
    if len(sys.argv) < 2 :
        print("Falta argumentos:")
        print("Uso: "+sys.argv[0]+" <busca+produto>")
        exit(1)

    txt = ""

    for argumento in sys.argv[1:] :
        txt += argumento+" "

    busca_mercadolivre(txt[0:-1])


