def ordenar(valor1,valor2):
	ordenado=list()
	lista2=valor1
	if valor2=="M":
		for j in range(len(valor1)):	
			mayor=valor1[0]
			for i in valor1:
				if mayor<=i:
					mayor=i
			ordenado.append(mayor)
			valor1.remove(mayor)
		print("\nLista ordenada de mayor a menor: ",ordenado)
	else:
		for j in range(len(valor1)):	
			menor=valor1[0]
			for i in valor1:
				if menor>=i:
					menor=i
			ordenado.append(menor)
			valor1.remove(menor)
		print("\nLista ordenada de Menor a mayor: ",ordenado)

lista=list()
while True:
	numero=input("Introduzca un numero: ")
	if numero.isdigit():
		lista.append(numero)
	else:
		orden=input("\nIndica M si es mayor a menor y N si es de menor a mayor: ")
		ordenar(lista,orden)
		break



