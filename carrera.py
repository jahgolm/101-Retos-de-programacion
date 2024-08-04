# Carrera de Obstaculos
hayvamos=str()
def carrera(corredor,actividad):
	global hayvamos
	if (corredor=="1" and actividad=="1") or (corredor=="2" and actividad=="2"):
		hayvamos=hayvamos+"bien"
	if (corredor=="2" and actividad=="1"):
		hayvamos=hayvamos+"x"
	elif (corredor=="1" and actividad=="2"):
		hayvamos=hayvamos+"/"
while True:
	atleta=input("El atleta esta: 1.- Run o 2.- Jump:  ")
	pista=input("lo q hace en la pista: 1.- Suelo o 2.- Valla:  ")
	carrera(atleta,pista)
	continuar=input("Indique el fin de la pista: (S/N):  ")
	if continuar=="S":
		printA("Recorrido del atleta varios tramos: ",hayvamos)
		break
