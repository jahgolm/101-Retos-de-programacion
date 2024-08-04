# número de Armstrong

def armstrong(valor):
	posiciones=len(valor)
	acum=0
	for i in valor:
		acum=acum+(int(i)**int(len(valor)))
	if int(valor)==int(acum):
		print("Este es un numero Armstrong.....")
	else:
		print("Este NO es un numero Armstrong...")
numero=input("Introduzca un numero: ")
if int(numero)>0:
	armstrong(numero)
else:
	print("Debe incluir un numero entero positivo...")
