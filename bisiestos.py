# Años Bisiestos

def verificar(argu1):
	c=0
	while c<=30:
		if (argu1+c)%4==0 and not (argu1+c)%100==0:
			print(argu1+c)
		elif (argu1+c)%4==0:
			print(argu1+c)
		c +=1

print("RECUERDE. Se verificaran los proximos 30 años")
comienzo=input("\nIntroduzca el año a comenzar a verificar: ")
verificar(int(comienzo))