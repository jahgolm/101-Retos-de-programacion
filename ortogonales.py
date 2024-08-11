#Determinar si dos vectores son ortogonales

def comunes(array1,array2):
	resp=0
	c=0
	while c<len(array1):
		resp=(array1[c]*array2[c])+resp
		c +=1
	if resp==0:
		print("\nLos vectores son ortogonales.....")
	else:
		print("\nLos vectores NO son ortogonales.....")

arreglo1=list()
arreglo2=list()
resp=str()
while True:
	arreglo1.append(int(input("\nIntroduzca valor del arreglo1: ")))
	arreglo2.append(int(input("\nIntroduzca valor del arreglo2: ")))
	resp=input("\n\nDesea continuar (S/N):")
	if resp=="N":
		comunes(arreglo1,arreglo2)
		break
