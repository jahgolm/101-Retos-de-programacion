#Ley de ohm

def buscarvol(valor1,valor2):
	resultado=valor1*valor2
	print("\nResultado de V es:",resultado)

def buscarcor(valor1,Valor2):
	resultado=valor1/valor2
	print("\nResultado de I es:",round(resultado,2))

def buscarre(valor1,valor2):
	resultado=valor1/valor2
	print("\nResultado de R es:",round(resultado,2))

voltaje=input("\nIntroduzca voltaje (V): ")
corriente=input("\nIntroduzca corriente (I): ")
resistencia=input("\nIntroduzca resistencia (R): ")

if(voltaje=="" and (corriente.isdigit() and resistencia.isdigit())):
	buscarvol(int(corriente),int(resistencia))
elif (corriente=="" and (voltaje.isdigit() and resistencia.isdigit())):
	buscarcor(int(voltaje),int(resistencia))
elif (resistencia=="" and (voltaje.isdigit() and corriente.isdigit())):
	buscarre(int(voltaje),int(corriente))
else:
	print("\nInvalid values")