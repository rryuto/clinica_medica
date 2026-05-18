import json
import admin
import recepcionista
import medico
import funcoes as f

print("Bem Vindo\n")
#verificacao de login
while True:
    
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    nivel = f.login(usuario, senha)

    if nivel == "admin":
        admin.main_admin(usuario)
        break
    elif nivel == "recepcionista":
        recepcionista.recepcionista_open()
        recepcionista.menu_principal()
        break
    elif nivel == "medico":
        main_medico()
        break
    else:
        print("Usuario nao cadastrado, tente denovo.\n")