import json

def ler_json(arquivo):
    with open(arquivo, "r") as f:
        json.load(f)

def salvar_json(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=2)

