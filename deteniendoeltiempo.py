# Parando el tiempo

def parando(valor1,valor2,espera):
	import time
	time.sleep(int(espera))
	print("\nResultado: "+str(int(numero1)+int(numero2)))

numero1=input("Introduzca primer numero: ")
numero2=input("Introduzca segundo numero: ")
tiempo=input("Introduzca el tiempo a esperar: ")
parando(numero1,numero2,tiempo)

def recorrido(nombre):
	import time
	import os
	try:
		operando=str()
		archivo=open(nombre,"r")
		for i in archivo.read().split():
			print(i)
			if not i=="=":
				operando=operando+i
			else:
				print("El resultado de la operacion es: ",eval(operando))
				operando=str()
	except:
		print("\nArchivo no se encuentra.....")
		time.sleep(5)
		os.system("cls")

file=input("Introduzca el nombre del archivo: ")
recorrido(file)