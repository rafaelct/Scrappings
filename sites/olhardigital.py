import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys


def busca_olhardigital() :
        
    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies
    browser.set_handle_robots(False)

    # carrega a pagina
    browser.open('https://olhardigital.com.br/')

    # carrega a pagina
    pagina = browser.response().read()  # pega o HTML 

    #print(pagina)
    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all("article")


     
    print(codigo)
    
    strResultado = ""
    listaResultado = []
    
    for dados in codigo :
        #print(dados)
        print("--------------------------------")
        print("Titulo da noticia:")
        print(dados.find("a")["title"] )
        print("Link da noticia:")
        print(dados.find("a")["href"] )
        print("Link da foto da noticia")
        print(dados.find("img")['src'])
        print("******************************************")

        nomeNoticia = dados.find("a")["title"]
        linkNoticia = dados.find("a")["href"]
        strResultado = nomeNoticia + "\n" + linkNoticia + "\n"
        listaResultado.append(strResultado)

    return listaResultado


if __name__ == "__main__" :
    
    busca_olhardigital()

    #for dados in retorno :
    #    print(dados)

