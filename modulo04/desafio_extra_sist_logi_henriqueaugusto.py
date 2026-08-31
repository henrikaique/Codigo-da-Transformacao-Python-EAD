# essa parte do código cria a bibilhoteca de usuários.
usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}


# Esse bloco tem uma função que valida o login do usuário, procurando na bibilhoteca.
def validar_login(nome_usuario, senha_digitada):
   
    if nome_usuario in usuarios:
      
        if usuarios[nome_usuario] == senha_digitada:
            return True 
        else:
            return False 
    else:
        return False 

# essa parte do código é a parte de login de usuário onde ele digita o nome pode fechar o programa digitando sair e pode digitar a senha.
while True:
    print("\n--- Sistema de Login ---")
    nome_usuario = input("Digite seu nome de usuário (ou 'sair' para fechar): ")
    
    
    if nome_usuario.lower() == 'sair':
        print("👋 Fechando o programa. Até mais!")
        break
    
    senha_digitada = input("Digite sua senha: ")

 # esse bloco do código serve para validar o login do usuário e verificar se ele escreveu certo no sistema.
    if validar_login(nome_usuario, senha_digitada):
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {nome_usuario}!")
        break # O login deu certo, então saímos do loop.
    else:
        print("\n❌ Login inválido. Tente novamente.")
