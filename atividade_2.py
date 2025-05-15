import requests
import os
import time

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

def mostrar_menu_login():
    demarcacao_menu()
    print("Bem vindo ao Jsonplaceholder.Net")
    demarcacao_menu()
    print('- Para sair digite "0"')
    print('- Para efetuar o login digite "1"')
    print('- Para efetuar o cadastro digite "2"')
    demarcacao_menu()
        
def efetuar_login():
    global Menu_aplicação, Menu_login

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
        
    limpar_terminal()
def efetuar_cadastro():
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

def mostrar_comentarios():
    global qtd_coments_visu

    resposta_api = requests.get('https://jsonplaceholder.typicode.com/comments?_limit=5')
    comentarios = resposta_api.json()
    qtd_coments_visu += len(comentarios) 

    for comentario in comentarios:
        print("\n")
        demarcacao_menu()
        print("Nome do usuario: ", comentario["name"])
        print(f'\nConteúdo do comentário: \n{comentario["body"]}')
        demarcacao_menu()

def mostrar_posts():
    global qtd_posts_visu

    resposta_api_2 = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=5')
    posts = resposta_api_2.json()
    qtd_posts_visu += len(posts)
        
    print("\n* POSTS *")
        
    for post in posts:
        print("\n")
        demarcacao_menu()
        print("Título do post: ", post["title"])
        print(f'\nConteúdo do post: \n{post["body"]}' )
        demarcacao_menu()

def mostrar_menu_aplicacao():
    demarcacao_menu()
    print('- Digite "0" para sair (Voltar ao menu)')
    print('- Digite "1" para visualizar seus próprios posts')
    print('- Digite "2" para filtrar posts por algum outro usuário')
    print('- Digite "3" para criar um novo post')
    print('- Digite "4" para visualizar comentários')
    print('- Digite "5" para visualizar posts públicos')
    demarcacao_menu()

def sair_menu_aplicacao():
    global Menu_aplicação, Menu_login

    limpar_terminal()
    demarcacao_menu()
    print("Resumo da sessão:")
    demarcacao_menu()
    print(f"- Comentários visualizados: {qtd_coments_visu}")
    print(f"- Posts visualizados: {qtd_posts_visu}")
    print(f"- Posts criados: {qtd_posts_criados}")
    demarcacao_menu()
    input("Pressione Enter para sair do menu...\n#>")
    limpar_terminal()
    Menu_aplicação = False
    Menu_login = True

def filtro_post():
    usuario_escolhido = input("Digite o numero do usuário que você ver:")

    post_usuario_escolhido = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={usuario_escolhido}&_limit=5')
    usuario_escolhido_resposta = post_usuario_escolhido.json()

    limpar_terminal()

    print(f"\n* POSTS DO USUARIO {usuario_escolhido} *\n")
    demarcacao_menu()
    try:
        for post in usuario_escolhido_resposta:
            print("Título do post: ", post["title"])
            print(f'\nConteúdo do post: \n{post["body"]}' )
            qtd_posts_visu += 1
                
    except:
            print("Nenhum post encontrado")
    demarcacao_menu()
    input("#>")

def criar_post():
    global qtd_posts_criados

    novo_post = {
        "titulo": "",
        "conteudo": "",
        "userId": int(banco_usuario["id"])
        }

    limpar_terminal()
    demarcacao_menu()
    print(" * Criação de um novo post *")
    demarcacao_menu()
    titulo_post = input("Digite um título para o seu post:")
    conteudo_post = input("Digite um conteúdo para o seu post:")

    novo_post["titulo"] = titulo_post
    novo_post["conteudo"] = conteudo_post

    # Salva localmente
    posts_criados_usuario.append(novo_post)
    qtd_posts_criados += 1 

    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("\nPost efetuado com sucesso!!")
    time.sleep(2)

def mostrar_posts_usuario():
    if posts_criados_usuario:
        for post in posts_criados_usuario:
            print(f'Título do post: {post["titulo"]}')
            print(f'\nConteúdo do post: \n{post["conteudo"]}')
            demarcacao_menu()
        input("#>")
    else:
        print("Você ainda não criou nenhum post!")
        demarcacao_menu()
        input("#>")

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

posts_criados_usuario = []



while True:
    while Menu_login:
        mostrar_menu_login()
        escolha_menu = input("#>")

        if escolha_menu == "0":
            print("Saindo...")
            quit()

        if escolha_menu == "1":
            efetuar_login()
            continue
        if escolha_menu == "2":
            efetuar_cadastro()
            continue

    while Menu_aplicação:
        
        limpar_terminal()
        demarcacao_menu()
        print("Menu Jsonplaceholder.Net")
        demarcacao_menu()
        
        mostrar_menu_aplicacao()
        
        escolha_menu_programa = input("#>")

        if escolha_menu_programa == "0":
            sair_menu_aplicacao()

        if escolha_menu_programa == "1":
            limpar_terminal()
            print("* MEUS POSTS *\n")
            demarcacao_menu()
            mostrar_posts_usuario()
        

        if escolha_menu_programa == "2":
            
            filtro_post()

        if escolha_menu_programa == "3":
                
           criar_post()

        if escolha_menu_programa == "4":
            limpar_terminal()
            print("* COMENTÁRIOS *\n")
            mostrar_comentarios()
            input("#>")

        if escolha_menu_programa == "5":
            limpar_terminal()
            print("* POSTS PÚBLICOS *\n")
            mostrar_posts()
            input("#>")
