def chino(valor1):
	animal=["Rata","Buey","Tigre","Conejo","Dragon","Serpiente","Caballo","Oveja","Mono","Gallo","Perro","Cerdo"]
	material=["Madera","Madera","Fuego","Fuego","Tierra","Tierra","Metal","Metal","Agua","Agua"]
	modulo=(valor1-1924)%12
	modulo2=(valor1-1924)%10
	print(valor1," Signo del zodiaco: ",animal[modulo], "Wu Xing: ",material[modulo2])

year=input("\nIntroduzca el año a consultar: ")
chino(int(year))