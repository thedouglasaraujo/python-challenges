#Contadores
piadas_boas = 0
piadas_ruins = 0

piada = input()

while (piada != "Fim do Show!"): #Entradas não param até receber "Fim do Show!"
  reacao = input()
  if (reacao == "BAZINGA!"):
    piadas_boas += 1
  else:
    piadas_ruins += 1
  piada = input()
  
    
if (piadas_boas > ((piadas_boas + piadas_ruins) * 0.6)): #Cálculo para saber se a quantidade de piadas boas é 60% maior que o total das piadas
    print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
elif (piadas_ruins > ((piadas_boas + piadas_ruins) * 0.6)):
    print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
else:
    print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")
