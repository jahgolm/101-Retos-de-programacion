#valores comunes en los vectores

def comunes(array1,array2):
	numeros=list()
	numeros2=list()
	for i in array1:
		for j in array2:
			if i==j:
				if not numeros.count(i)==1:
					numeros.append(i)
	print("\nNumeros Comunes: ",numeros)
	for i in array1:
		sw=0
		for j in array2:
			if i==j:
				sw=1
		if sw==0:
			numeros2.append(j)
		else:
			sw=0	
	for j in array2:
		sw=0
		for i in array1:
			if j==i:
				sw=1
		if sw==0:
			numeros2.append(j)
		else:
			sw=0	
	print("\nNumeros no Comunes: ",numeros2)
		
arreglo1=list()
arreglo2=list()
resp=str()
while True:
	arreglo1.append(input("\nIntroduzca valor del arreglo1: "))
	arreglo2.append(input("\nIntroduzca valor del arreglo2: "))
	resp=input("\n\nDesea continuar (S/N):")
	if resp=="N":
		comunes(arreglo1,arreglo2)
		break