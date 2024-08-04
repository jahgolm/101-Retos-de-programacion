#9DecimalaBinario

def bin(numero):
	c=numero
	r=0
	resto=list()
	whilec>=1:
		c=int(numero)/2
		r=int(numero)%2
		#resto=resto+str(r)
		resto.insert(0,str(r))
		numero=c
	s="".join(resto)
	print("El Binario del numero introducido es:"+s)

valor=input("Introduzcalacantidad:")
bin(int(valor))