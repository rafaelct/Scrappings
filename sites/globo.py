import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys

def executa() :

    strResultado = []
    linhas = ""
    
  
    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies

    
    
    # carrega a pagina
    browser.open('https://www.globo.com')
    pagina = browser.response().read()  # pega o HTML 
    print(pagina)
    print("###################################################")

    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all(True,{'class':'hui-premium'})
    #codigo = soup.find_all(True,{"class":"titulo"})

    #print(dir(codigo))
    #print(codigo.text)
    #exit(0)

    strResultado.append(linhas)
    for item in codigo :
        #print("Item:")
        #print(item)
        #print("-----------")
        print("Titulo:")
        print(item.find(class_='hui-premium__title').text)
        print("-----------")
        print('Link:')
        print(item.find(class_='hui-highlight__link')['href'])
        print("-----------")
        print("Sub-Titulo:")
        print(item.find(class_='hui-premium__related-title')['title'])
        print("-----------")
        print('Sub-Link:')
        print(item.find(class_='hui-premium__related-title')['href'])
        print("*************************************************************")
        
        #print(item.find(class_='hui-premium__title'))
        
        #print(codigo2)
        #for it in codigo2:
        #    print(it)

        #titulo = item.text.split('\t')[4].split('\r')[0]
        #valor = item.text.split('\t')[-3]
        #linhas = titulo+" - "+ valor
        #strResultado.append(linhas)

    exit(0)

    #codigo = soup.find_all(True,{"class":"box-tecnologias"})
    codigo = soup.findAll(class_='box-tecnologias')

    #print(codigo)

    linhas = "Tecnologias:\n"
    strResultado.append(linhas)

    for item in codigo :

        listTec = item.findAll(class_='tags')
        #print(listTec)
        for tec in listTec :
            linhas =tec.text
            strResultado.append(linhas)
    return strResultado


if __name__ == '__main__' :
    
    #if len(sys.argv) < 3 :
    #    print("Falta argumentos:")
    #    print("Uso: "+sys.argv[0]+" <login> <senha>")
    #    exit(1)

    #login = sys.argv[1]
    #senha = sys.argv[2]
    
    retorno = executa()

    for linha in retorno :
        print(linha)

