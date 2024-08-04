# En Mayusculas
def mayuscula(primera):
	#parrafo=primera.split()
	#print(primera[0].upper())
	sw=0
	c=0
	respuesta=str()
	for i in primera:
		if sw==0:
			respuesta=respuesta+primera[c].upper()
			sw=1
		else:
			respuesta=respuesta+primera[c]
		if i==" ":
			sw=0
		c +=1
	print(respuesta)

palabra=input("Introduzca un texto: ")
mayuscula(palabra)
