#de Binario a decial

def binde(valor1):
	c=1
	sumando=0
	while c<=len(valor1):
		sumando=((int(valor1[-1*c])*2)**(c-1))
		c +=1
	print("\nEl valor decimal es: ",sumando)


binario=input("\nIntroduzca su numero Binario: ")
c=0
tabla=list()
hasta=len(binario)-1
while c<=hasta:
	tabla.append(binario[c])
	c +=1
for i in tabla:
	if not (i=="1" or i=="0"):
		print("\nNo es un numero binario....")
		exit()
binde(tabla)