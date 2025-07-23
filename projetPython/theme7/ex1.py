def somme_pair(liste):
    somme = 0
    
    for i in liste:
        if i % 2 == 0:
            somme = somme + i
    return somme    

print(somme_pair([4, 7, 12, 0, 21, 5]))
    
def nb_elem_pairs (liste):  
    cpt =0
    for i in liste:
        if i % 2 == 0:
            cpt +=1
            
            return cpt 
print(nb_elem_pairs([4, 7, 12, 0, 21, 5]))    
    
    
    
def max_pair(liste):
    max = None
    

    for i in liste:
        if i % 2 == 0:
            if  max is None or i > max:#max is None or
                max = i

    return max


print(max_pair([4, 7, 12, 0, 21, 5]))  


def indice_de(entier, liste):
#je dois le terminer








def min_pair(liste):
    min_pair = None
    for i in liste:
        if i % 2 == 0:
            if min_pair is None or i < min_pair:
                min_pair = i
    return min_pair

print(min_pair([4, 7, 12, 1, 21, 5]))  # Résultat attendu : 4

    
    
      