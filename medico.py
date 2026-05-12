import json
import funcoes as f
from datetime import datetime
from datetime import date

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")
medicos = f.ler_json("medicos.json")
prontuarios = f.ler_json("prontuarios.json")

#Agenda
def Listar_consultas_para_medico_especifico():
    medico = input("Digite o seu nome Doutor: ")
    id_medico = f.id_paciente(medicos, medico)
    if id_medico:
        for i in consultas:
            if i["id_medico"].lower() == id_medico.lower() and (i["status"] == "Agendada" or i["status"] == "Confirmada"):
                print(f"Essas são as consultas marcadas para você {i}")
    else:
        print(f"Esse médico não existe.")

def Visualisar_agenda_diaria():
    doutor = input("Digite o seu nome Doutor: ")
    id = f.id_paciente(medicos,doutor)
    if id:
        data_hj = str(input("Qual a data que voce quer saber?, use como formato de exemplo isso (DD/MM/AAAA): "))
        for i in consultas:
            if data_hj == i["data"]:
                print(f"Essas são consultas para esse dia {i}")
    else:
        print("Você não é um médico cadastrado.")

def Visualizar_agenda_futura():
    doutor = input("Digite seu nome Doutor: ")
    id = f.id_paciente(medicos, doutor)
    hoje = datetime.today()
    if id:
        for i in consultas:
            if datetime.strptime(i["data"], "%d/%m/%Y").timestamp() > hoje.timestamp():
                print(f"{i}")


#Atendimento
def Iniciar_Atendimento():
    consulta_especifica = input("Qual o nome do paciente que você deseja iniciar o atendimento? ")
    id = f.id_paciente(pacientes, consulta_especifica)
    if id:
        iniciar = input("Você quer iniciar o atendimento?(Responda sim ou não) ")
        if iniciar == "sim":
            for i in consultas:
                if i["status"] == "Confirmada":
                    i["status"] = "Em Atendimento"
                    print("Você iniciou o atendimento.")
        elif iniciar == "não":
            print("Tranquilo então.")
        else:
            print("Essã opção não existe, digite sim ou não.")
        f.salvar_json("consultas.json", consultas)
    else:
        print("Você não esta cadastrado.")

def Finalizar_Atendimento():
    consulta_especifica = input("Qual o nome do paciente que você deseja finalizar o atendimento? ")
    id = f.id_paciente(pacientes, consulta_especifica)
    if id:
        finalizar = input("Você quer finalizar o atendimento?(Responda sim ou não) ")
        if finalizar == "sim":
            for i in consultas:
                if i["status"] == "Em Atendimento":
                    i["status"] == "Finalizada"
                    print("Você finalizou o atendimento.")
        elif finalizar == "não":
            print("Tranquilo então.") 
        else:
            print("Essã opção não existe, digite sim ou não.")   
        f.salvar_json("consultas.json", consultas) 
    else:
        print("Voce não esta cadastrado.")    

def Menu_Agenda_Medico():
    print(" 1 - Listar apenas consultas marcadas para ele ")
    print(" 2 - Visualizar agenda diária ")
    print(" 3 - Visualizar agenda futura ")

def Atendimento():
    print(" 1 - Iniciar atendimento ")
    print(" 2 - Finalizar atendimento ")


#Prontuário/Laudo
def Laudo_Medico():
    doutor = input("Qual o nome do médico que deseja fazer o Laudo Médico? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        for i in consultas:
            if i["status"] == "Em Atendimento":
                nome_paciente = input("Qual o nome do paciente que necessita de um Laudo? ")
                data = str(input("Quando o voce deseja fazer a consulta do Laudo? Use como exemplo esse: DD/MM/AAAA "))
                medico_responsavel = input("Qual médico será resposável por fazer o Laudo? ")
                Diagnostico = input("Qual o diagnóstico final do paciente? ")
                receita = input("Qual a receita médica á ser passado? ")
                observacoes = input("Quais são as observações que devem ser passadas ao paciente? ")
                dic = {"id" : f.novo_id(prontuarios)
                        ,"id_paciente" : f.id_paciente(pacientes,nome_paciente)
                        , "id_medico" :f.id_paciente(medicos, medico_responsavel)
                        , "data" : data
                        , "diagnostico" : Diagnostico
                        , "receita" : receita
                        , "observacoes" : observacoes}
                prontuarios.append(dic)
        f.salvar_json("prontuarios.json", prontuarios)
    else:
        print("Você não é um médico cadastrado.")

#Histórico Médico
def buscar_paciente_por_nome():
    doutor = input("Qual o nome do doutor que está procurando o paciente? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        paciente = input("Qual o nome do paciente que você deseja saber as informações?")
        for i in pacientes:
            if i["nome"] == paciente:
                print(f"{i}")
                break
            else:
                print("Esse paciente não existe.")
                break
    else:
        print("Você não está cadastrado.")

def Ver_historico_de_consultas_anteriores():
    doutor = input("Qual o nome do médico que deseja ver o histórico dos pacientes? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        paciente = input("Qual o nome do paciente que você deseja saber sobre o histórico de consultas? ")
        for i in pacientes:
            if i["nome"] == paciente:
                for x in consultas:
                    id = f.id_paciente(pacientes,paciente)
                    if id == x["id_paciente"]:
                        print(f" iD: {x["id"]} - iD do paciente: {x["id_paciente"]} - iD do médico: {x["id_medico"]} - Data da consulta: {x["data"]} - Hora da consulta: {x["hora"]} - status da consulta: {x["status"]} ")
    else:
        print("Você não está cadastrado.")

def ver_prontuarios_anteriores_do_paciente():
    doutor = input("Qual o nome do médico que deseja ver o histórico dos prontuários do pacientes? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        paciente = input("Qual o nome do paciente que você deseja saber sobre o histórico de seus prontuários? ")
        for i in pacientes:
            if i["nome"] == paciente:
                for x in prontuarios:
                    id = f.id_paciente(pacientes,paciente)
                    if id == x["id_paciente"]:
                        print(f"iD: {x["id"]} - iD do paciente: {x["id_paciente"]} - Data: {x["data"]} - Dignóstico final: {x["diagnostico"]} - Receita: {x["receita"]} - Observções para o paciente: {x["observacoes"]}")
    else:
        print("Você não está cadastrado.")

#Relatórios
def Total_de_atendimentos():
    doutor = input("Qual o nome do médico que deseja saber sobre seus atendimentos? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        for i in consultas:
            if i["id_medico"] == id and i["status"] == "Finalizada":
                print(f"""
        Consulta feitas por você
        ---------
        ID da consulta: {i['id']}
        Paciente ID:    {i['id_paciente']}
        Médico ID:      {i['id_medico']}
        Data:           {i['data']}
        Hora:           {i['hora']}
        Status:         {i['status']}
        """)
    else:
        print("Você não está cadastrado.")

def quantidade_de_consultas_pendentes():
    doutor = input("Qual o nome do médico que deseja saber sobre suas consultas pendentes? ")
    id = f.id_paciente(medicos, doutor)
    if id:
        for i in consultas:
            if i["id_medico"] == id and i["status"] == "Agendada" or i["status"] == "Confirmada":
                print(f"""
        Consultas Pendentes
        ---------
        ID da consulta: {i['id']}
        Paciente ID:    {i['id_paciente']}
        Médico ID:      {i['id_medico']}
        Data:           {i['data']}
        Hora:           {i['hora']}
        Status:         {i['status']}
        """)
    else:
        print("Você não está cadastrado.")
