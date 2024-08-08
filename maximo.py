def minimo(num1,num2):
	mcm1=dict()
	mcm2=dict()
	while True:
		if num1%2==0:
			resul=num1/2
			mcm1[num1]=2
			num1=int(resul)
		else:
			if num1%3==0:
				resul=num1/3
				mcm1[num1]=3
				num1=int(resul)
			else:
				if num1%5==0:
					resul=num1/5
					mcm1[num1]=5
					num1=int(resul)
				else:
					if num1%7==0:
						resul=num1/7
						mcm1[num1]=7
						num1=int(resul)
					else:
						break
	print(mcm1)

	while True:
		if num2%2==0:
			resul=num2/2
			mcm2[num2]=2
			num2=int(resul)
		else:
			if num2%3==0:
				resul=num2/3
				mcm2[num2]=3
				num2=int(resul)
			else:
				if num2%5==0:
					resul=num2/5
					mcm2[num2]=5
					num2=int(resul)
				else:
					if num2%7==0:
						resul=num2/7
						mcm2[num2]=7
						num2=int(resul)
					else:
						break
	print(mcm2)
	minimo2=0
	if list(mcm1.values()).count(2)>list(mcm2.values()).count(2):
		minimo2=2**list(mcm2.values()).count(2)
	elif list(mcm1.values()).count(2)<list(mcm2.values()).count(2):
		minimo2=2**list(mcm1.values()).count(2)
	else:
		minimo2=2**list(mcm2.values()).count(2)
	
	minimo3=0
	if list(mcm1.values()).count(3)>list(mcm2.values()).count(3):
		minimo3=3**list(mcm2.values()).count(3)
	elif list(mcm1.values()).count(3)<list(mcm2.values()).count(3):
		minimo3=3**list(mcm1.values()).count(3)
	else:
		minimo3=3**list(mcm2.values()).count(3)

	minimo5=0
	if list(mcm1.values()).count(5)>list(mcm2.values()).count(5):
		minimo5=5**list(mcm2.values()).count(5)
	elif list(mcm1.values()).count(5)<list(mcm2.values()).count(5):
		minimo5=5**list(mcm1.values()).count(5)
	else:
		minimo5=5**list(mcm2.values()).count(5)


	minimo7=0
	if list(mcm1.values()).count(7)>list(mcm2.values()).count(7):
		minimo7=7**list(mcm2.values()).count(7)
	elif list(mcm1.values()).count(7)<list(mcm2.values()).count(7):
		minimo7=7**list(mcm1.values()).count(7)
	else:
		minimo7=7**list(mcm2.values()).count(7)

	print("\nEl maximo comun divisor es: ",minimo2*minimo3*minimo5*minimo7)

valor1=input("Introduzca primer valor: " )
valor2=input("Introduzca segundo Valor: ")
minimo(int(valor1),int(valor2))