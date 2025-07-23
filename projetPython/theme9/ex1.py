# stock ={'pomme' : 2, 'banane' : 6}
def ajout1(stock ,fruit):
#on donne un dictiojnair vide 
    nouveau_stock = {}
    for cle, valeur in stock.items():
        nouveau_stock[cle] = valeur
        if fruit in nouveau_stock:
            nouveau_stock[fruit] += 1
        else:    
            nouveau_stock[fruit] = 1
            
    return nouveau_stock



def enleve1(stock, fruit):
    # Copier le stock pour ne pas modifier l'original
    nouveau_stock = {}
    for cle, valeur in stock.items():
        nouveau_stock[cle] = valeur

    if fruit not in nouveau_stock:
        print(f"Erreur: quantité insuffisante de {fruit}")
        return stock  # Retourne le stock original non modifié
    
    if nouveau_stock[fruit] < 1:
        print(f"Erreur: quantité insuffisante de {fruit}")
        return stock  # Retourne le stock original non modifié

    # Sinon, on enlève un fruit
    nouveau_stock[fruit] -= 1

    # Si la quantité tombe à 0, on supprime la clé
    if nouveau_stock[fruit] == 0:
        del nouveau_stock[fruit]

    return nouveau_stock



def apres_livraison(stock, livraison):
    nouveau_stock = {}
    # Copier le stock initial
    for fruit, quantite in stock.items():
        nouveau_stock[fruit] = quantite
    
    # Ajouter les fruits de la livraison
    for fruit, quantite in livraison.items():
        if fruit in nouveau_stock:
            nouveau_stock[fruit] += quantite
        else:
            nouveau_stock[fruit] = quantite
    
    return nouveau_stock

def commande(stock, stock_voulu):
    commande_a_faire = {}
    for fruit, quantite_voulue in stock_voulu.items():
        quantite_actuelle = stock.get(fruit, 0)  # Si le fruit n'existe pas dans le stock, quantité = 0
        if quantite_actuelle < quantite_voulue:
            commande_a_faire[fruit] = quantite_voulue - quantite_actuelle
    return commande_a_faire


def total(stock):
    somme = 0
    for quantite in stock.values():
        somme += quantite
    return somme


def quantite(stock, fruits_a_compter):
    total_fruits = 0
    for fruit in fruits_a_compter:
        if fruit in stock:
            total_fruits += stock[fruit] #si oui, ajouter sa quantité au compteur total_fruits
    return total_fruits

def quantite_agrumes(stock):
    agrumes = ['orange', 'citron', 'mandarine', 'clementine', 'pamplemousse']
    total = 0
    for fruit in agrumes:
        if fruit in stock:
            total += stock[fruit]
    return total
