#ContandoPalabras

def contando(texto):
	texto=texto.replace(",","")
	texto=texto.replace(".","")
	prueba1=texto.split()
	prueba2=[]
	for x in prueba1:
		if x not inprueba2:
			prueba2.append(x)
	c=0
	for i in prueba2:
		for j in prueba1:
			if j.lower()==i.lower():
				c+=1
		print("Lapalabra:"+i+",serepite:"+str(c))
		c=0
palabras=input("Incluya el texto a evaluar:")
contando(palabras)
