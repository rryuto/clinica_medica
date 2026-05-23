import json
import funcoes as f
from datetime import datetime
from datetime import date

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")
medicos = f.ler_json("medicos.json")
prontuarios = f.ler_json("prontuarios.json")

#Agenda
def Listar_consultas_para_medico_especifico(usuario):
    id_medico = f.retorna_id_medico(usuario)
    existe = False
    if id_medico:
        for i in consultas:
            if i["id_medico"] == id_medico and (i["status"] == "Agendada" or i["status"] == "Confirmada"):
                print(f"""
                            Consultas 
                            ---------
                            ID da consulta: {i['id']}
                            Paciente ID:    {i['id_paciente']}
                            Médico ID:      {i['id_medico']}
                            Data:           {i['data']}
                            Hora:           {i['hora']}
                            Status:         {i['status']}
                            """)

                existe = True
    
    if not existe:
            print(f"Nao ha consultas no dia.")

def Visualisar_agenda_diaria(usuario):
    id = f.retorna_id_medico(usuario)
    hoje = date.today()
    existe = False

    for i in consultas:
        if hoje.strftime("%d/%m/%Y") == i["data"] and (i["status"] == "Agendada" or i["status"] == "Confirmada") and i["id"] == id:
            print(f"ID: {i['id']} - ID do paciente: {i['id_paciente']} - ID do medico: {i['id_medico']} - Hora: {i['hora']}")
            existe = True
    if not existe:
        print("Nao ha consultas hoje.")

def Visualizar_agenda_futura(usuario):
    id = f.retorna_id_medico(usuario)
    hoje = datetime.today()
    if id:
        for i in consultas:
            if datetime.strptime(i["data"], "%d/%m/%Y").timestamp() > hoje.timestamp():
                print(f"{i}")


#Atendimento 
def Iniciar_Atendimento(usuario):
    id = f.retorna_id_medico(usuario)
    id_atendimento = int(input("Qual consulta deseja iniciar?\nID da consulta: "))
    existe = False    
    for i in consultas:
        if (i["status"] == "Confirmada" or i["status"] == "Agendada") and i["id_medico"] == id and id_atendimento == i["id"]:
            i["status"] = "Em Atendimento"
            existe = True
            print("Você iniciou o atendimento.")
            f.salvar_json("consultas.json", consultas)
    if not existe:
        print("Consulta inexistente")
    
def Finalizar_Atendimento(usuario):
    id = f.retorna_id_medico(usuario)
    id_atendimento = int(input("Qual consulta deseja Finalizar?\nID da consulta: "))
    existe = False    
    for i in consultas:
        if i["status"] == "Em Atendimento" and i["id_medico"] == id and id_atendimento == i["id"]:
            i["status"] = "Finalizada"
            existe = True
            print("Atendimento Finalizado.")
            f.salvar_json("consultas.json", consultas)
    if not existe:
        print("Consulta inexistente")


#Prontuário/Laudo
def Laudo_Medico(usuario):
    id = f.retorna_id_medico(usuario)
    id_consulta = input("Qual consulta deseja fazer o prontuário?\nid da consulta: ")
    for i in consultas:
        if i["status"] == "Em Atendimento" and i["id_medico"] == id and id_consulta == i["id"]:
            data = str(date.today())
            Diagnostico = input("Qual o diagnóstico final do paciente? ")
            receita = input("Qual a receita médica á ser passado? ")
            observacoes = input("Quais são as observações que devem ser passadas ao paciente? ")
            novo_prontuario = {"id" : f.novo_id(prontuarios)
                    ,"id_paciente" : i["id_paciente"]
                    , "id_medico" : id
                    , "data" : data
                    , "diagnostico" : Diagnostico
                    , "receita" : receita
                    , "observacoes" : observacoes}
            prontuarios.append(novo_prontuario)
    f.salvar_json("prontuarios.json", prontuarios)



#Histórico Médico
def buscar_paciente_por_nome(usuario):
    id = f.retorna_id_medico(usuario)
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

def Ver_historico_de_consultas_anteriores(usuario):
    id = f.retorna_id_medico(usuario)
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

def ver_prontuarios_anteriores_do_paciente(usuario):
    id = f.retorna_id_medico(usuario)
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
def Total_de_atendimentos(usuario):
    
    id = f.retorna_id_medico(usuario)
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

