#Invirtiendocadenas

def invirtiendo(palabras):
	c=0
	result=str()
	for i in palabras:
		c=c+1	
		result=result+palabras[c*-1]
	print("La palabra invertida es:",result)
frases=input("Introduzca frase:")
invirtiendo(frases)
