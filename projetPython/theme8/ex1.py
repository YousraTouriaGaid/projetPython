def commence_par(lettre, mot):
    return mot[0] == lettre
print(commence_par('h', 'hello'))  
print(commence_par('e', 'roue'))   

def contient_voyelle(mot):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    for lettre in mot:
        if lettre in voyelles:
            return True
        return False


def derniere_consonne(mot):
    for i in range(len(mot) - 1, -1, -1):  # Parcours du mot à l'envers
        if not contient_voyelle(mot[i]):  # Si ce n'est pas une voyelle, donc une consonne
            return i, mot[i]

#DOUBLE CONSONNE PAS ENCORE
def double_consonne(mot:True):
     if not contient_voyelle(mot[i]):
        return consonne
    
def double_consonne(mot):
    for i in range(len(mot) - 1):
        if mot[i] == mot[i + 1] and not voyelle(mot[i]):
            return True, mot[i]
    return False, None    



def envers(li):
    resultat = []                      # Étape 1 : créer une liste vide
    for i in range(len(li) - 1, -1, -1):  # Étape 2 : parcourir la liste à l’envers
        resultat.append(li[i])        # Ajouter chaque élément à la liste résultat
    return resultat                   # Étape 3 : retourner la liste inversée



def envers(li):
    list = [] #j eai cree unenlist vid 
    for i in range(len[i]-1,-1,-1):#j ai parcourer la list a l enver
        list.apppend(li[i]) 
    return list    



def palindrome(mot):
    mot_inverse = mot[::-1] #inverser le mot
    if mot == mot_inverse:
        return True
    else:
        return False 
    

def mot_autorise (mot, liste_interdits):
    if mot in liste_interdits:
        return False
    else:
        return True
    
    