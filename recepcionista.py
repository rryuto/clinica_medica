import json
import funcoes as f

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")

#CONSULTAS ===========================================================================================================

#marcar consulta

nome_paciente = input("Nome do paciente: ")
id_paciente = f.id_paciente(pacientes, nome_paciente)
print(f.listar_medicos())
id_medico = int(input("Escolha um medico pelo iD: "))
data = input("Data: ")
hora = input("Hora: ")

nova_consulta = {"id": f.novo_id(consultas),
                 "id_paciente": id_paciente,
                 "id_medico": id_medico,
                 "data": data,
                 "hora": hora,
                 "status": "Agendada"}

consultas.append(nova_consulta)
f.salvar_json(consultas, "consultas.json")
print("Consulta marcada com sucesso.")