sentencas = int(input())
contador = 0

def verificar_equacoes(indice):
  if equacao[indice] == "(":
    C.append("(")
  elif equacao[indice] == ")":
    Ç.append(")")
  if (indice+1) < len(equacao):
    verificar_equacoes(indice+1) #Recursão para analisar o próximo caractere da equação
  
while contador < sentencas:
  equacao = input()
  C = [] #C = (
  Ç = [] #Ç = )
  verificar_equacoes(0) #Parâmetro 0, pois é o primeiro índice da equação
  if len(C) == len(Ç):
    print("Essa sentença está com os parênteses balanceados, HOORAY!")
  if len(C) > len(Ç):
    print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
  if len(Ç) > len(C):
    print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
  contador += 1
  