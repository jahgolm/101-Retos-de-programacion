# Transformar celsius a Fahrenheit

def calculo(valor1):
	numero=float(valor1[0:(len(valor1))-2])
	if valor1[-1]=="C":
		print("\nCelsius")
		resultado=((numero*9)/5)+32
	else:
		print("\nFahrenheit")
		resultado=((numero-32)*5)/9
	print("\nEl resultado es: ",resultado,"º",valor1[-1])

tempera=input("\nIngrese la temperatura con el formato 72ºC o 72ºF: ")

if "º" in tempera and ("C" in tempera or "F" in tempera):
	calculo(tempera)
else:
	print("\n Error.... Formato de temperatura no correcto....")