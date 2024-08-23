def segundo(valor1):
	print("\nArreglo cargado: ",valor1)
	c=0
	mayor=0
	resultado=list()
	i=1
	while i<=2:
		while c<len(valor1):
			if valor1[c]>mayor:
				mayor=valor1[c]			
			c +=1
		resultado.append(mayor)
		valor1.remove(mayor)
		mayor=0
		c=0
		i +=1

	print("El segundo valor mayor es: ",resultado[1])

arreglo=list()
while True:
	listado=input("Introduzca un listado de numeros: ")
	arreglo.append(int(listado))
	finalizar=input("\nDesea Continuar (s/n): ")
	if finalizar.upper()=="N":
		segundo(arreglo)
		break