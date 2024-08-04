# Cuantos dias

from datetime import datetime,timedelta

def contador(f1,f2):
	fechaconv1 = datetime.strptime(f1, '%d/%m/%Y').date()
	fechaconv2 = datetime.strptime(f2, '%d/%m/%Y').date()
	opera=(fechaconv1-fechaconv2)
	finalizando=(str(opera).split())
	print("Los dias de separacion entre fechas es: ",int(finalizando[0])*-1)
fecha1=input("Introduzca la fecha 1 a calcular: ")
fecha2=input("Introduzca la fecha 2 a calcular: ")

try:
	fechaconv1 = datetime.strptime(fecha1, '%d/%m/%Y').date()
	fechaconv2 = datetime.strptime(fecha2, '%d/%m/%Y').date()
	contador(fecha1,fecha2)
except:
	print("Debe incluir formato de fecha correcta....")