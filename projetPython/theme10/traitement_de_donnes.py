# Exemple de lecture de données
nom_fichier = "resultats-donnes1.txt"  # Remplacez par le nom de votre fichier
#lignes = import_lignes(nom_fichier)

# Afficher les lignes lues
#for ligne in lignes:
    #print(ligne.strip())
    
def import_lignes(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
    return lignes
    