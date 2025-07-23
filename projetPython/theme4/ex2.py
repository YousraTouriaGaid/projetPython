"""
        Ecrire un programme qui demande à l'utilisateur plusieurs nombres 
    successivement en affichant "Nombre ?" jusqu'à ce que l'utilisateur entre le nombre 0. 
    Le programme doit alors afficher "Tous -", ou "Tous +", ou "Seulement 0", ou "Ni tous +, 
    ni tous -" selon que l'utilisateur n'a rentré que des nombres négatifs, ou bien que des nombres positifs, 
    ou bien seulement zéro, ou bien aucun des cas précédents. Dans ce dernier cas (Ni tous +, ni tous -), le programme doit afficher "Somme -", ou "Somme=0", ou "Somme +" selon que la somme totales des nombres donnés par l'utilisateurs
    est strictement négative, nulle ou strictement positive.
    """
    

            
            
            
nombres = []
somme = 0


while True:
    n = int(input("Nombre ? "))
    if n == 0:
        break
    nombres.append(n)
    somme += n
    

if not nombres:
    print("Seulement 0")
elif all(x > 0 for x in nombres):
    print("Tous +")
elif all(x < 0 for x in nombres):
    print("Tous -")
else:
    print("Ni tous +, ni tous -")
    if somme > 0:
        print("Somme +")
    elif somme < 0:
        print("Somme -")
    else:
        print("Somme = 0")            