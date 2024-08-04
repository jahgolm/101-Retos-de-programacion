#Leyendo un archivo y ejecutando las poeraciones matematicas

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