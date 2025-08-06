# Exemple de lecture de données
nom_fichier = "resultats-donnes1.txt"  # Remplacez par le nom de votre fichier
#lignes = import_lignes(nom_fichier)

   
    
def import_lignes(nom_fichier):
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    return lignes

def separe(ligne):
    return ligne.strip().split()

def cree_patient(ligne):
    nom, poids, taille = separe(ligne)
    return {
        "nom": nom,
        "poids": float(poids),
        "taille": float(taille)
    }

def liste_patients_from_nom_fichier(nom_fichier):
    lignes = import_lignes(nom_fichier)
    return [cree_patient(ligne) for ligne in lignes]
    

#calcule sur les donnes 

def imc(patient):
    return round(patient["poids"] / (patient["taille"] ** 2), 2)

def imc_moyen(liste_patients):
    total = sum(imc(patient) for patient in liste_patients)
    return round(total / len(liste_patients), 2)

def liste_noms_patients_en_corpulence_normale(liste_patients):
    return [
        patient["nom"]
        for patient in liste_patients
        if 18.5 <= imc(patient) <= 25
    ]
    
    
#ecrire les resultat dans fichier
def produire_chaine(patient):
    return f"{patient['nom']} {imc(patient)}\n"

def ecrire_imc(liste_patients, nom_fichier):
    with open(nom_fichier, 'w') as f:
        for patient in liste_patients:
            f.write(produire_chaine(patient))
        
        f.write(f"IMC Moyen : {imc_moyen(liste_patients)}\n")
        f.write("Noms des patients en corpulence normale :\n")
        
        for nom in liste_noms_patients_en_corpulence_normale(liste_patients):
            f.write(f"{nom}\n")

def traitement_complet_donnees(nom_fichier_source, nom_fichier_destination):
    patients = liste_patients_from_nom_fichier(nom_fichier_source)
    ecrire_imc(patients, nom_fichier_destination)
