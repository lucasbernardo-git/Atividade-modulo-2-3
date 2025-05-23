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
    Exibe uma linha visual de separação no terminal para melhorar a leitura do menu.
    """
    print("===========================")

def limpar_terminal():
    """
    Limpa o terminal usando o comando apropriado para o sistema operacional(Windows).
    """
    os.system("cls")

def menu():
    """
    Exibe o menu principal da aplicação com as opções disponíveis para o usuário.
    """
    limpar_terminal()
    marcacao_menu()
    print("MENU NEWS API")
    print('\n- Digite "0" para sair')
    print('- Digite "1" para iniciar busca')
    marcacao_menu()

def sair_aplicacao():
    """
    Finaliza a aplicação exibindo o histórico de temas pesquisados e o número total de notícias chamadas.
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
    global numero_noticias
    """
    Exibe as notícias obtidas da API, respeitando a quantidade definida em "numero_noticias".
    Cada notícia mostra o título, a URL da fonte e o autor.
    
    Requer:
        resposta_json (dict): JSON de resposta da API com a chave "articles".
    """
    for artigo in resposta_json["articles"][:numero_noticias]:
            print("\n")
            print(f'Título da notícia: {artigo["title"]}')
            print(f'Fonte de notícia: {artigo["url"]}')
            print(f'Autor da noícia: {artigo["author"]}')
    
def inputs_noticia():
    """
    Solicita ao usuário o tema da pesquisa e a quantidade de notícias desejadas (1 a 10).
    Atualiza os parâmetros da requisição e registra os históricos de temas e quantidades.
    
    Try/Except:
        ValueError: Se o valor informado para quantidade não for um número válido.
    """
    global params, numero_noticias

    escolha_tema = input("Digite qual o tema das notícias que você deseja: ")
    historico_temas.append(escolha_tema)

    #Loop de verificação do numero de notícias
    while True:
        try:
            numero_noticias = int(input("\nDigite o número de notícias que você deseja receber(Até 10 notícias): "))

        except ValueError:
            print("\nDigite apenas numero!")
            continue

        if numero_noticias >= 1 and numero_noticias <= 10:
            historico_numero_noticias.append(numero_noticias)
            params = {
                    "q" : escolha_tema,
                    "language" : "pt"}
            break
        else:
            print("\nNumero de notícias incorreto, tente novamente!")
            continue

numero_noticias = 0

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

        inputs_noticia()

        resposta = requests.get(url=url, headers=headers, params=params)

        status_code = resposta.status_code

        if status_code == 200:
            resposta_json = resposta.json()

        else:
            print("Ocorreu algum erro, tente novamente!")
            continue
        
        exibir_noticias()
        
        input("#>")