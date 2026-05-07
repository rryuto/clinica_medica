import json
import funcoes as f
from datetime import datetime
from datetime import date

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")
medicos = f.ler_json("medicos.json")

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
                print(i)

