def prix_menu (nom_menu: str, avecBoisson: bool = False, nb_supplement: int = 0)-> float:
    if nom_menu == "Basique":
        prix = 9
        
    elif nom_menu == "Gourmand":
        prix = 15
    elif nom_menu == "Complet":
        prix = 19    
    if avecBoisson:
        prix += 4

    prix += nb_supplement * 1.5

    return prix
	
def table_Dupont ()-> float:
    
    total = 0
    total += prix_menu("Basique")  # Jacqueline
    total += prix_menu("Gourmand", avecBoisson=True)  # Michel
    total += prix_menu("Basique", nb_supplement=2)  # Johanna
    total += prix_menu("Basique", avecBoisson=True, nb_supplement=1)  # Antoine
    return total
