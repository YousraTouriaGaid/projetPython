def lundi(mot):
    return f"{mot} {mot}"

def mardi(mot):
    if len(mot) % 2 == 0:
        return mot * 6
    else:
        return mot * 3

def mercredi(mot):
    return mot if len(mot) % 2 == 0 else "impair"

def jeudi(mot):
    repeat = len(mot) % 3
    return mot * repeat

def vendredi(mot):
    return mot

def transforme(mot, num_jour):
    if num_jour == 1:
        return lundi(mot)
    elif num_jour == 2:
        return mardi(mot)
    elif num_jour == 3:
        return mercredi(mot)
    elif num_jour == 4:
        return jeudi(mot)
    elif num_jour == 5:
        return vendredi(mot)
    else:
        return ""  
