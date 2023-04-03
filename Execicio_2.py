'''2) Dado a sequência de Fibonacci,
onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

valor = int(input("Que termo deseja encontrar na sequência: "))
ultimo = 1
penultimo = 0
sequencia = []
encontrouOuEMaior = False
if (valor==1) or (valor==2):
    print("1")
else:
    while not encontrouOuEMaior:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        sequencia.append(termo)
        if valor == termo:
            print(sequencia)
            print("O valor existe na sequência")
            encontrouOuEMaior = True
        elif termo > valor:
            print(sequencia)
            print("O valor não existe na sequência")
            encontrouOuEMaior = True


