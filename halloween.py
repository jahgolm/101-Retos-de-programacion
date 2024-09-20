# halloween
import os
#import emoji
import random

def truco(valor1):
	susto=["calabaza","Fantasma","Calavera","Araña","Telaraña","Vampiro"]
	#cuantas=len(valor1)/3
	#print(cuantas)
	d=0
	while d<len(valor1):
		hasta=len(valor1[d])/2
		print(f"\nPor tener el nombre de: {valor1[d]}")
		c=1
		while c<=hasta:
			print(random.choice(susto))
			c +=1
		if float(valor1[d+1])%2==0:
			print(f"\nPor tener una edad {valor1[d+1]}")
			print(random.choice(susto))
			print(random.choice(susto))
		cada=float(valor1[d+2])/100
		print("\npor cada 100 cm de altura entre todas las personas")
		e=1
		while e<=int(cada):
			print(random.choice(susto))
			print(random.choice(susto))
			print(random.choice(susto))
			e +=1
		d +=3
	
def trato(valor1):
	dulces=["Torta","Caramelo","Helado","Chupeta","Galleta","Chocolate","Panquecito","Donas"]
	d=0
	while d<len(valor1):
		hasta=len(valor1[d])
		print(f"\nPor tener el nombre de: {valor1[d]}")
		c=1
		while c<=hasta:
			print(random.choice(dulces))
			c +=1

		cumplidos=float(valor1[d+1])/3
		print(f"\nPor tener una edad {valor1[d+1]}")
		anos=1
		while anos<=int(cumplidos) and anos<4:
			print(random.choice(dulces))
			anos +=1

		cada=float(valor1[d+2])/50
		print("\npor cada 50 cm de altura entre todas las personas")
		e=1
		while e<=int(cada):
			print(random.choice(dulces))
			print(random.choice(dulces))
			e +=1
		d +=3

personas=list()

while True:
	nombre=input("\nIntroduza su nombre: ")
	edad=input("\nEdad: ")
	altura=input("\nAltura en cm: ")
	personas.append(nombre)
	personas.append(edad)
	personas.append(altura)
	respuesta=input("\nDesea continuar agregando: (S/N): ")
	if respuesta.upper()=="S":
		os.system("cls")
	else:
		break

trucootrato=input("\nTruco o trato: ")
if trucootrato.upper()=="TRUCO":
	truco(personas)
elif trucootrato.upper()=="TRATO":
	trato(personas)
