# Bumeran

def boomerang(valor1):
	i=0
	j=list()
	b1=0

	while i<len(valor1):
		b1=valor1[i]
		if not i+3>len(valor1):
			if b1==valor1[i+2]:
				j.append(b1)
				j.append(valor1[i+1])
				j.append(valor1[i+2])
				print("\n",b1,",",valor1[i+1],",",valor1[i+2])
				i +=3
				b1=0
			else:
				i +=1
		else:
			i +=1

numeros=list()

while True:
	v=input("\nIntroduzca Numeros del boomerang: ")
	if not v.isdigit():
		print("\nNo es un numero....")
	else:
		numeros.append(v)
		resp=input("\nDesea continuar incluyendo numeros....(S/N): ")
		if resp.upper()=="N":
			boomerang(numeros)
			break