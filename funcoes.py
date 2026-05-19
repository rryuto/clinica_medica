import json
from datetime import date, datetime
import funcoes as f
usuarios = f.ler_json("usuarios.json")
medicos = f.ler_json("medicos.json")
pacientes = f.ler_json("pacientes.json")
consultas = f.ler_json("consultas.json")
def ler_json(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def novo_id(lista):
    if not lista:
        return 1    
    else:
        return lista[len(lista)-1]["id"] + 1

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

def login(usuario, senha):
    usuarios_json = ler_json("usuarios.json")

    for i in usuarios_json:
        if i["usuario"].lower() == usuario.lower() and i["senha"] == senha:
            print("Login Realizado com sucesso\n")
            return i["nivel"]

def buscar_id(lista, id):
    for i in lista:
        if i["id"] == id:
            return i
    return None

def buscar_usuario(lista, usuario):
    for i in lista:
        if i["usuario"].lower() == usuario.lower():
            return i
    return None

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

def excluir_por_id(lista, id):
    for i in lista:
        if i["id"] == id:
            lista.remove(i)
            return True
    return False

def excluir_por_usuario(lista, usuario):
    for i in lista:
        if i["usuario"].lower() == usuario.lower():
            lista.remove(i)
            return True

def id_paciente(lista, nome):
    for i in lista:
        if i["nome"].lower() == nome.lower():
            return i["id"]
    return None

def procurar_medico(lista, nome):
    for i in lista:
        if i["nome"].lower() == nome.lower():
            return i
    return None

def listar_medicos():
    medicos = ler_json("medicos.json")
    for i in medicos:
        print(f"iD: {i['id']} - Nome: {i['nome']} - Especialidade: {i['especialidade']} - CRM: {i['crm']}")
    print("\n")

def validar_disponibilidade(lista, idmedico, hora, data):
    disponivel = True
    for i in lista:
        if i["status"] != "Cancelada":
            if idmedico == i["id_medico"] and data == i["data"] and hora == i["hora"]:
                disponivel = False
        
    return disponivel

def converter_data(data):
    return datetime.strptime(data, "%d/%m/%Y").date()

def validar_data(data_str, hora_str):
    data_informado = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
    
    if data_informado >= datetime.now():
        return True
    else:
        return False

def medico_existe(id):
    for i in medicos:
        if i["id"] == id:
            return True
            break
    return None

def retorna_id_medico(usuario):
    for i in usuarios:
        if i["usuario"] == usuario:
            return i["id"]

retorna_id_medico("med5")