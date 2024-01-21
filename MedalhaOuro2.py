import sys
import time
from time import sleep

print ("Bem vindo a uma aventura pelo conhecimento onde irás enriquecer o teu cérebro!")

# Deixar 3 segundos entre a primeira print e a segunda
sleep(3)

print ("Insere o teu nome aventureiro")
respostanome = input()

print (f"\nTens a certeza, {respostanome}? (s/n)")
resposta = input()

respostatacs = resposta == "s" or "S"
respostatacn = resposta == "n" or "N"
respostatacindef = resposta != "s" or resposta != "n" or resposta != "S" or resposta != "N"

# Loop até a resposta ser válida. Aplica-se em diversas porcoes
# de código
while respostatacn == True:
  print ("\nReescreve o teu nome")
  respostanome = input()
  print (f"\nTens a certeza, {respostanome}? (s/n)")
  resposta = input()
  respostatacs = resposta == "s" or "S"
  respostatacn = resposta == "n" or "N"
  respostatacindef = resposta != "s" or resposta != "n" or resposta != "S" or resposta != "N"


if respostatacs == True:
  print (f"\nBoa! Bem vindo {respostanome}, bonito nome... Adoro! Continuemos.")

sleep(3)
print("\nAgora que já sei o teu nome, deixa-me explicar-te como vai funcionar o jogo. Terás de responder a várias perguntas, com 4 opções cada uma. Quando escolheres uma opção correta, ganhas 1 ponto. Se escolheres a opção errada, então (infelizmente) não te posso dar nenhum ponto. Começas com 0 pontos.")

sleep(10)

print("""\nQuando estiveres pronto, basta selecionares um dos temas presentes em baixo (coloca apenas o número). Não são muitos, mas é lidar...
1 - Futebol (nivel de dificuldade -> fácil)
2 - Geografia (nivel de dificuldade -> médio)""")
tema = input()

while tema != "1" and tema != "2": 
  print ("\nNão percebi... Tenta novamente")
  tema = input()

