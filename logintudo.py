import json
#Login de Acesso
with open("usuarios.json","r") as arq:
    dados = json.load(arq)
def login(nivel_acesso):
    print("---SEU LOGIN---")
    usuario = input("Informe seu usuario: ")
    senha = input("Informe sua senha: ")
    for i in dados:
        if usuario == i["usuario"] and senha == i["senha"] and  nivel_acesso == i["nivel"]:
            print(f"Bem vindo,{usuario}!")
            return
    print("Usuarios ou senha inválido!")
while True:
    print(" 1 - Admin ")
    print(" 2 - Recepcionista ")
    print(" 3 - Médico ")
    nivel_acesso = int(input("Digite o seu número referente á sua função: "))
    if nivel_acesso == 1:
        login(nivel_acesso)
        break
    elif nivel_acesso == 2:
        login(nivel_acesso)
        break
    elif nivel_acesso == 3:
        login(nivel_acesso)
        break