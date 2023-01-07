silabas = []
indices = []
verificador = []
temporario = []
juntar = []
parar = False
Fazer = True

def separarsilabas(string,lista):
  for letra in string:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        lista.append(string[:(string.index(letra))+1])
        string = string[string.index(letra)+1:]
        
def verificar(lista,separacao,definitiva,mudar):
  for silaba in lista:
    if silaba in separacao and silaba not in definitiva:
      definitiva.append(silaba)
      mudar.append(silaba)
      
def limparlistas():
  silabas.clear()
  juntar.clear()
  temporario.clear()
  
def formatarprint():
  for i in silabas: 
    junt = ''.join(i)
    juntar.append(junt)
    
while parar != True:
  letras = input()
  #Separando sílabas  
  separarsilabas(letras,silabas)
  hospital = ['shi','chi','ko','ku','ya','ma']
  #Verificando se a sílaba é igual a sílaba do hospital
  verificar(silabas,hospital,verificador,temporario)
  
  juntarstr = ', '.join(temporario) #Formatando o print 
  formatarprint()
  #Condições para printar
  if len(temporario) == 0:
    print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")
  if len(temporario) == 1:
    print(f"Lembrei! A sílaba {juntarstr} está no nome do hospital. Obrigada, Totoro!")
  if len(temporario) == len(silabas) and len(temporario) > 1 and letras in "shichikokuyama":
    print(f"A palavra {letras} está toda no nome do hospital. Acertou em cheio, Totoro!")
    Fazer = False
  if len(temporario) >= 2 and Fazer == True:
    print(f"Lembrei! As sílabas: {juntarstr} estão no nome do hospital. Obrigada, Totoro!")
  limparlistas()
  Fazer = True
  if "shi" in verificador and "chi" in verificador and "ko" in verificador and "ku" in verificador and "ya" in verificador and "ma" in verificador:
    print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!")
    parar = True