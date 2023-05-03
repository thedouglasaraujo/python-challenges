numeros = []
fazer = True
numeros.append(input().split(" "))  # Separando cada número da linha do input
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", " "]


def formar_frase():
    if fazer == True:
        for i in numeros:
            for numero in i:
                # O número dado no input será o índice da letra na lista para formar a frase
                print(letras[int(numero)], end="")


for i in numeros:
    for numero in i:
        if (int(numero) > 100) or (int(numero) < 0):  # Limitando o intervalo permitido
            print("Infelizmente os números nao dizem nada")
            fazer = False

if fazer == True:
    formar_frase()
