#Marco de palabras

def marco(argu1):
	mayor=0
	for i in argu1.split():
		if len(i)>mayor:
			mayor=len(i)
	c=1
	mayor=mayor+4
	barra=str()
	while c<=mayor:
		barra=barra+("*")
		c +=1
	print(barra)
	c=0
	for i in argu1.split():
		c=3+len(i)
		espacio=str()
		while c<mayor:
			espacio=espacio+" "
			c +=1
		print("* "+i+espacio+"*")
	print(barra)

palabra=input("Introduzca el parrafo a enmarcar: ")
marco(palabra)