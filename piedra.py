# Piedra, papel o tijera

def ganador(player1,player2,movimientos):
	resultado1=0
	resultado2=0
	i=0
	while i<len(movimientos)-1:		
		if (movimientos[i]=="R" and movimientos[i+1]=="P"):
			resultado2 +=1
		elif (movimientos[i]=="P" and movimientos[i+1]=="R"):
			resultado1 +=1
		if (movimientos[i]=="R" and movimientos[i+1]=="S"):
			resultado1 +=1
		elif (movimientos[i]=="S" and movimientos[i+1]=="R"):
			resultado2 +=1
		if (movimientos[i]=="S" and movimientos[i+1]=="P"):
			resultado1 +=1
		elif (movimientos[i]=="P" and movimientos[i+1]=="S"):
			resultado2 +=1
		i +=2	
	if resultado1>resultado2:
		print("\nEl ganador es PLAYER 1.....")
	elif resultado1<resultado2:
		print("\nEl ganador es PLAYER 2.....")
	else:
		print("\nEmpate.....")

jugadas=list()
while True:
	print("R=(piedra), P=(papel) o S=(tijera)")
	jugador1=input("\nMuestra tu mano jugador 1: ")
	jugador2=input("Muestra tu mano jugador 2: ")
	continuar=input("\nDeseas ver los resultados S/N: ")
	jugadas.append(jugador1)
	jugadas.append(jugador2)
	if continuar=="N":
		ganador(jugador1,jugador2,jugadas)
		break