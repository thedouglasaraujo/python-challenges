senha = input()
qtd_palavras = int(input())
senhanova = []
decifrar = []
achou = False
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
contador = 0


def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)  # Recursão para calcular Fibonacci


def fatorial(z):
    if (z == 0):
        return 1
    else:
        return z * fatorial(z-1)  # Recursão para calcular o fatorial


def somar(lista1, lista2):  # Função para somar Fatorial e Fibonacci caso a operação 1 seja par
    resultado = [elemA + elemB for elemA, elemB in zip(lista1, lista2)]
    return resultado


# Função para multiplicar Fatorial e Fibonacci caso a operação 1 seja ímpar
def multiplicar(lista1, lista2):
    resultado = [elemA * elemB for elemA, elemB in zip(lista1, lista2)]
    return resultado


def traducaosenha(indice):
    elemento = lista[indice]
    if elemento == "1fixo":  # Caso a operação 1 seja 0
        decifrar.append('1')
    else:
        if int(elemento) > 25:
            elemento = elemento % 26  # Para colocar o número no intervalo das letras do alfabeto
            decifrar.append(letras[elemento])
        else:
            decifrar.append(letras[elemento])
    if (indice+1) < len(lista):
        traducaosenha(indice+1)  # Recursão para traduzir os números em letras


def fazer_mod(indice):
    # Analisa letra por letra da palavra
    numero = letras.index(palavra[indice])
    operacao1 = numero % 11
    contador2 = 0
    while contador2 != operacao1:
        fatoracoes.append(fatorial(contador2))
        contador2 += 1
    for i in range(0, operacao1):
        x.append(fib(i))
    if operacao1 == 0:
        senhanova.append(["1fixo"])
    elif operacao1 % 2 == 0:  # Caso seja par
        soma = somar(x, fatoracoes)
        senhanova.append(soma)
    elif operacao1 % 2 != 0:  # Caso seja ímpar
        mult = multiplicar(x, fatoracoes)
        senhanova.append(mult)
    if indice+1 < len(palavra):
        fatoracoes.clear()
        x.clear()
        # Recursão para analisar a próxima letra da palavra
        fazer_mod(indice+1)


while contador != qtd_palavras:
    palavra = input()
    fatoracoes = []
    x = []
    mult = []
    senhanova = []
    decifrar = []
    fazer_mod(0)
    for lista in senhanova:
        traducaosenha(0)
    # Formatação para verificar a igualdade da senha
    juntarstr = ''.join(decifrar)
    if juntarstr == senha:  # Se a senha encontrada for igual a mostrada no input
        achou = True
    contador += 1

# Condições para printar:
if achou == True:
    print("Achamos! Achamos a senha.")
else:
    print("É... Temos que procurar mais.")
