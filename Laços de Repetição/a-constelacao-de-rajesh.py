estrelas = int(input())  # Quantidade de estrelas
# Inicialização das variáveis
distancia = 0
contador = 0
# Variáveis para fibonacci
proximo = proximo2 = 1
anterior = anterior2 = 1
fibonacci = 0
# Variáveis para verificar se a soma das distâncias é um número primo
soma = 0
cont_primo = 0
primo = False

while (contador != estrelas) and (estrelas >= 3):
    eixo_x = int(input())
    eixo_y = int(input())
    contador += 1
    # Se o contador for 1, ele não consegue comparar a distância com outra estrela
    if ((contador % 2) != 0) and (contador != 1):
        distancia = int(((eixo_x2 - eixo_x)**2 + (eixo_y2 - eixo_y)**2)**(1/2))
        print("Distância [star" + str((contador-1)) +
              " <-> star" + str((contador)) + "]: " + str(distancia))
        soma += distancia
        # Verfica se a distância está na sequência de fibonacci
        while (proximo <= distancia):
            proximo = proximo + anterior
            anterior = proximo - anterior
            if (proximo == distancia):
                fibonacci += 1
        # Retorna os valores iniciais para entrar no laço novamente
        proximo = 1
        anterior = 1

    if (contador != estrelas):
        eixo_x2 = int(input())
        eixo_y2 = int(input())
        contador += 1
        distancia = int(((eixo_x - eixo_x2)**2 + (eixo_y - eixo_y2)**2)**(1/2))
        print("Distância [star" + str((contador-1)) +
              " <-> star" + str((contador)) + "]: " + str(distancia))
        soma += distancia
        while (proximo2 <= distancia):
            proximo2 = proximo2 + anterior2
            anterior2 = proximo2 - anterior2
            if (proximo2 == distancia):
                fibonacci += 1
        proximo2 = 1
        anterior2 = 1

# Verifica se a soma das distâncias é um número primo
for i in range(1, (soma + 1)):
    if (soma % i) == 0:
        cont_primo += 1
    if (cont_primo == 2):
        primo = True
    else:
        primo = False

# Condições para o que deve ser printado
if (fibonacci == (contador-1)) and (primo == False):
    print("Yes! Eu consegui!")
elif (fibonacci == (contador-1)) and (primo == True):
    print("Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!")
elif (fibonacci == (contador-2)):
    print("Oh, não! Eu quase consegui!")
elif (fibonacci < (contador-2)) and (primo == False):
    print("Eu vou acabar como o Stuart :/")
elif (fibonacci < (contador-2)) and (primo == True):
    print("Pelo menos o programa está funcionando...")
elif (estrelas <= 0):
    print("Isso está quebrado, acho que Howard pode me ajudar.")
elif (0 < estrelas < 3):
    print("Acho que bebi demais, eu juro que tinha mais estrelas!")
