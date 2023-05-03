acoes = 0  # Contador do avanço da carreira
feito1 = ""  # Inicializa feito1 para entrar no primeiro laço

while (acoes == 0) and (feito1 != "é o fim da estrada pra sheldon cooper"):
    feito1 = input().lower()
    if (feito1 == "começou a trabalhar na caltech"):
        acoes = 1
        # Verifica se a entrada seguinte ao avanço da carreira é um bazinga
        feito2 = input().lower()
        if (feito2 == "bazinga"):
            acoes = 0  # Se a entrada seguinte for bazinga, ele entra novamente no laço e cancela o feito anterior
    elif (feito1 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito1 == "leonard seu anão covarde") or (feito1 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")

while (acoes == 1) and (feito2 != "é o fim da estrada pra sheldon cooper"):
    if (feito2 == "trabalho sobre a string theory"):
        acoes = 2
        feito3 = input().lower()
        if (feito3 == "bazinga"):
            acoes = 1
    elif (feito2 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito2 == "leonard seu anão covarde") or (feito2 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")
        feito2 = input().lower()
    else:
        feito2 = input().lower()

while (acoes == 2) and (feito3 != "é o fim da estrada pra sheldon cooper"):
    if (feito3 == "ganhar o chancellor de ciência"):
        acoes = 3
        feito4 = input().lower()
        if (feito4 == "bazinga"):
            acoes = 2
    elif (feito3 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito3 == "leonard seu anão covarde") or (feito3 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")
        feito3 = input().lower()
    else:
        feito3 = input().lower()

while (acoes == 3) and (feito4 != "é o fim da estrada pra sheldon cooper"):
    if (feito4 == "pensar na teoria de cooper-hofstader"):
        acoes = 4
        feito5 = input().lower()
        if (feito5 == "bazinga"):
            acoes = 3
    elif (feito4 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito4 == "leonard seu anão covarde") or (feito4 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")
        feito4 = input().lower()
    else:
        feito4 = input().lower()

while (acoes == 4) and (feito5 != "é o fim da estrada pra sheldon cooper"):
    if (feito5 == "criou a super assimetria"):
        acoes = 5
        feito6 = input().lower()
        if (feito6 == "bazinga"):
            acoes = 4
    elif (feito5 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito5 == "leonard seu anão covarde") or (feito5 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")
        feito5 = input().lower()
    else:
        feito5 = input().lower()

while (acoes == 5) and (feito6 != "é o fim da estrada pra sheldon cooper"):
    if (feito6 == "ganhar o nobel"):
        acoes = 6
    elif (feito6 == "tinha que ser o engenheiro sem phd do wolowitz") or (feito6 == "leonard seu anão covarde") or (feito6 == "tu é muito burro raj"):
        print("Não xingue seus amigos Sheldon!")
        feito6 = input().lower()
    else:
        feito6 = input().lower()

# Condições do que deve ser printado
if (acoes == 0):
    print("Que potencial desperdiçado...")
elif (acoes == 1) or (acoes == 2):
    print("Tão perto, mas tão longe")
elif (acoes == 3) or (acoes == 4):
    print("Não desista Sheldon, você ainda têm muito para alcançar!")
elif (acoes == 5):
    print("Nãoooooo, esse momento ia ser seu Sheldon")
elif (acoes == 6):
    print("Você conseguiu Sheldon, o Nobel é seu!!!")
