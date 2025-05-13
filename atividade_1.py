import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY_NEWS")

if not api_key:
    raise ValueError("API KEY não foi encontrada nas variáveis de ambiente")

url = "https://newsapi.org/v2/everything"

headers={
"X-Api-key": api_key
}

#Funções
def marcacao_menu():
    """

    """
    print("===========================")

def limpar_terminal():
    """

    """
    os.system("cls")

def menu():
    """

    """
    limpar_terminal()
    marcacao_menu()
    print("MENU NEWS API")
    print('\n- Digite "0" para sair')
    print('- Digite "1" para iniciar busca')
    marcacao_menu()

def sair_aplicacao():
    """

    """
    print("\n")
    print("Temas que foram escolhidos:")

    for temas in historico_temas:
        print(f"- {temas}")

    print("\n")
    print(f"Numero de notícias chamadas: {sum(historico_numero_noticias)}")

    print("\nsaindo...")
    quit()

def exibir_noticias():
    """

    """
    for artigo in resposta_json["articles"][:numero_noticias]:
            print("\n")
            print(f'Título da notícia: {artigo["title"]}')
            print(f'Fonte de notícia: {artigo["url"]}')
            print(f'Autor da noícia: {artigo["author"]}')
        
#Listas com os históricos de temas e numeros de notícias pesquisados.

historico_temas = []
historico_numero_noticias = []

#Loop principal da aplicação
while True:
    menu()

    escolha_menu = input("#>")

    if escolha_menu == "0":
        sair_aplicacao()

    if escolha_menu == "1":

        escolha_tema = input("Digite qual o tema das notícias que você deseja: ")

        #Loop de verificação do numero de notícias
        while True:
            try:
                numero_noticias = int(input("\nDigite o número de notícias que você deseja receber(Até 10 notícias): "))
            except ValueError:
                print("\nDigite apenas numero!")
                continue

            if numero_noticias >= 1 and numero_noticias <= 10:
                params = {
                    "q" : escolha_tema,
                    "language" : "pt"}
                break
            else:
                print("\nNumero de notícias incorreto, tente novamente!")
                continue

        historico_temas.append(escolha_tema)
        historico_numero_noticias.append(numero_noticias)

        resposta = requests.get(url=url, headers=headers, params=params)

        status_code = resposta.status_code

        if status_code == 200:
            resposta_json = resposta.json()

        else:
            print("Ocorreu algum erro, tente novamente!")
            continue
        
        exibir_noticias()
        
        input("#>")

        


        


