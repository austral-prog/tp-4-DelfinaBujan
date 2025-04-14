def leap_year():
    Año=int(input("Ingrese un año: "))
    if Año%4 == 0 :
	    if Año%100== 0 and not Año%400==0:
		print(f"El {Año} no es bisiesto")
	    else:
		print(f"El {Año} es bisiesto")
    else:
	    print(f"El {Año} no es bisiesto")
