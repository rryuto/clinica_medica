import json
import funcoes as f

usuarios = f.ler_json("usuarios.json")

def retorna_nivel():
    escolha = False
    while escolha == False:
        print("Qual o nivel do usuario?")
        print("1. para Administrador")
        print("2. para Recepcionista")
        print("3. para Medico")
        nivel = int(input())
        if nivel == 1:
            nivel = "admin"
            escolha = True
        elif nivel == 2:
            nivel = "recepcionista"
            escolha = True
        elif nivel == 3:
            nivel = "medico"
            escolha = True
        else:
            print(f"Escolha nao compativel, escolha entre 1-3")
    
    return nivel

#cadastrar usuarios
def cadastro_usuario():
    usuario = input(f"Usuario: ")
    senha = input(f"Senha: ")
    nivel = retorna_nivel()

    novo_usuario = {"id": f.novo_id(usuarios),
                    "usuario": usuario,
                    "senha" : senha,
                    "nivel" : nivel}

    usuarios.append(novo_usuario)

    f.salvar_json("usuarios.json", usuarios)
    print("Usuario cadastrado com sucesso.")

#listar usuarios
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado")
    else:
        for dic in usuarios:
            print(f"iD: {dic["id"]} - Usuario: {dic["usuario"]} - Nivel: {dic["nivel"]}")
        print("\n")

#excluir usuarios
def excluir_usuarios():
    print("Deseja excluir pelo usuario ou iD?")
    print("1. Usuario")
    print("2. iD")
    op = int(input())

    if op == 1:
        print("Qual usuario deseja excluir? ")
        usuario = input()
        encontrado = False
        for i in usuarios:
            if i["usuario"].lower() == usuario.lower():
                usuarios.remove(i)
                encontrado = True
                break

        if encontrado:
            f.salvar_json("usuarios.json", usuarios)
            print("Usuario excluido com sucesso.")
        else:
            print("Usuario nao existe no banco de dados.")
        
    elif op == 2:
        id = int(input("Qual iD deseja excluir? "))
        encontrado = False
        for i in usuarios:
            if i["id"] == id:
                usuarios.remove(i)
                encontrado = True
                break
        if encontrado:
            f.salvar_json("usuarios.json", usuarios)
            print("Usuario excluido com sucesso.")
        else:
            print("Usuario nao existe no banco de dados.")

#editar usuarios
def editar_usuario():
    print("Qual usuario deseja editar?")
    id = int(input("iD do usuario: "))
    for i in usuarios:
        if i["id"] == id:
            print(i)
            break
        else:
            print("i")
    print("Qual informacao deseja editar?")
    print("1. Usuario")
    print("2. Senha")
    print("3. Nivel de acesso")
    op = input()

    if op == '1':
        novo_usuario = input("Novo usuario:")
        for i in usuarios:
            if i["id"] == id:
                i["usuario"] = novo_usuario
    elif op == '2':
        nova_senha = input("Nova senha:")
        for i in usuarios:
            if i["id"] == id:
                i["senha"] = nova_senha
    elif op == '3':
        novo_nivel = retorna_nivel()
        
        for i in usuarios:
            if i["id"] == id:
                i["nivel"] = novo_nivel

    f.salvar_json("usuarios.json", usuarios)

#resetar senha do usuario
def resetar_senha():
    print("Qual usuario deseja resetar a senha?")
    print("iD do usuario: ")
    id = int(input())
    for i in usuarios:
        if i["id"] == id:
            i["senha"] = ""

    f.salvar_json("usuarios.json", usuarios)

while True:
