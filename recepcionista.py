import funcoes as f
from datetime import date, datetime

pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")
medicos = f.ler_json("medicos.json")

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
    if id:
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
            print("Opção inválida.")
        f.salvar_json("pacientes.json", pacientes)
    else:
        print("Paciente não encontrado")

   

def buscar_paciente_especifico():
    paciente = input("Digite o nome do paciente que você deseja buscar: ")
    
    for i in pacientes:
        if i["nome"].lower() == paciente.lower():
            print(f"iD: {i['id']} - Nome: {i['nome']} - Idade: {i['idade']} - CPF: {i['cpf']} - Telefone: {i['telefone']} - Endereço: {i['endereco']}")
            break
    else:
        print("Paciente não encontrado.")


def listar_pacientes():
    for i, valor in enumerate(pacientes):
        print(f"{valor['id']} --- {valor['nome']}")   

def Visuzlizar_dados_completos():
    print("Qual paciente deseja ver os dados?")
    id_paciente = int(input("iD do paciente: "))
    if f.buscar_id(pacientes, id_paciente):
        for i in pacientes:
            if i["id"] == id_paciente:
                print(f"ID: {i['id']}")
                print(f"Nome: {i['nome']}")
                print(f"CPF: {i['cpf']}")
                print(f"Telefone: {i['telefone']}")
                print(f"Endereco: {i['endereco']}")
                break
    else:
        print(f"Paciente nao encontrado.")
    

def menu_pacientes():
    while True:
        print("========== PACIENTES ===========")
        print(" 1 - Cadastrar paciente")
        print(" 2 - Editar paciente")
        print(" 3 - Buscar paciente específico")
        print(" 4 - Listar todos os pacientes")
        print(" 5 - Visualizar dados completos")
        print(" 0 - Voltar")
        opção = int(input("Digite uma opção: "))
        if opção == 0:
            break
        elif opção == 1:
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
            print("Opção inválida.")

#CONSULTAS ===========================================================================================================

#marcar consulta
def marcar_consulta():
    nome_paciente = input("Nome do paciente: ")
    id_paciente = f.id_paciente(pacientes, nome_paciente)
    f.listar_medicos()
    id_medico = int(input("Escolha um medico pelo iD: "))
    data = input("Data(DD/MM/AAAA): ")
    hora = input("Hora(HH:MM): ")
    if f.validar_data(data, hora):
        if f.validar_disponibilidade(consultas, id_medico, hora, data):
            if f.medico_existe(id_medico) and id_paciente:
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
    else:
        print("Por favor insira uma data futura.")

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
            if i["id"] == id and i["status"] == "Agendada":
                i["status"] = "Confirmada"
                f.salvar_json("consultas.json", consultas)
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

def consultas_futuras():
    hoje = date.today()
    existe = False
    for i in consultas:
        data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()
        if data_consulta > hoje and i["status"] == "Agendada":
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
        print("Nao ha consultas futuras.")

def menu_consultas():
    while True:
        print("========== CONSULTAS ===========")
        print(" 1 - Marcar consulta (médico, data e horário)")
        print(" 2 - Reagendar consulta")
        print(" 3 - Cancelar consulta")
        print(" 4 - Confirmar presença do paciente")
        print(" 5 - Listar consultas do dia")
        print(" 6 - Listar consultas futuras")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            marcar_consulta()
        elif op == 2:
            reagendar_consulta()
        elif op == 3:
            cancelar_consulta()
        elif op == 4:
            confirmar_consulta()
        elif op == 5:
            consultas_hoje()
        elif op == 6:
            consultas_futuras()
        else:
            print("Opção inválida.")

#historico

#•	Visualizar consultas anteriores do paciente 
def consultas_anteriores_paciente():
    nome_paciente = input("Nome do paciente: ")
    id_paciente = f.id_paciente(pacientes, nome_paciente)
    existe = False
    if id_paciente:
        for i in consultas:
            if i["id_paciente"] == id_paciente and i["status"] == "Finalizada":
                    print(f"""
        Consultas Finalizadas
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
            print(f"Consultas passadas inexistente.")
    else:
        print(f"Paciente nao encontrado.")

def menu_historico():
    while True:
        print("========== HISTÓRICO ===========")
        print(" 1 - Consultas anteriores do paciente")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            consultas_anteriores_paciente()
        else:
            print("Opção inválida.")

#Relatorios

#agenda do dia
#nao e a mesma coisa que consultas do dia?

#consultas por data

def consultas_por_data():
    data = input("Data a consultar no formato(DD/MM/AAAA)\n")
    existe = False

    for i in consultas:
        if i["data"] == data:
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
            print(f"Nao ha consultas para esta data.")

#consultas canceladas no periodo

def consultas_canceladas_no_periodo():
    data_inicio = input("Data de inicio no formato(DD/MM/AAAA):")
    data_inicio = f.converter_data(data_inicio)
    data_fim = input("Data de fim no formato(DD/MM/AAAA):")
    data_fim = f.converter_data(data_fim)
    existe = False
    for i in consultas:
        if i["status"] == "Cancelada":
            data_consulta = f.converter_data(i["data"])
            if data_inicio <= data_consulta <= data_fim:
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
            print(f"Nao ha consultas neste periodo.")

def pacientes_atendidos_no_dia():
    hoje = date.today()
    existe = False
    for i in consultas:
        data_consulta = f.converter_data(i["data"])
        if data_consulta == hoje and i["status"] == "Finalizada":
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
            print(f"Nao ha pacientes atendidos no dia.")

def menu_relatorios():
    while True:
        print("========== RELATÓRIOS ===========")
        print(" 1 - Agenda do dia")
        print(" 2 - Consultas por data")
        print(" 3 - Consultas canceladas no período")
        print(" 4 - Pacientes atendidos no dia")
        print(" 0 - Voltar")
        op = int(input("Opção: "))
        if op == 0:
            break
        elif op == 1:
            consultas_hoje()
        elif op == 2:
            consultas_por_data()
        elif op == 3:
            consultas_canceladas_no_periodo()
        elif op == 4:
            pacientes_atendidos_no_dia()
        else:
            print("Opção inválida.")

#MAIN

def consultas_status(status):
    hoje = date.today()
    n = 0
    for i in consultas:
        data_consulta = f.converter_data(i["data"])
        if data_consulta == hoje and i["status"] == status:
            n += 1
    return n

def menu_principal():
    while True:
        print("\n========== MENU PRINCIPAL ===========")
        print(" 1 - Pacientes")
        print(" 2 - Consultas")
        print(" 3 - Histórico")
        print(" 4 - Relatórios")
        print(" 0 - Sair")
        op = int(input("Opção: "))
        if op == 0:
            print("Até logo.")
            break
        elif op == 1:
            menu_pacientes()
        elif op == 2:
            menu_consultas()
        elif op == 3:
            menu_historico()
        elif op == 4:
            menu_relatorios()
        else:
            print("Opção inválida.")

print("=====RECEPCIONISTA=====")
print(f"Consultas hoje: {consultas_status("Agendada")}")
print(f"Pacientes cadastrado: {len(pacientes)}")
print(f"Médicos ativos: {len(medicos)}")
print(f"Atendimentos finalizados hoje: {consultas_status("Finalizada")}")
print(f"Consultas canceladas hoje: {consultas_status("Cancelada")}")

menu_principal()

