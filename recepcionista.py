import json
import funcoes as f
from datetime import date

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")

#PACIENTES ===========================================================================================================

def cadastro_paciente():
    paciente = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    cpf = str(input("Informe seu cpf: "))
    telefone = str(input("Informe seu número de contato: "))
    end = str(input("Informe seu endereço de residência: "))
    dic = {"id": f.novo_id(pacientes),
           "nome": paciente,
             "idade":idade,
             "cpf": cpf,
             "telefone": telefone,
             "endereco": end}
    pacientes.append(dic)
    f.salvar_json("pacientes.json", pacientes)
    
def editar_paciente():
    print("Qual paciente deseja editar: ")
    id = int(input("iD do Usuário: "))
    for i in pacientes:
        if i["id"] == id:
            print(i)
            break
        else:
            print("Esse paciente não está cadastrado!")
    print("Qual informação deseja editar: ")
    print(" 1 - Nome ")
    print(" 2 - Idade ")
    print(" 3 - CPF ") 
    print(" 4 - Telefone ")
    print(" 5 - Endereço ") 
    op = int(input("Escolha uma dessas opções: "))
    if op == 1:
        n_nome = input("Digite o novo nome: ")
        for i in pacientes:
            if i["id"] == id:
                i["nome"] = n_nome
    elif op == 2:
        nova_idade = input("Me informe a sua idade: ")
        for i in pacientes:
            if i["id"] == id:
                i["idade"] = nova_idade
    elif op == 3:
        novo_cpf = str(input("Digite seu novo CPF: "))
        for i in pacientes:
            if i["id"] == id:
                i["cpf"] = novo_cpf
    elif op == 4:
        novo_telefone = str(input("Digite seu novo número de contato: "))
        for i in pacientes:
            if i["id"] == id:
                i["telefone"] = novo_telefone
    elif op == 5:
        novo_end = str(input("Digite seu novo endereço: "))
        for i in pacientes:
            if i["id"] == id:
                i["endereco"] = novo_end
    else:
        print("Essa opção não existe, escolha as opções de 1 á 5!!")
    f.salvar_json("pacientes.json", pacientes)

def buscar_paciente_especifico():
    paciente = input("Digite o nome do paciente que você deseja buscar: ")
    
    for i in pacientes:
        if i["nome"].lower() == paciente.lower():
            print(f"iD: {i['id']} - Nome: {i['nome']} - Idade: {i['idade']} - CPF: {i['cpf']} - Telefone: {i['telefone']} - Endereço: {i['endereco']}")
            break
    else:
        print("Paciente não encontrado.")
    f.salvar_json("pacientes.json", pacientes)

def listar_pacientes():
    for i, valor in enumerate(pacientes):
        print(f"{valor["id"]} --- {valor["nome"]}")   

def Visuzlizar_dados_completos():
    print("Qual paciente deseja ver os dados?")
    id_paciente = input("iD do paciente: ")
    for i in pacientes:
        if i["id"] == id_paciente:
            print(f"ID: {i["id"]}")
            print(f"Nome: {i["nome"]}")
            print(f"CPF: {i["cpf"]}")
            print(f"Telefone: {i["telefone"]}")
            print(f"Endereco: {i["endereco"]}")
            break
    else:
        print(f"Paciente nao encontrado.")
    

def Menu_recepcionista_pacientes():
    print("========== PACIENTES ===========")
    print(" 1 - Cadastrar paciente ")
    print(" 2 - Editar paciente ")
    print(" 3 - Buscar paciente específico ")
    print(" 4 - Listar todos os pacientes ")
    print(" 5 - Visualizar dados completos ")
    print("================================")
    opção = int(input("Digite uma dessas opção: "))

    if opção == 1:
        cadastro_paciente()
    elif opção == 2:
        editar_paciente()
    elif opção == 3:
        buscar_paciente_especifico()
    elif opção == 4:
        listar_pacientes()
    elif opção == 5:
        Visuzlizar_dados_completos()
    else:
        print("Essa opção não existe, digite de 1 á 5!!")
