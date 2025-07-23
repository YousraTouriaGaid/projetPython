def coord_centre_cercle (x1, y1, x2, y2):
    #qui revois les coordonnées x, y du centre du cercl
    x = (x1+x2) / 2
    y = (y1+y2) / 2
    return x, y
    
def coord_bas_losange(x1,y1,x2,y2):
    #(le premier sur le sommet gauche, le second sur le sommet supérieur)
    x = x2
    y = y1 -( y2 - y1)
    
    #x_centre = (x1 + x2) / 2
    #y_centre = (y1 + y2) / 2
    #qui renvoie les coordonnées x, y du sommet inférieur du losange.
    
    
    
def coordDEF():
    #et qui demande à l'utilisateur les coordonnées des points A, B, C de 
    xD = input("entre point par l'abscisse xD") 
    yD = input("entre point par l'abscisse yD") 
    xE = input("entre point par l'abscisse XE") 
    yE = input("entre point par l'abscisse yE") 
    xF = input("entre point par l'abscisse xF") 
    yF = input("entre point par l'abscisse yF") 
    
    return coord_centre_cercle ()
    return coord_centre_cercle ()