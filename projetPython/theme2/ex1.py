        
            
            
            
reponse = input("Lancement de la gestion des comptes ? ")

if reponse != "oui":
    print("OK. À bientôt.")
else:
    solde_guillaume = float(input("Solde du compte de Guillaume ? "))
    solde_marion = float(input("Solde du compte de Marion ? "))

    if solde_guillaume >= 0 and solde_marion >= 0:
        print("Tous les deux en positif !")

    elif solde_guillaume < 0 and solde_marion < 0:
        print("Tous les deux en négatif !")
        print("Impossible de rétablir la situation.")

    else:
        if solde_guillaume < 0:
            print("Guillaume est en négatif.")
            if solde_marion > 0:
                print("Marion peut lui transférer.")
            else:
                print("Impossible de rétablir la situation.")

        if solde_marion < 0:
            print("Marion est en négatif.")
            if solde_guillaume > 0:
                print("Guillaume peut lui transférer.")
            else:
                print("Impossible de rétablir la situation.")
            