def futebol():
  sleep(0.5)
  print ("\nBeeeeeep! Apita o árbitro! Inicia o jogo!")

  sleep(2)

  print ("1 - No futebol, quando um jogador toca com a mão na bola dentro da sua grande área o que acontece?")
  sleep(5)
  
  print (f"""
  A. Lançamento lateral
  B. Pontapé de Baliza
  C. Penálti
  D. É expulso da partida""")

  resposta1fut = input()
  pontos = 0

  if resposta1fut == "C" or resposta1fut == "c":
    pergunta1 = True
    pontos1 = pontos+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos1} ponto(s)")
  else:
    pergunta1 = False
    pontos1 = pontos
    print ("Incorreto. A resposta correta era a C (Penálti). Para a próxima consegues.")

  sleep(2)

  print ("\nProsseguindo...")
  print ("2 - O que acontece quando o árbitro da partida mostra um cartão vermelho a um jogador?")
  sleep(3)
  print (f"""
  A. Fica na partida mas sem poder tocar na bola
  B. Sai cinco minutos
  C. É expulso da partida
  D. O jogador não pode mais chutar à baliza""")

  resposta2fut = input()

  if resposta2fut == "C" or resposta2fut == "c":
    pergunta2 = True
    pontos2 = pontos1+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos2} ponto(s)")
  else:
    pergunta2 = False
    pontos2 = pontos1
    print ("Incorreto. A resposta correta era a C (É expulso da partida). Para a próxima acertas.")

  sleep(2)

  print ("\nNext...")
  print ("3 - O que acontece quando um jogador marca 3 ou mais golos na mesma partida?")
  sleep(3)
  print (f"""
  A. Fica com a bola da partida e consequentemente leva-a para casa
  B. É proibido de jogar o próximo jogo da equipa
  C. Fica mais 10 minutos em campo
  D. Oferece a camisola ao árbitro da partida""")

  resposta3fut = input()

  if resposta3fut == "A" or resposta3fut == "a":
    pergunta3 = True
    pontos3 = pontos2+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos3} ponto(s)")
  else:
    pergunta3 = False
    pontos3 = pontos2
    print ("Incorreto. A resposta correta era a A (Fica com a bola da partida e consequentemente leva-a para casa). Para a próxima acertas.")
  
  sleep(2)

  print ("\nContinuando...")
  print ("4 - O que acontece quando a bola sai pela linha final do campo do jogador que tocou por último na bola?")
  sleep(3)
  print (f"""
  A. Canto
  B. Livre indireto
  C. Penálti
  D. O jogo acaba""")

  resposta4fut = input()

  if resposta4fut == "A" or resposta4fut == "a":
    pergunta4 = True
    pontos4 = pontos3+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos4} ponto(s)")
  else:
    pergunta4 = True
    pontos4 = pontos3
    print ("Incorreto. A resposta correta era a A (Canto). Para a próxima acertas.")
  
  sleep(2)

  print ("\nSeguinte...")
  print ("5 - Qual é o melhor marcador da história do futebol (golos oficiais)?")
  sleep(3)
  print (f"""
  A. Pelé
  B. Cristiano Ronaldo.
  C. Lionel Messi
  D. Diego Maradona""")

  resposta5fut = input()

  if resposta5fut == "B" or resposta5fut == "b":
    pergunta5 = True
    pontos5 = pontos4+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos5} ponto(s)")
  else:
    pergunta5 = False
    pontos5 = pontos4
    print ("Incorreto. A resposta correta era a B (Cristiano Ronaldo). Para a próxima acertas.")

  sleep(2)

  print ("\nPróxima pergunta...")
  print ("6 - Qual é o melhor assistente da história do futebol?")
  sleep(3)
  print (f"""
  A. Luis Figo
  B. Lionel Messi
  C. David Beckham
  D. Cristiano Ronaldo""")

  resposta6fut = input()

  if resposta6fut == "C" or resposta6fut == "c":
    pergunta6 = True
    pontos6 = pontos5+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos6} ponto(s)")
  else:
    pergunta6 = False
    pontos6 = pontos5
    print ("Incorreto. A resposta correta era a C (David Beckham). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nPróxima questão...")
  print ("7 - Qual é o melhor marcador da história de seleções?")
  sleep(3)
  print (f"""
  A. Ali Daei
  B. Ferenc Puskás
  C. Cristiano Ronaldo.
  D. Pelé""")

  resposta7fut = input()

  if resposta7fut == "C" or resposta7fut == "c":
    pergunta7 = True
    pontos7 = pontos6+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos7} ponto(s)")
  else:
    pergunta7 = False
    pontos7 = pontos6
    print ("Incorreto. A resposta correta era a C (Cristiano Ronaldo). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima pergunta... Esta vale 2 pontos!")
  print ("8 - Em que ano foi realizado o primeiro campeonato mundial de futebol?")
  sleep(3)
  print (f"""
  A. 1930
  B. 1946
  C. 1926
  D. 1938""")

  resposta8fut = input()

  if resposta8fut == "A" or resposta8fut == "a":
    pergunta8 = True
    pontos8 = pontos7+2
    print (f"Está correto! Muito bem! Ganhaste dois pontos! Tens agora {pontos8} ponto(s)")
  else:
    pergunta8 = False
    pontos8 = pontos7
    print ("Incorreto. A resposta correta era a A (1930). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima question...")
  print ("9 - Onde foi situado o último campeonato do mundo de futebol?")
  sleep(3)
  print (f"""
  A. Brasil
  B. Rússia
  C. França
  D. Inglaterra""")

  resposta9fut = input()

  if resposta9fut == "B" or resposta9fut == "b":
    pergunta9 = True
    pontos9 = pontos8+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos9} ponto(s)")
  else:
    pergunta9 = False
    pontos9 = pontos8
    print ("Incorreto. A resposta correta era a B (Rússia). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nVamos para a próxima...")
  print ("10 - Qual a seleção que mais venceu o campeonato mundial de futebol?")
  sleep(3)
  print (f"""
  A. Alemanha
  B. Argentina
  C. Brasil
  D. Portugal""")

  resposta10fut = input()

  if resposta10fut == "C" or resposta10fut == "c":
    pergunta10 = True
    pontos10 = pontos9+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos10} ponto(s)")
  else:
    pergunta10 = False
    pontos10 = pontos9
    print ("Incorreto. A resposta correta era a C (Brasil). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nNext question...")
  print ("11 - Quando foi a primeira edição da UEFA CHAMPIONS LEAGUE?")
  sleep(3)
  print (f"""
  A. 1980-1981
  B. 1955-1956
  C. 1976-1977
  D. 1971-1972""")

  resposta11fut = input()

  if resposta11fut == "B" or resposta11fut == "b":
    pergunta11 = True
    pontos11 = pontos10+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos11} ponto(s)")
  else:
    pergunta11 = False
    pontos11 = pontos10
    print ("Incorreto. A resposta correta era a B (1955-1956). Para a próxima acertas.")
  
  sleep(2)

  print ("\nNext pergunta...")
  print ("12 - Qual é o melhor marcador da UEFA CHAMPIONS LEAGUE?")
  sleep(3)
  print (f"""
  A. Cristiano Ronaldo
  B. Lionel Messi
  C. Pelé
  D. Ferenc Puskás""")

  resposta12fut = input()

  if resposta12fut == "A" or resposta12fut == "a":
    pergunta12 = True
    pontos12 = pontos11+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos12} ponto(s)")
  else:
    pergunta12 = False
    pontos12 = pontos11
    print ("Incorreto. A resposta correta era a A (Cristiano Ronaldo). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima...")
  print ("13 - Qual o melhor assistente da UEFA CHAMPIONS LEAGUE?")
  sleep(3)
  print (f"""
  A. Zinedine Zidane
  B. Lionel Messi
  C. Cristiano Ronaldo
  D. Ronaldinho Gaúcho""")

  resposta13fut = input()

  if resposta13fut == "C" or resposta13fut == "c":
    pergunta13 = True
    pontos13 = pontos12+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos13} ponto(s)")
  else:
    pergunta13 = False
    pontos13 = pontos12
    print ("Incorreto. A resposta correta era a C (Cristiano Ronaldo). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nPróxima...")
  print ("14 - Qual destas equipas nunca venceu a UEFA CHAMPIONS LEAGUE?")
  sleep(3)
  print (f"""
  A. Nottingham Forest
  B. Feyenoord
  C. Sporting CP
  D. Celtic""")

  resposta14fut = input()

  if resposta14fut == "C" or resposta14fut == "c":
    pergunta14 = True
    pontos14 = pontos13+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos14} ponto(s)")
  else:
    pergunta14 = False
    pontos14 = pontos13
    print ("Incorreto. A resposta correta era a C (Sporting). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nEstamos perto dos 90 minutos. Esta é a última questão! Vale a dobrar!")
  print ("15 - Qual a equipa com mais troféus desta competição?")
  sleep(3)
  print (f"""
  A. Real Madrid CF
  B. AC Milan
  C. FC Barcelona
  D. Liverpool FC""")

  resposta15fut = input()

  if resposta15fut == "A" or resposta15fut == "a":
    pergunta15 = True
    pontos15 = pontos14+2
    print (f"Está correto! Muito bem! Ganhaste dois pontos!")
  else:
    pergunta15 = False
    pontos15 = pontos14
    print ("Incorreto. A resposta correta era a A (Real Madrid CF).")

  sleep(2)

  if pergunta1 == False:
    pergunta1errada = "1"
  else:
    pergunta1errada = ""
  
  if pergunta2 == False:
    pergunta2errada = "2"
  else:
    pergunta2errada = ""
  
  if pergunta3 == False:
    pergunta3errada = "3"
  else:
    pergunta3errada = ""
  
  if pergunta4 == False:
    pergunta4errada = "4"
  else:
    pergunta4errada = ""
  
  if pergunta5 == False:
    pergunta5errada = "5"
  else:
    pergunta5errada = ""
  
  if pergunta6 == False:
    pergunta6errada = "6"
  else:
    pergunta6errada = ""
  
  if pergunta7 == False:
    pergunta7errada = "7"
  else:
    pergunta7errada = ""
  
  if pergunta8 == False:
    pergunta8errada = "8"
  else:
    pergunta8errada = ""
  
  if pergunta9 == False:
    pergunta9errada = "9"
  else:
    pergunta9errada = ""
  
  if pergunta10 == False:
    pergunta10errada = "10"
  else:
    pergunta10errada = ""
  
  if pergunta11 == False:
    pergunta11errada = "11"
  else:
    pergunta11errada = ""
  
  if pergunta12 == False:
    pergunta12errada = "12"
  else:
    pergunta12errada = ""
  
  if pergunta13 == False:
    pergunta13errada = "13"
  else:
    pergunta13errada = ""
  
  if pergunta14 == False:
    pergunta14errada = "14"
  else:
    pergunta14errada = ""

  if pergunta15 == False:
    pergunta15errada = "15"
  else:
    pergunta15errada = ""
    
  if pontos15 == 17:
    print (f"\nVamos ver o teu resultado... Tens {pontos15} pontos. Excelente! Pontuação máxima atingido. És um génio!")
    print("Até à proxima sabichão!")
  elif pontos15 < 17 and pontos15 >= 14:
    print (f"\nVamos ver o teu resultado... Tens {pontos15} pontos. Boa! Infelizmente, não conseguiste atingir a pontuação máxima. Falhaste a(s) pergunta(s): {pergunta1errada} {pergunta2errada} {pergunta3errada} {pergunta4errada}{pergunta5errada} {pergunta6errada} {pergunta7errada} {pergunta8errada}{pergunta9errada} {pergunta10errada} {pergunta11errada} {pergunta12errada}{pergunta13errada} {pergunta14errada} {pergunta15errada}")
    print ("Até à próxima!")
  elif pontos15 > 17 or pontos15 < 0:
    print (f"\nResultado manipulado/alterado detetado!")
  elif pontos15 == 0:
    print (f"\nPor acaso... Fizeste alguma coisa engraçadinho?! Tens 0 pontos. O teu trabalho vale népia!")
    print ("Adeus triste :(")
  else:
    print(f"\nVamos ver o teu resultado... Tens {pontos15} pontos. Podia ter sido melhor! Para a próxima consegues aventureiro. Falhaste a(s) pergunta(s): {pergunta1errada}{pergunta2errada}{pergunta3errada}{pergunta4errada}{pergunta5errada}{pergunta6errada}{pergunta7errada}{pergunta8errada}{pergunta9errada}{pergunta10errada}{pergunta11errada}{pergunta12errada}{pergunta13errada} {pergunta14errada} {pergunta15errada}")
    print ("Adeus!")

