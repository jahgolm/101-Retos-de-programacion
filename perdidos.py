#Numeros perdidos

def determina(valor1):
	valormax=max(valor1)
	respuesta=list()
	for i in range(valormax):
		if valor1.count(i)==0: 
			respuesta.append(i)
	print("\nNumeros Perdidos: ",respuesta)

arreglo=list()
while True:
	numeros=input("\nIntroduzca los numeros del array: ")
	if numeros.isdigit() and arreglo.count(numeros)==0:
		arreglo.append(int(numeros))
	else:
		print("\nDebe incluir solo digitos / Ya esta incluido en el arreglo......")
	continuar=input("\nDesea continuar incluyendo digitos: S/N:  ")
	if continuar.upper()=="N":
		arreglo==arreglo.sort()
		print("\nNumeros introducidos: ",arreglo)
		determina(arreglo)
		break