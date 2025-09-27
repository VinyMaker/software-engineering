import numpy as np
my_array = np.array([1,2,3,4,5,6])
print(f"Meu array original: {my_array}")

quadrado_do_array = my_array ** 2
soma_do_array = np.sum(my_array)
media_do_array = np.mean(my_array)

print(f"Array original: {my_array}")
print(f"Array ao quadrado: {quadrado_do_array}")
print(f"Soma dos elementos do array: {soma_do_array}")
print(f"Média dos elementos do array: {media_do_array}")

