#legend of zelda
from datetime import datetime
from datetime import date
from datetime import timedelta

zelda1=input("\nIntroduzca fecha del primer juego de zelda: ")
zelda2=input("\nIntroduzca fecha del segundo juego de zelda: ")
try:
	zelda1new=datetime.strptime(zelda1, '%d/%m/%Y')
	zelda2new=datetime.strptime(zelda2, '%d/%m/%Y')
except:
	print("\nDebe ingresar fecha DD/MM/AAAA....")
else:
	resultado=zelda1new-zelda2new
	fresultado=str(format(resultado.days))
	if int(fresultado)>365:
		imprimir=int(fresultado)/365
		imprimir2=int(imprimir)
		imprimir3=int(fresultado)%365
		print("\nSon ",(imprimir2), "Años con ",imprimir3, "Dias")
	else:
		print("\nSon ",fresultado," Dias")

