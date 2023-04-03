'''5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''


lista = list(input("Escreva a Palavra para inverter : "))

print(lista)
listaInvertida = []
contador = len(lista)-1

for num in lista:
    listaInvertida.append(lista[contador])
    contador -= 1

transformandoEmString = "".join(listaInvertida)
print(transformandoEmString)