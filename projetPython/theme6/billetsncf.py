def tarif_carte(nom_carte):
    if nom_carte == "jeune" :
        return(50)
    elif nom_carte == "seniore":
        return (60)
    else:
        print("carte inconnue")
        return None


    
    
def plein_tarif(depart , arrivee ):  
    trajet = {
        ("Grenoble","Paris") : 100,
        ("Grenoble ", "Lyon") :20 ,
        ("Lyon","Paris") :80 ,
        ("Paris","Grenoble") : 100,
        ("Lyon ", "Grenoble") :20 ,
        ("Paris","Lyon") :80 ,
    }   
    
    tarif = trajet[(depart , arrivee )]
    
    #return prix
    
    #Si le trajet demandé n'est aucun des 6 trajets existants dans cet exercice, la fonction affichera "Trajet inconnu" et renverra None (ou rien).
    if tarif is None :
        print("tajet inconnue")
        return None 
    return tarif
def tarif_billet(depart , arrivee,modifiable = True , carte = None , periode = None):
#utiliser tarif carte
    tarif = plein_tarif(depart, arrivee)
    if tarif is None:
        return None
    
   #recuction liee a la carte 
    if carte is not None :
        if carte not in ["jeune", "senior"]:
            print("carte inconnue")
            return None
        if periode == "bleue":
            if carte in ["jeune", "senior"]:
                tarif *= 0.5
        
        if periode == "blanche ":
            if carte == "jeune":
                tarif *= 0.7   
            if carte == "senior":
                tarif *= 0.75
            else:
                print("Période inconnue ou non précisée")
                return None    
    else :
        if not modifiable:
            tarif *= 0.9  
                
                      
        
        

    
    return tarif











