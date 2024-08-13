#Maquina expendedora

def vuelto(para1,para2,precio):
	billete=list()
	monedas=["0.5","1","2","5","10","20","50","100"]
	devolucion=float(para2)-float(precio[para1])
	hasta=monedas.index(para2)
	contador=0
	while hasta>=0:
		hasta -=1
		if contador+float(monedas[hasta])<=devolucion:
			contador=contador+float(monedas[hasta])
			billete.append(monedas[hasta])

	print("\nMonedas o billetas a devolver: ", billete)

productos={
	"1":"Pepito",
	"2":"Papitas",
	"3":"Cotufas",
	"4":"Chupetas",
	"5":"Galletas",
	"6":"Gaseosas",
	"7":"Chicle"
}
maquina={
	"1":2,
	"2":2.5,
	"3":1.5,
	"4":1,
	"5":2,
	"6":3,
	"7":1.5
}

while True:
	for i in productos:
		print(i,"-",productos[i],"-",maquina[i])
	try:	
		escoge=input("\nIntroduzca el producto a escoger: ")
		monto=input("Introduzca el monto a pagar: ")
		print("\nProducto escogido es: ",productos[escoge])
		vuelto(escoge,monto,maquina)
	except:
		print("\nProducto No existe.....")	
		break

