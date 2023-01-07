adversario = input()
qnt_turnos = int(input())
parar = True
Mestre = False
adversarios_conhecidos = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14}
grupo = {'Bobby': ('Grande espada', 8, 'media'), 'Diana': ('Dardo', 12, 'leve'), 'Eric': ('Grande espada', 8, 'pesada'), 'Hank': ('Espada', 6, 'media'), 'Presto': ('Cajado', 4, 'leve'), 'Sheila': ('Espada', 6, 'leve'), 'Uni': ('Chifre', 2, 'leve')}
if adversario in adversarios_conhecidos:
  pontos_de_vida = adversarios_conhecidos.get(adversario) #Pontos de vida dos adversários conhecidos
else:
  pontos_de_vida = 9
  
while parar == True:
  try:
    personagem = input()
    qnt_turnos -= 1
    if personagem == "Mestre dos Magos":
        print("Muito obrigado amigo, que nos vejamos novamente um dia")
        Mestre = True
    else:
      dano = grupo.get(personagem)[1] #Armazenando o dano
      armadura = grupo.get(personagem)[2] #Armazenando a armadura
      if armadura == "media":
        qnt_turnos -= 1 
      if armadura == "leve":
        qnt_turnos -= 3
      pontos_de_vida -= dano
  except EOFError:
    parar = False
    if pontos_de_vida <= 0 and Mestre == False:
        print(f"{personagem} executou o ultimo golpe em {adversario}, estamos livres!")
    if qnt_turnos <= 0 and pontos_de_vida >= 0 and Mestre == False:
        print(f"Oh nao, {adversario} e muito forte, este e o fim!")