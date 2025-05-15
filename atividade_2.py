import requests
import os

def demarcacao_menu():
    '''
    Exibe uma linha visual de separação no terminal para melhorar a leitura do menu.
    '''
    print("==================================")

def limpar_terminal():
    """
    Limpa o terminal usando o comando apropriado para o sistema operacional(Windows).
    """
    os.system("cls")


Menu_login = True
Menu_aplicação = False
qtd_posts_visu = 0
qtd_coments_visu = 0
qtd_posts_criados = 0

banco_usuario = {
    "id" : "1",
    "email" : 0,
    "senha" : 0,
}

"""
Menu_inicial = True
Menu_cadastro = False
Menu_login = False
Menu_funcionamento = True
"""

while True:
    while Menu_login:
        demarcacao_menu()
        print("Bem vindo ao Jsonplaceholder.Net")
        demarcacao_menu()
        print('- Para sair digite "0"')
        print('- Para efetuar o login digite "1"')
        print('- Para efetuar o cadastro digite "2"')
        demarcacao_menu()
        escolha_menu = input("#>")

        if escolha_menu == "0":
            print("Saindo...")
            quit()

        if escolha_menu == "1":
            limpar_terminal()
            demarcacao_menu()
            print("Tela de login")
            demarcacao_menu()
            print("Para efetuar o login digite seu email e senha")
            email_login = input("\nEmail: ")
            senha_login = input("Senha: ")

            if email_login == banco_usuario["email"]:
                if senha_login == banco_usuario["senha"]:
                    Menu_login = False
                    Menu_aplicação = True
                else:
                    print("Sua senha está incorreta, tente novamente!")
            else:
                print("Seu email está incorreto, tente novamente!")
        if escolha_menu == "2":
            limpar_terminal()
            demarcacao_menu()
            print("Tela de cadastro")
            demarcacao_menu()
            print("Para se cadastrar, digite seu email e senha de usuario")
            email_usuario = input("\nDigite seu email:")
            senha_usuario = input("Digite sua senha:")

            banco_usuario["email"] = email_usuario
            banco_usuario["senha"] = senha_usuario

            print("\nUsuário cadastrado com sucesso!")
            input("\n#>")
            limpar_terminal()

    while Menu_aplicação:
        limpar_terminal()
        demarcacao_menu()
        print("Menu Jsonplaceholder.Net")
        demarcacao_menu()
        print("\n* COMENTÁRIOS *")
        
        resposta_api = requests.get('https://jsonplaceholder.typicode.com/comments?_limit=5')
        comentarios = resposta_api.json()

        for comentario in comentarios:
            print("\n")
            demarcacao_menu()
            print("Nome do usuario: ", comentario["name"])
            print(f'\nConteúdo do comentário: \n{comentario["body"]}')
            demarcacao_menu()

        resposta_api_2 = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=5')
        posts = resposta_api_2.json()
        
        print("\n* POSTS *")
        
        for post in posts:
            print("\n")
            demarcacao_menu()
            print("Título do post: ", post["title"])
            print(f'\nConteúdo do post: \n{post["body"]}' )
            demarcacao_menu()

        demarcacao_menu()
        print('- Digite "0" para sair (Voltar ao menu)')
        print('- Digite "1" para visualizar seus próprios posts')
        print('- Digite "2" para filtrar posts por algum outro usuário')
        print('- Digite "3" para criar um novo post')
        demarcacao_menu()
        escolha_menu_programa = input("#>")

        if escolha_menu_programa == "0":
            limpar_terminal()
            Menu_aplicação = False
            Menu_login = True

        if escolha_menu_programa == "1":
            
            post_usuario = requests.get(f'https://jsonplaceholder.typicode.com/posts/{banco_usuario["id"]}')
            posts_usuario_resposta = post_usuario.json()

            limpar_terminal()

            print("* MEUS POSTS *\n")
            demarcacao_menu()
            try:
                for post in posts_usuario_resposta:
                    print("Título do post: ", post["title"])
                    print(f'\nConteúdo do post: \n{post["body"]}' )
                
            except:
                    print("Nenhum post encontrado")
            demarcacao_menu()
        input("#>")

        if escolha_menu_programa == "2":
            
            usuario_escolhido = input("Digite o numero do usuário que você ver:")

            post_usuario_escolhido = requests.get(f'https://jsonplaceholder.typicode.com/posts/{usuario_escolhido}?_limit=5')
            usuario_escolhido_resposta = post_usuario_escolhido.json()

            limpar_terminal()

            print(f"* POSTS DO USUARIO {usuario_escolhido} *\n")
            demarcacao_menu()
            try:
                for post in usuario_escolhido_resposta:
                    print("Título do post: ", post["title"])
                    print(f'\nConteúdo do post: \n{post["body"]}' )
                
            except:
                    print("Nenhum post encontrado")
            demarcacao_menu()
        input("#>")