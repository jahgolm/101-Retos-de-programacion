# tres en raya

matriza={"A1":" ","A2":" ","A3":" "}
matrizb={"B1":" ","B2":" ","B3":" "}
matrizc={"C1":" ","C2":" ","C3":" "}
c=1
x=0
o=1
while c<=9:
	fila=input("Introduzca Fila A,B,C: ")
	colu=input("Introduzca columna 1,2,3: ")
	veri=fila+colu
	print(veri)
	if x==0:
		if fila=="A" and matriza.get(veri)==" ":
			matriza[veri]="X"
			print(matriza)
			c +=1
			x=1
		elif fila=="B" and matrizb.get(veri)==" ":
			matrizb[veri]="X"
			print(matrizb)
			c +=1
			x=1
		elif fila=="C" and matrizc.get(veri)==" ":
			matrizc[veri]="X"
			print(matrizc)
			c +=1
			x=1
		else:
			print("Ya fue marcada la opcion")
		
	else:
		if fila=="A" and matriza.get(veri)==" ":
			matriza[veri]="O"
			print(matriza)
			c +=1
			x=0
		elif fila=="B" and matrizb.get(veri)==" ":
			matrizb[veri]="O"
			print(matrizb)
			c +=1
			x=0
		elif fila=="C" and matrizc.get(veri)==" ":
			matrizc[veri]="O"
			print(matrizc)
			c +=1
			x=0
		else:
			print("Ya fue marcada la opcion2")
print("\n Resultado final \n")
print(matriza.values())
print(matrizb.values())
print(matrizc.values())

if matriza["A1"]==matrizb["B1"] and matrizc["C1"]==matrizb["B1"]:
	print("\n A ganado "+matriza["A1"])
elif matriza["A2"]==matrizb["B2"] and matrizc["C2"]==matrizb["B2"]:
	print("\n A ganado "+matriza["A2"])
elif matriza["A3"]==matrizb["B3"] and matrizc["C3"]==matrizb["B3"]:
	print("\n A ganado "+matriza["A3"]) 
elif matriza["A1"]==matriza["A2"] and matriza["A2"]==matriza["A3"]:
	print("\n A ganado "+matriza["A1"])
elif matrizb["B1"]==matrizb["B2"] and matrizb["B2"]==matrizb["B3"]:
	print("\n A ganado "+matrizb["B1"])
elif matrizc["C1"]==matrizc["C2"] and matrizc["C2"]==matrizc["C3"]:
	print("\n A ganado "+matrizc["C1"])
elif matriza["A1"]==matrizb["B2"] and matrizb["B2"]==matrizc["C3"]:
	print("\n A ganado "+matriza["A1"])
elif matrizc["C1"]==matrizb["B2"] and matrizb["B2"]==matriza["A3"]:
	print("\n A ganado "+matrizb["B2"])
else:
	print("\n Nadie gano")