def geografia():
  print ("\nQue começe a viagem à volta do mundo!")

  sleep(2)

  print ("1 - Qual é a capital da Bélgica?")
  sleep(5)
  print (f"""
  A. Bruxelas
  B. Madrid
  C. Sófia
  D. Budapeste""")

  resposta1geo = input()
  pontos = 0

  if resposta1geo == "A" or resposta1geo == "a":
    pergunta1 = True
    pontos1 = pontos+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos1} ponto(s)")
  else:
    pergunta1 = False
    pontos1 = pontos
    print ("Incorreto. A resposta correta era a A (Bruxelas). Para a próxima consegues.")

  sleep(2)

  print ("\nProsseguindo...")
  print ("2 - Qual é a capital da Hungria?")
  sleep(3)
  print (f"""
  A. Berlim
  B. Viena
  C. Budapeste
  D. Pristina""")

  resposta2geo = input()

  if resposta2geo == "C" or resposta2geo == "c":
    pergunta2 = True
    pontos2 = pontos1+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos2} ponto(s)")
  else:
    pergunta2 = False
    pontos2 = pontos1
    print ("Incorreto. A resposta correta era a C (Budapeste). Para a próxima acertas.")

  sleep(2)

  print ("\nNext...")
  print ("3 - Qual é a capital da Finlândia? ")
  sleep(3)
  print (f"""
  A. Pristina
  B. Copenhaga
  C. Helsínquia
  D. Bratislava""")

  resposta3geo = input()

  if resposta3geo == "C" or resposta3geo == "c":
    pergunta3 = True
    pontos3 = pontos2+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos3} ponto(s)")
  else:
    pergunta3 = False
    pontos3 = pontos2
    print ("Incorreto. A resposta correta era a C (Helsínquia). Para a próxima acertas.")
  
  sleep(2)

  print ("\nContinuando...")
  print ("4 - Qual é a capital da Suiça?")
  sleep(3)
  print (f"""
  A. Dublim
  B. Roma
  C. Reiquiavique
  D. Berna""")

  resposta4geo = input()

  if resposta4geo == "D" or resposta4geo == "d":
    pergunta4 = True
    pontos4 = pontos3+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos4} ponto(s)")
  else:
    pergunta4 = True
    pontos4 = pontos3
    print ("Incorreto. A resposta correta era a D (Berna). Para a próxima acertas.")
  
  sleep(2)

  print ("\nSeguinte...")
  print ("5 - Qual é a capital da Colômbia?")
  sleep(3)
  print (f"""
  A. Bogotá
  B. Nicarágua
  C. São Jorge
  D. Cidade da Guatemala""")

  resposta5geo = input()

  if resposta5geo == "A" or resposta5geo == "a":
    pergunta5 = True
    pontos5 = pontos4+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos5} ponto(s)")
  else:
    pergunta5 = False
    pontos5 = pontos4
    print ("Incorreto. A resposta correta era a A (Bogotá). Para a próxima acertas.")

  sleep(2)

  print ("\nPróxima pergunta...")
  print ("6 - Onde está localizada a Guiné-Bissau?")
  sleep(3)
  print (f"""
  A. África
  B. Ásia
  C. Europa
  D. América""")

  resposta6geo = input()

  if resposta6geo == "A" or resposta6geo == "a":
    pergunta6 = True
    pontos6 = pontos5+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos6} ponto(s)")
  else:
    pergunta6 = False
    pontos6 = pontos5
    print ("Incorreto. A resposta correta era a A (África). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nPróxima questão...")
  print ("7 - Onde está localizada a República Dominicana do Congo?")
  sleep(3)
  print (f"""
  A. América
  B. África
  C. Europa
  D. Ásia""")

  resposta7geo = input()

  if resposta7geo == "b" or resposta7geo == "B":
    pergunta7 = True
    pontos7 = pontos6+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos7} ponto(s)")
  else:
    pergunta7 = False
    pontos7 = pontos6
    print ("Incorreto. A resposta correta era a B (África). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima pergunta... Esta vale 2 pontos!")
  print ("8 - Onde está localizada a Letónia?")
  sleep(3)
  print (f"""
  A. Europa 
  B. Ásia
  C. África
  D. América""")

  resposta8geo = input()

  if resposta8geo == "A" or resposta8geo == "a":
    pergunta8 = True
    pontos8 = pontos7+2
    print (f"Está correto! Muito bem! Ganhaste dois pontos! Tens agora {pontos8} ponto(s)")
  else:
    pergunta8 = False
    pontos8 = pontos7
    print ("Incorreto. A resposta correta era a A (Europa). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima question...")
  print ("9 - Onde está localizado o Vietname?")
  sleep(3)
  print (f"""
  A. América
  B. África
  C. Ásia
  D. Europa""")

  resposta9geo = input()

  if resposta9geo == "C" or resposta9geo == "c":
    pergunta9 = True
    pontos9 = pontos8+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos9} ponto(s)")
  else:
    pergunta9 = False
    pontos9 = pontos8
    print ("Incorreto. A resposta correta era a C (Ásia). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nVamos para a próxima...")
  print ("10 - Onde está localizada a Malásia?")
  sleep(3)
  print (f"""
  A. Europa
  B. Ásia
  C. África
  D. América""")

  resposta10geo = input()

  if resposta10geo == "B" or resposta10geo == "b":
    pergunta10 = True
    pontos10 = pontos9+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos10} ponto(s)")
  else:
    pergunta10 = False
    pontos10 = pontos9
    print ("Incorreto. A resposta correta era a B (Ásia). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nNext question...")
  print ("11 - Qual é a língua principal falada na Venezuela?")
  sleep(3)
  print (f"""
  A. Francês
  B. Espanhol
  C. Alemão
  D. Inglês""")

  resposta11geo = input()

  if resposta11geo == "B" or resposta11geo == "b":
    pergunta11 = True
    pontos11 = pontos10+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos11} ponto(s)")
  else:
    pergunta11 = False
    pontos11 = pontos10
    print ("Incorreto. A resposta correta era a B (Espanhol). Para a próxima acertas.")
  
  sleep(2)

  print ("\nNext pergunta...")
  print ("12 - Qual é a língua principal falada na Tailândia?")
  sleep(3)
  print (f"""
  A. Inglês 
  B. Tailandês
  C. Mandarim
  D. Espanhol""")

  resposta12geo = input()

  if resposta12geo == "B" or resposta12geo == "b":
    pergunta12 = True
    pontos12 = pontos11+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos12} ponto(s)")
  else:
    pergunta12 = False
    pontos12 = pontos11
    print ("Incorreto. A resposta correta era a B (Tailandês). Para a próxima acertas.")
  
  sleep(2)

  print ("\nPróxima...")
  print ("13 - Qual é a língua principal falada no Chipre?")
  sleep(3)
  print (f"""
  A. Espanhol
  B. Inglês 
  C. Turco
  D. Português""")

  resposta13geo = input()

  if resposta13geo == "C" or resposta13geo == "c":
    pergunta13 = True
    pontos13 = pontos12+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos13} ponto(s)")
  else:
    pergunta13 = False
    pontos13 = pontos12
    print ("Incorreto. A resposta correta era a C (Turco). Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nPróxima...")
  print ("14 - Qual é a língua principal falada na Suiça?")
  sleep(3)
  print (f"""
  A. Inglês  
  B. Alemão
  C. Espanhol
  D. Francês""")

  resposta14geo = input()

  if resposta14geo == "B" or resposta14geo == "b":
    pergunta14 = True
    pontos14 = pontos13+1
    print (f"Está correto! Muito bem! Ganhaste um ponto! Tens agora {pontos14} ponto(s)")
  else:
    pergunta14 = False
    pontos14 = pontos13
    print ("Incorreto. A resposta correta era a B (Alemão). Cuidado com a pergunta! O Alemão é a língua principal, ou seja a mais falada. 63% da população utiliza o Alemão como língua diária. Para a próxima acertas.")
  
  sleep(2)
  
  print ("\nEstamos perto do fim da viagem! Esta é a última questão! Vale a dobrar!")
  print ("15 - Qual é a língua principal falada na Moldávia?")
  sleep(3)
  print (f"""
  A. Mandarim
  B. Inglês 
  C. Romeno
  D. Espanhol""")

  resposta15geo = input()

  if resposta15geo == "C" or resposta15geo == "c":
    pergunta15 = True
    pontos15 = pontos14+2
    print (f"Está correto! Muito bem! Ganhaste dois pontos!")
  else:
    pergunta15 = False
    pontos15 = pontos14
    print ("Incorreto. A resposta correta era a C (Romeno).")

  sleep(2)

  if pergunta1 == False:
    pergunta1errada = "1"
  else:
    pergunta1errada = ""
  
  if pergunta2 == False:
    pergunta2errada = "2"
  else:
    pergunta2errada = ""
  
  if pergunta3 == False:
    pergunta3errada = "3"
  else:
    pergunta3errada = ""
  
  if pergunta4 == False:
    pergunta4errada = "4"
  else:
    pergunta4errada = ""
  
  if pergunta5 == False:
    pergunta5errada = "5"
  else:
    pergunta5errada = ""
  
  if pergunta6 == False:
    pergunta6errada = "6"
  else:
    pergunta6errada = ""
  
  if pergunta7 == False:
    pergunta7errada = "7"
  else:
    pergunta7errada = ""
  
  if pergunta8 == False:
    pergunta8errada = "8"
  else:
    pergunta8errada = ""
  
  if pergunta9 == False:
    pergunta9errada = "9"
  else:
    pergunta9errada = ""
  
  if pergunta10 == False:
    pergunta10errada = "10"
  else:
    pergunta10errada = ""
  
  if pergunta11 == False:
    pergunta11errada = "11"
  else:
    pergunta11errada = ""
  
  if pergunta12 == False:
    pergunta12errada = "12"
  else:
    pergunta12errada = ""
  
  if pergunta13 == False:
    pergunta13errada = "13"
  else:
    pergunta13errada = ""
  
  if pergunta14 == False:
    pergunta14errada = "14"
  else:
    pergunta14errada = ""

  if pergunta15 == False:
    pergunta15errada = "15"
  else:
    pergunta15errada = ""
    
  if pontos15 == 17:
    print (f"Vamos ver o teu resultado... Tens {pontos15} pontos. Excelente! Pontuação máxima atingido. És um génio!")
    print("Até à proxima sabichão!")
  elif pontos15 < 17 and pontos15 >= 14:
    print (f"""Vamos ver o teu resultado... Tens {pontos15} pontos. Boa! Infelizmente, não conseguiste atingir a pontuação máxima. Falhaste a(s) pergunta(s): {pergunta1errada} {pergunta2errada} {pergunta3errada} {pergunta4errada}{pergunta5errada} {pergunta6errada} {pergunta7errada} {pergunta8errada}{pergunta9errada} {pergunta10errada} {pergunta11errada} {pergunta12errada}{pergunta13errada} {pergunta14errada} {pergunta15errada}""")
    print ("Até à próxima!")
  elif pontos15 > 17 or pontos15 < 0:
    print (f"Resultado manipulado/alterado detetado!")
  elif pontos15 == 0:
    print (f"Por acaso... Fizeste alguma coisa engraçadinho?! Tens 0 pontos. O teu trabalho vale népia!")
    print ("Adeus triste :(")
  else:
    print(f"Vamos ver o teu resultado... Tens {pontos15} pontos. Podia ter sido melhor! Para a próxima consegues aventureiro. Falhaste a(s) pergunta(s): {pergunta1errada} {pergunta2errada} {pergunta3errada} {pergunta4errada}{pergunta5errada} {pergunta6errada} {pergunta7errada} {pergunta8errada} {pergunta9errada} {pergunta10errada} {pergunta11errada} {pergunta12errada}{pergunta13errada} {pergunta14errada} {pergunta15errada}")
    print ("Adeus!")


