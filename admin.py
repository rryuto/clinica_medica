import json
import funcoes as f

usuarios = f.ler_json("usuarios.json")
medicos = f.ler_json("medicos.json")
pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")

# USUARIOS ===========================================================================================================

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
            print(f"iD: {dic['id']} - Usuario: {dic['usuario']} - Nivel: {dic['nivel']}")
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


#MEDICOS ===========================================================================================================

#cadastrar medicos
def cadastrar_medico():
    nome = input(f"Nome: ")
    especialidade = input(f"Especialidade: ")
    crm = input(f"CRM: ")

    novo_medico = {"id": f.novo_id(medicos),
                    "nome": nome,
                    "especialidade": especialidade,
                    "crm": crm}

    medicos.append(novo_medico)

    f.salvar_json("medicos.json", medicos)
    print("Medico cadastrado com sucesso.")

#listar medicos
def listar_medicos():
    if not medicos:
        print("Nenhum medico cadastrado.")
    else:
        for dic in medicos:
            print(f"iD: {dic['id']} - Nome: {dic['nome']} - Especialidade: {dic['especialidade']} - CRM: {dic['crm']}")
        print("\n")

#excluir medicos
def excluir_medico():
    print("Deseja excluir pelo nome ou iD?")
    print("1. Nome")
    print("2. iD")
    op = int(input())

    if op == 1:
        nome = input("Qual medico deseja excluir? ")
        encontrado = False
        f.excluir_por_nome(medicos, nome)

        if encontrado:
            f.salvar_json("medicos.json", medicos)
            print("Medico excluido com sucesso.")
        else:
            print("Medico nao existe no banco de dados.")

    elif op == 2:
        id = int(input("Qual iD deseja excluir? "))
        encontrado = False
        for i in medicos:
            if i["id"] == id:
                medicos.remove(i)
                encontrado = True
                break

        if encontrado:
            f.salvar_json("medicos.json", medicos)
            print("Medico excluido com sucesso.")
        else:
            print("Medico nao existe no banco de dados.")

#editar medicos
def editar_medico():
    id = int(input("iD do medico: "))
    encontrado = False
    for i in medicos:
        if i["id"] == id:
            print(i)
            encontrado = True
            break

    if not encontrado:
        print("Medico nao encontrado.")
        return

    print("Qual informacao deseja editar?")
    print("1. Nome")
    print("2. Especialidade")
    print("3. CRM")
    op = input()

    if op == '1':
        novo_nome = input("Novo nome: ")
        for i in medicos:
            if i["id"] == id:
                i["nome"] = novo_nome
    elif op == '2':
        nova_especialidade = input("Nova especialidade: ")
        for i in medicos:
            if i["id"] == id:
                i["especialidade"] = nova_especialidade
    elif op == '3':
        novo_crm = input("Novo CRM: ")
        for i in medicos:
            if i["id"] == id:
                i["crm"] = novo_crm

    f.salvar_json("medicos.json", medicos)
    print("Medico editado com sucesso.")

#menu medicos
def menu_medicos():
    print("-- MEDICOS --")
    print("1. Cadastrar medicos")
    print("2. Editar medicos")
    print("3. Excluir medicos")
    print("4. Listar medicos cadastrados")
    op = input()

    if op == '1':
        cadastrar_medico()
    elif op == '2':
        editar_medico()
    elif op == '3':
        excluir_medico()
    elif op == '4':
        listar_medicos()

#MENU USUARIOS
def menu_usuarios():
    print("-- USUARIOS --")
    print("1. Cadastrar usuarios do sistema")
    print("2. Editar usuarios")
    print("3. Excluir usuarios")
    print("4. Resetar senha de usuarios")
    print("5. Listar todos os usuarios")
    op = input()
    
    if op == '1':
        cadastro_usuario()
    elif op == '2':
        editar_usuario()
    elif op == '3':
        excluir_usuarios()
    elif op == '4':
        resetar_senha()
    elif op == '5':
        listar_usuarios()

#PACIENTES ===========================================================================================================

def visualizar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for dic in pacientes:
            print(f"iD: {dic['id']} - Nome: {dic['nome']} - Idade: {dic['idade']} - CPF: {dic['cpf']} - Telefone: {dic['telefone']} - Endereco: {dic['endereco']}")
        print("\n")

def buscar_paciente():
    print("Qual paciente deseja buscar?")
    nome = input()
    for i in pacientes:
        if i["nome"].lower() == nome.lower():
            print(i)
            break
    else:
        print("Paciente nao encontrado.")

def historico_completo():
    if not consultas:
        print("Nenhuma consulta realizada.")
    else:
        for dic in consultas:
            print(f"iD: {dic['id']} - Paciente: {dic['paciente']} - Medico: {dic['medico']} - Data: {dic['data']} - Hora: {dic['hora']}")
        print("\n")

def menu_pacientes():
    print("-- PACIENTES --")
    print("1. Visualizar todos os pacientes")
    print("2. Buscar pacientes")
    print("3. Ver histórico completo")
    op = input()
    
    if op == '1':
        visualizar_pacientes()
    elif op == '2':
        buscar_paciente()
    elif op == '3':
        historico_completo()

#CONSULTAS ===========================================================================================================

def visualizar_consultas():
    if not consultas:
        print("Nenhuma consulta realizada.")
    else:
        for dic in consultas:
            print(f"iD: {dic['id']} - Paciente: {dic['paciente']} - Medico: {dic['medico']} - Data: {dic['data']} - Hora: {dic['hora']}")
        print("\n")

def visualizar_consultas_medico():
    print("Qual medico deseja visualizar as consultas?")
    id_medico = int(input("iD do medico: "))
    for i in consultas:
        if i["id_medico"] == id_medico:
            print(i)
            break

def menu_consultas():
    print("-- CONSULTAS --")
    print("1. Visualizar todas as consultas")
    print("2. Visualizar consultas de um medico")
    op = input()
    
    if op == '1':
        visualizar_consultas()
    elif op == '2':
        visualizar_consultas_medico()

#MAIN ADMIN ===========================================================================================================
def main_admin():
    print("-- ADMIN --")
    print("1. Usuarios")
    print("2. Médicos")
    print("3. Pacientes")
    print("4. Consultas")
    print("5. Relatórios")
    op = input()

    if op == '1':
        menu_usuarios()
    elif op == '2':
        menu_medicos()
    elif op == '3':
        menu_pacientes()
    elif op == '4':
        menu_consultas()
    elif op == '5':
        menu_relatorios()

main_admin()