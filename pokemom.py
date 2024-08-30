#Ataque pokemom

while True: 
	dano=float()
	print("\nSólo hay 4 tipos de Pokémon: Agua(1), Fuego(2), Planta(3) y Eléctrico(4)")
	atacante=input("\nTipo del Pokémon atacante: ")
	defensor=input("\nTipo del Pokémon defensor: ")
	ata=input("\nAtaque: Entre 1 y 100: ")
	defe=input("\nDefensa: Entre 1 y 100: ")
	if atacante.isdigit() and (int(atacante)>0 and int(atacante)<5):
		if defensor.isdigit() and (int(defensor)>0 and int(defensor)<5):
			if ata.isdigit() and (int(ata)>0 and int(ata)<=100) and defe.isdigit() and (int(defe)>0 and int(defe)<=100):
				if atacante=="1":
					dano=50*(int(ata)/int(defe))*2
				elif atacante=="2":
					dano=50*(int(ata)/int(defe))*2
				elif atacante=="3":
					dano=50*(int(ata)/int(defe))*0.5
				elif atacante=="4":
					dano=50*(int(ata)/int(defe))*1.5
				print("\nEl daño sufrido por el defensor es: ",round(dano,2))
				break
			else:
				print("\nAlgo salio mal")
				break
		else:
			print("\nAlgo salio mal")
			break
	else:
		print("\nAlgo salio mal")
		break 