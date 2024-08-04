# Conversor de tiempo

def conversor(milidias,milihoras,miliminutos,miliseg):
	result=0
	result=(int(miliseg)/0.001)
	result=result+(int(miliminutos)*60/0.001)
	result=result+(int(milihoras)*3600/0.001)
	result=result+((int(milidias)*24)*3600/0.001)
	print("El resultado es: "+str(result)+" miliseg")

dias=input("Introduce dia: ")
horas=input("Introduce hora: ")
minutos=input("Introduce minutos: ")
segundos=input("Introduce segundos: ")

conversor(dias,horas,minutos,segundos)