def pacientes_atendidos_no_mes(usuario):
    id = f.retorna_id_medico(usuario)
    if id:
        mes_atual = date.today().month
        ano_atual = date.today().year
        encontrou = False
        for i in consultas:
            if i["id_medico"] == id and i["status"] == "Finalizada":
                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y")
                if (data_consulta.month == mes_atual and
                    data_consulta.year == ano_atual):
                    print(f"Pacientes atendidos no mês: iD: {i['id']} - ID do paciente: {i['id_paciente']} - ID do medico: {i['id_medico']} - Hora: {i['hora']}")
            encontrou = True
        if not encontrou:
            print("Você não atendeu nenhum paciente esse mês.")
    else:
        print("Você não está cadastrado.")

def quantidade_de_consultas_pendentes(usuario):
    id = f.retorna_id_medico(usuario)
    if id:
        for i in consultas:
            if i["id_medico"] == id and (i["status"] == "Agendada" or i["status"] == "Confirmada"):
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

#MAIN ===========================================================================================================

def consultas_status_medico(usuario, status):
    id_medico = f.retorna_id_medico(usuario)
    if not id_medico:
        return 0
    hoje = date.today()
    n = 0
    for i in consultas:
        data_consulta = f.converter_data(i["data"])
        if data_consulta == hoje and i["status"] == status and i["id_medico"] == id_medico:
            n += 1
    return n

def menu_agenda(usuario):
    while True:
        print("========== AGENDA ===========")
        print(" 1 - Listar consultas agendadas/confirmadas")
        print(" 2 - Visualizar agenda diária")
        print(" 3 - Visualizar agenda futura")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            Listar_consultas_para_medico_especifico(usuario)
        elif op == 2:
            Visualisar_agenda_diaria(usuario)
        elif op == 3:
            Visualizar_agenda_futura(usuario)
        else:
            print("Opção inválida.")

def menu_atendimento(usuario):
    while True:
        print("========== ATENDIMENTO ===========")
        print(" 1 - Iniciar atendimento")
        print(" 2 - Finalizar atendimento")
        print(" 3 - Registrar laudo médico (prontuário)")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            Iniciar_Atendimento(usuario)
        elif op == 2:
            Finalizar_Atendimento(usuario)
        elif op == 3:
            Laudo_Medico(usuario)
        else:
            print("Opção inválida.")

def menu_historico(usuario):
    while True:
        print("========== HISTÓRICO / PRONTUÁRIO ===========")
        print(" 1 - Buscar paciente por nome")
        print(" 2 - Ver histórico de consultas anteriores")
        print(" 3 - Ver prontuários anteriores do paciente")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            buscar_paciente_por_nome(usuario)
        elif op == 2:
            Ver_historico_de_consultas_anteriores(usuario)
        elif op == 3:
            ver_prontuarios_anteriores_do_paciente(usuario)
        else:
            print("Opção inválida.")

def menu_relatorios(usuario):
    while True:
        print("========== RELATÓRIOS ===========")
        print(" 1 - Total de atendimentos finalizados")
        print(" 2 - Pacientes atendidos no mês")
        print(" 3 - Consultas pendentes")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            Total_de_atendimentos(usuario)
        elif op == 2:
            pacientes_atendidos_no_mes(usuario)
        elif op == 3:
            quantidade_de_consultas_pendentes(usuario)
        else:
            print("Opção inválida.")

def menu_principal(usuario):
    while True:
        print("\n========== MENU PRINCIPAL ===========")
        print(" 1 - Agenda")
        print(" 2 - Atendimento")
        print(" 3 - Histórico / Prontuário")
        print(" 4 - Relatórios")
        print(" 0 - Sair")
        op = int(input("Opção: "))
        if op == 0:
            print("Até logo.")
            break
        elif op == 1:
            menu_agenda(usuario)
        elif op == 2:
            menu_atendimento(usuario)
        elif op == 3:
            menu_historico(usuario)
        elif op == 4:
            menu_relatorios(usuario)
        else:
            print("Opção inválida.")

def open_medico(usuario):
    id_medico = f.retorna_id_medico(usuario)
    medico = f.buscar_id(medicos, id_medico) if id_medico else None
    nome = medico["nome"] if medico else usuario
    print("===== MÉDICO =====")
    print(f"Médico: {nome}")
    print(f"Consultas agendadas hoje: {consultas_status_medico(usuario, 'Agendada')}")
    print(f"Consultas confirmadas hoje: {consultas_status_medico(usuario, 'Confirmada')}")
    print(f"Em atendimento hoje: {consultas_status_medico(usuario, 'Em Atendimento')}")
    print(f"Atendimentos finalizados hoje: {consultas_status_medico(usuario, 'Finalizada')}")
