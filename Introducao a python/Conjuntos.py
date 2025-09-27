#Add(), in e remove()

#criando um conjunto vazio
meu_conjunto = set()
meu_conjunto.add(1)
meu_conjunto.add(2)
meu_conjunto.add(3)
print(meu_conjunto)

elemento = 2
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto\n")
else:
    print(f"{elemento} não está no conjunto\n")
    
meu_conjunto.remove(2)
print(meu_conjunto)
