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

historico_temas = []
historico_numero_noticias = []

while True:

    print("===========================")
    print("MENU NEWS API")
    print('\n- Digite "0" para sair')
    print('- Digite "1" para iniciar busca')
    print("===========================")

    escolha_menu = input("#>")

    if escolha_menu == "0":
        print("\n")
        print("Temas que foram escolhidos:")

        for temas in historico_temas:
            print(f"- {temas}")

        print("\n")
        print(f"Numero de notícias chamadas: {sum(historico_numero_noticias)}")

        print("saindo...")
        quit()

    if escolha_menu == "1":

        escolha_tema = input("Digite qual o tema das notícias que você deseja: ")
        numero_noticias = int(input("Digite o número de notícias que você deseja receber(Até 10 notícias): "))

        if numero_noticias >= 1 and numero_noticias <= 10:
            params = {
                "q" : escolha_tema,
                "language" : "pt"}
        else:
            print("Numero de notícias incorreto, tente novamente!")
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

        for artigo in resposta_json["articles"][:numero_noticias]:
            print("\n")
            print(f'Título da noícia: {artigo["title"]}')
            print(f'Fonte de notícia: {artigo["url"]}')
            print(f'Autor da noícia: {artigo["author"]}')

        


        


