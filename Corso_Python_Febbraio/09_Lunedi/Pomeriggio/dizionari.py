studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}

print(studente["nome"])
print(studente["età"])

studente["età"] = 21
print(studente)

studente["città"] = "Roma"
print(studente)

print(studente.keys())
print(studente.values())
print(studente.items())