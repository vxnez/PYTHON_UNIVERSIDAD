#BRAYAN IVAN FUENTES AREVALO
#236W0315


lista=["cheetos",17,"coca",17,"chocokrispis",75,"leche",250,"aceite",30,"fricoles",40]
lista.append("Boing")
lista.append(16)
lista.append("Tortillinas")
lista.append(32)

listaElec=["placha",1200,"refrigerador",7000,"microondas",1500,"lavadora",10000,"estufa",10000]
listaElec.append("Licuadora")
listaElec.append(1200)
listaElec.append("tostadora")
listaElec.append(1200)

listaVide=["Minecraft",1000,"Call of Duty",1200,"Dark Souls",2000,"Gear of War",1800]
listaVide.append("GTA")
listaVide.append(900)
listaVide.append("Sony")
listaVide.append(1400)

#ELIMINAMOS ELEMENTOS DE LA LISTA
    #ELEMENTO ELIMINADO DE COMESTIBLES
lista.remove("Boing")
lista.remove(16)
    #ELEMENTO ELIMINADO DE ELECTRODOMESTICOS
listaElec.remove("refrigerador")
listaElec.remove(7000)
    #ELEMENTO ELIMINADO DE VIDEOJUEGOS
listaVide.remove("Minecraft")
listaVide.remove(1000)

#LISTA DE COMESTIBLES 
print("============================")
print("LISTA DE COMESTIBLES")
print("============================\n")
for comestible in lista:
    print(comestible)
#LISTA DE ELECTRODOMESTICOS
print("============================")
print("LISTA DE ELECTRODOMESTICOS")
print("============================\n")
for electrodomestico in listaElec:
    print(electrodomestico)
#LISTA DE VIDEOJUEGOS
print("============================")
print("LISTA DE VIDEOJUEGOS")
print("============================\n")
for videojuego in listaVide:
    print(videojuego)