#CONSULTAS ===========================================================================================================

#marcar consulta
def marcar_consulta():
    nome_paciente = input("Nome do paciente: ")
    id_paciente = f.id_paciente(pacientes, nome_paciente)
    print(f.listar_medicos())
    id_medico = int(input("Escolha um medico pelo iD: "))
    data = input("Data: ")
    hora = input("Hora: ")

    if f.validar_disponibilidade(consultas, id_medico, hora, data):
        if id_medico and id_paciente:
            nova_consulta = {"id": f.novo_id(consultas),
                            "id_paciente": id_paciente,
                            "id_medico": id_medico,
                            "data": data,
                            "hora": hora,
                            "status": "Agendada"}

            consultas.append(nova_consulta)
            f.salvar_json("consultas.json", consultas)
            print("Consulta agendada com sucesso.")
        else:
            print("Medico ou paciente nao encontrado.")
    else:
        print("Horario nao disponivel.")

def reagendar_consulta():
    print("Qual consulta deseja reagendar: ")
    id = int(input("iD da consulta: "))
    existe = False
    for i in consultas:
        if i["id"] == id:
            print(f"iD: {i['id']} - Paciente: {i['id_paciente']} - Medico: {i['id_medico']} - Data: {i['data']} - Hora: {i['hora']} - Status: {i['status']}")
            existe = True
            break
    else:
        print("Consulta não encontrada.")
    if existe:
        for i in consultas:
            if i["id"] == id and (i["status"] == "Agendada" or i["status"] == "Cancelada"):
                print("Informe as informacoes do reagendamento: ")
                nova_data = input("Nova data: ")
                novo_horario = input("Novo horario: ")
                i["data"] = nova_data
                i["hora"] = novo_horario
                f.salvar_json("consultas.json", consultas)
                break
        else:
            print("Status da consulta nao permite reagendamento.")

def cancelar_consulta():
    print("Cancelamento da consulta")
    id = int(input("Informe o iD da consulta: "))
    for i in consultas:
        if i["id"] == id:
            if i["status"] == "Agendada":
                i["status"] = "Cancelada"
                f.salvar_json("consultas.json", consultas)
                break
            else:
                print("Status da consulta nao esta como agendada.")
def confirmar_consulta():
    id = int(input("Qual consulta deseja confirmar?"))
    if f.buscar_id(consultas, id):
        for i in consultas:
            if i["status"] == "Agendada":
                i["status"] = "Confirmada"
                break
    else:
        print("Consulta nao existe no sistema.")

def consultas_hoje(): 
    hoje = date.today()
    existe = False
    for i in consultas:
        if hoje.strftime("%d/%m/%Y") == i["data"] and (i["status"] == "Agendada" or i["status"] == "Confirmada"):
            print(f"ID: {i['id']} - ID do paciente: {i['id_paciente']} - ID do medico: {i['id_medico']} - Hora: {i['hora']}")
            existe = True
    if not existe:
        print("Nao ha consultas hoje.")

def Menu_Consultas_recepcionista():
    print("================ CONSULTAS =================")
    print(" 1 - Marcar consulta para médico específico ")
    print(" 2 - Reagendar consulta ")
    print(" 3 - Cancelar Consulta ")
    print(" 4 - Confirmar presença do paciente ")
    print(" 5 - Listar todas as consultas ")
    print(" 6 - Listar consultas futuras ")
    print("==============================================")




while True:
    Menu_Consultas_recepcionista()
    opção = int(input("Digite uma dessas opção: "))
    if opção == 1:
        marcar_consulta()
    elif opção == 2:
        reagendar_consulta()
    elif opção == 3:
        cancelar_consulta()
    elif opção == 4:
        confirmar_consulta()
    elif opção == 5:
        consultas_hoje()