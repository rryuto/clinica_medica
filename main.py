import json
import funcoes as f

print("Bem Vindo\n")
#verificacao de login
while True:
    
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    nivel = f.login(usuario, senha)

    if nivel == "admin":
        import admin
        break
    elif nivel == "recepcionista":
        import recepcionista
        break
    elif nivel == "medico":
        import medico
        break
    else:
        print("Usuario nao cadastrado, tente denovo.\n")