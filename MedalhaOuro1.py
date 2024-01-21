import math

# Descrição do programa
print ("Este programa calcula um ângulo formado entre dois vetores no espaço")

# O utilizador é questionado para colocar os vetores u e v
print ("Qual é as coordenadas do vetor u? (Coloca x, y e z em linhas diferentes)")
uxcoor = int(input())
uycoor = int(input())
uzcoor = int(input())

print (f"\nQual é as coordenadas do vetor v? (Repete o mesmo processo)")
vxcoor = int(input())
vycoor = int(input())
vzcoor = int(input())

# Calculo das normas dos vetores
normau = math.sqrt((uxcoor**2)+(uycoor**2)+(uzcoor**2))
normav = math.sqrt((vxcoor**2)+(vycoor**2)+(vzcoor**2))

# Calculo do produto escalar e do consequente ângulo arredondado às centésimas
produtoescalar = (uxcoor*vxcoor)+(uycoor*vycoor)+(uzcoor*vzcoor)
anguloradiano = round(math.acos(produtoescalar/(normau+normav)), 2)
angulograus = round(anguloradiano*180/math.pi, 1)

print (f"\nO ângulo formado entre os vetores u e v é: {angulograus}º/{anguloradiano}rad")