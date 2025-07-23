

début = int(input("Numero de début:"))
fin= int(input("Numero de fin:"))
nb_z = int(input("Nombre de z: "))


if fin < début:
    print("Rien ne s'affiche")
else:

    zigzag_str = "z" * (nb_z + 1) + "igzag"


    for i in range(début, fin + 1):
        if i % 2 == 0:
            
            print(f"{i} {zigzag_str}")
        else:
            
            print(f"{zigzag_str} {i}")







