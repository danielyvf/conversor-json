import json

dicionario = {
    "Nome" : "Python",
    "Missão" : "Ser incrível"
}

conteudo = json.dumps(dicionario, ensure_ascii=False, indent=4) 
with open("arquivo.json", mode="w", encoding="utf-8") as arquivo: 
    arquivo.write(conteudo) 

print("arquivo gerado corretamente")