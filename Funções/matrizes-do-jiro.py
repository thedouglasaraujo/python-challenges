contador_operacoes = 0
escalar = 0
m1 = []
m2 = []


def soma(primeirofator, segundofator):
    resultado = [[int(primeirofator[i][j]) + int(segundofator[i][j])
                  for j in range(len(primeirofator[0]))] for i in range(len(primeirofator))]
    return resultado


def subtracao(primeirofator, segundofator):
    resultado = [[int(primeirofator[i][j]) - int(segundofator[i][j])
                  for j in range(len(primeirofator[0]))] for i in range(len(primeirofator))]
    return resultado


def mult_escalar(matriz):
    resultado = [[int(matriz[i][j]) * int(escalar)
                  for j in range(len(matriz[0]))] for i in range(len(matriz))]
    return resultado


def mult_matriz(primeirofator, segundofator):
    resultado = [[sum(int(a) * int(b) for a, b in zip(primeirofator, segundofator))
                  for segundofator in zip(*segundofator)]
                 for primeirofator in primeirofator]
    return resultado


def separar_matriz(matriz):
    contador = 1
    while contador <= tamanho:
        matriz.append(input().split(" "))
        contador += 1


def imprimir_resultado(numero_matriz):
    for linha in numero_matriz:
        print(*linha)


tamanho = int(input())
separar_matriz(m1)
separar_matriz(m2)
quantidade_operacoes = int(input())

while contador_operacoes != quantidade_operacoes:
    operacao = input()
    matrizresultado = operacao[1]
    # Soma
    if operacao[8] == "+":
        if operacao[6] == "2":
            primeirofator = m2
        elif operacao[6] == "1":
            primeirofator = m1
        if operacao[11] == "2":
            segundofator = m2
        elif operacao[11] == "1":
            segundofator = m1
        if operacao[1] == "1":
            m1 = soma(primeirofator, segundofator)
        elif operacao[1] == "2":
            m2 = soma(primeirofator, segundofator)

    # Subtração
    if operacao[8] == "-":
        if operacao[6] == "2":
            primeirofator = m2
        elif operacao[6] == "1":
            primeirofator = m1
        if operacao[11] == "2":
            segundofator = m2
        elif operacao[11] == "1":
            segundofator = m1
        if operacao[1] == "1":
            m1 = subtracao(primeirofator, segundofator)
        elif operacao[1] == "2":
            m2 = subtracao(primeirofator, segundofator)

    # Multiplicação de uma matriz por um escalar
    if "*" in operacao:
        escalar = operacao.split(" ")
        for i in escalar:
            if i != "m2" and i != "=" and i != "m1" and i != "*":  # Procurando o escalar no input
                escalar = i
        if operacao[0]+operacao[1] == "m1":
            if operacao[-2]+operacao[-1] == "m1" or operacao[5]+operacao[6] == "m1":
                parametro = m1
                m1 = mult_escalar(parametro)
            elif operacao[-2]+operacao[-1] == "m2" or operacao[5]+operacao[6] == "m2":
                parametro = m2
                m1 = mult_escalar(parametro)
        if operacao[0]+operacao[1] == "m2":
            if operacao[-2]+operacao[-1] == "m1" or operacao[5]+operacao[6] == "m1":
                parametro = m1
                m2 = mult_escalar(parametro)
            elif operacao[-2]+operacao[-1] == "m2" or operacao[5]+operacao[6] == "m2":
                parametro = m2
                m2 = mult_escalar(parametro)

    # Multiplicação de uma matriz por outra matriz
    if "." in operacao:
        if operacao[6] == "1":
            primeirofator = m1
        elif operacao[6] == "2":
            primeirofator = m2
        if operacao[11] == "1":
            segundofator = m1
        elif operacao[11] == "2":
            segundofator = m2
        if operacao[0]+operacao[1] == "m2":
            m2 = mult_matriz(primeirofator, segundofator)
        elif operacao[0]+operacao[1] == "m1":
            m1 = mult_matriz(primeirofator, segundofator)

    contador_operacoes += 1

if matrizresultado == "1":
    imprimir_resultado(m1)
if matrizresultado == "2":
    imprimir_resultado(m2)
