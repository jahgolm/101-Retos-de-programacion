#Factorial Recursivo

def factorial(valor):
	i=1
	factor=1
	while i<=valor:
			if i>1:
				factor=factor*(i-1)
			print(i * factor)
			i +=1
numero=input("Introduzca el numero factorial: ")
if int(numero)>0:
	factorial(int(numero))
else:
	print("Debe ser un numero mayor a 0") 
