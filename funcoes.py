import json

def ler_json(arquivo):
    with open(arquivo, "r") as f:
        return json.load(f)

def salvar_json(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=2)

def novo_id(lista):
    return lista[len(lista)-1]["id"] + 1

def menu_usuarioAdmin():
    
    print(" 1 - Cadastrar usuários do sistema ")
    print(" 2 - Editar usuários ")
    print(" 3 - Excluir usuários ")
    print(" 4 - Resetar senha de usuários ")
    print(" 5 - Listar todos os usuários ")

def menu_medicosAdmin():
    print(" 1 - Cadastrar médicos ")
    print(" 2 - Editar médicos ")
    print(" 3 - Excluir médicos cadastrados ")
    print(" 4 - Listar médicos cadastrados ")

def menu_pacientesAdmin():
    print(" 1 - Visualizar todos os pacientes ")
    print(" 2 - Buscar pacientes ")
    print(" 3 - Ver histórico completo ")

def menu_consultasAdmin():
    print(" 1 - Visualizar todas as consultas ")
    print(" 2 - Consultar agenda geral ")

def menu_relatoriosAdmin():
    print(" 1 - Total de consultas realizadas por período ")
    print(" 2 - Total de consultas canceladas ")
    print(" 3 - Quantidade de pacientes ")
    print(" 4 - Quantidade de médicos ativos ")
    print(" 5 - Consultas por médico ")
    print(" 6 - Atendimentos realizados no dia ")
    print(" 7 - Pacientes mais atendidos")

def menu_consultas():
    print(" 1 - Marcar consulta para médico específico ")
    print(" 2 - Escolher data e horário ")
    print(" 3 - Reagendar consulta ")
    print(" 4 - Cancelar consulta ")
    print(" 5 - Confirmar presença do paciente ")
    print(" 6 - Listar todas as consultas do dia ")
    print(" 7 - Listar consultas futuras ")

def id_existe(lista):
    id = int(input("iD do usuario: "))

    encontrado = False
    for i in lista:
        if i["id"] == id:
            encontrado = True
            break
    
    if not encontrado:
        print("Usuario nao encontrado!")
        return
    
    else:
        return encontrado