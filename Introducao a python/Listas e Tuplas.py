#tuplas de convidados
convidados = ("alice", "Breno", "carol", "dave", "evelyn")
print("Lista inicial de Convidados:")
for cada_convidado in convidados:
    print(cada_convidado)

#lista de confirmações
confirmações = ["alice", "Breno"]
print("\nConvidados que confirmaram presença:")
for cada_confirmação in confirmações:
    print(cada_confirmação)

# #identificar quem ainda não confirmou
print("\n")
não_confirmados = []
for cada_convidado in convidados:
    if cada_convidado not in confirmações:
        não_confirmados.append(cada_convidado)
        print(f"{cada_convidado} ainda não confirmou presença.")

print("\nLista de não confirmados:")
for pessoa in não_confirmados:
    print(pessoa)
print(f"\nTotal de não confirmados: {len(não_confirmados)}")

# #Enviar lembretes aos não confirmados
# print("\nEnviando lembretes aos não confirmados: (...simulado)")
