# DIbujar cuadrados y tiangulos

def paint(valor1,valor2):
	pintar=str()
	if valor1=="C":
		c=1
		while c<=valor2:
			for i in range(valor2):
				pintar=pintar+"*"
			print(pintar)
			c +=1
			pintar=str()
	else:
		if valor2==2:
			print("Debe incluir una base mayor a 2....")
		else:
			c=1
			while c<=valor2:
				if c==1:
					print("*")
				else:
					for i in range(c):
						pintar=pintar+"*"
					print(pintar)
					pintar=str()
				c +=1

formas=input("Introduzca la figura a dibujar: T=Triangulo, C=Cuadrado: ")
tamano=input("Introduzca el tamaño. del triangulo sera la base: ")
paint(formas,int(tamano))