if tema == "1":
  print ("\nEscolheste futebol. Queres prosseguir? (s/n)")
  respostatema = input()
  respostatematacs = respostatema == "s" or "S"
  respostatematacn = respostatema == "n" or "N"
  respostatematacindef = respostatema != "s" or resposta != "n" or resposta != "S" or resposta != "N"

  while respostatematacn == True:
    print ("""\nEscolhe outro tema:
    1 - Futebol (nivel de dificuldade -> fácil)
    2 - Geografia (nivel de dificuldade -> médio)""")
    tema = input()

    if tema == "1":
      print ("\nEscolheste futebol. Queres prosseguir? (s/n)")
      respostatema = input()
      respostatematacs = respostatema == "s" or "S"
      respostatematacn = respostatema == "n" or "N"
      respostatematacindef = respostatema != "s" or resposta != "n" or resposta != "S" or resposta != "N"
  
  futebol()

elif tema == "2":
  print ("\nEscolheste geografia. Queres prosseguir? (s/n)")
  respostatema = input()
  respostatematacs = respostatema == "s" or "S"
  respostatematacn = respostatema == "n" or "N"
  respostatematacindef = respostatema != "s" or resposta != "n" or resposta != "S" or resposta != "N"

  while respostatematacn == True:
    print ("""\nEscolhe outro tema:
    1 - Futebol (nivel de dificuldade -> fácil)
    2 - Geografia (nivel de dificuldade -> médio)""")
    tema = input()

    if tema == "2":
      print ("\nEscolheste geografia. Queres prosseguir? (s/n)")
      respostatema = input()
      respostatematacs = respostatema == "s" or "S"
      respostatematacn = respostatema == "n" or "N"
      respostatematacindef = respostatema != "s" or resposta != "n" or resposta != "S" or resposta != "N"
  
  geografia()

