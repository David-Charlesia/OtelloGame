# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:04:31 2019

@author: tidad
"""

from Modules.Partie_1 import *

def pion_adverse (joueur):
    assert joueur==1 or joueur==2
    if joueur==1:
        return 2
    else:
        return 1




def prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):
    from Modules.Partie_1 import get_case
    
    i=i+vertical
    j=j+horizontal
    pion_adv=pion_adverse(joueur)
    if not(case_valide(plateau,i,j)) or get_case(plateau,i,j)!=pion_adv:
        return False
    
    while case_valide(plateau,i,j) :
        if get_case(plateau,i,j)==joueur:
            return True
        elif get_case(plateau,i,j)==0:
            return False
        
        i=i+vertical
        j=j+horizontal
        
    return False

def mouvement_valide(plateau,i,j,joueur):
    
    if get_case(plateau, i,j)!=0:
        return False
    #Retourne True si le joueur peut poser un pion à la case (i,j), False sinon.
    if prise_possible_direction (plateau,i,j,-1,-1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,0,-1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,-1,1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,1,0,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,1,1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,0,1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,1,-1,joueur):
        return True
    elif prise_possible_direction (plateau,i,j,-1,0,joueur):
        return True
    
	#on doit verirfier si la case du plateau au coordonnée i et j est libre
    
    else:
        return False


'''def mouvement_valide(plateau,i,j,joueur):
    from Modules.Partie_1 import get_case
    tab=[-1,1,0]
    x=0
    
    while x<3:
        vertical=tab[x]
        y=0
        while y<3:
            horizontal=tab[y]
            if tab[x]==0 and tab[y]==0:
                return False

            if prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):
                return True
            y=y+1
        x=x+1
    return False'''


def mouvement_direction(plateau,i,j,vertical,horizontal,joueur):
    if prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):
        i=i+vertical
        j=j+horizontal
        while get_case(plateau,i,j)== pion_adverse(joueur):
            set_case(plateau,i,j,joueur)
            i=i+vertical


'''def mouvement (plateau,i,j,joueur):
    tab=[-1,0,1]
    x=0
    while x>8:
        vertical=tab[x]
        x=x+1
        y=0
        while y>8:
            horizontal=tab[y]
            y=y+1
            mouvement_direction(plateau,i,j,vertical,horizontal,joueur)'''
            
def mouvement(plateau,i,j,joueur):
    if mouvement_valide(plateau,i,j,joueur):
    
         #on modifie la case du plateau ou le joueur a posé son pion
         mouvement_direction(plateau,i,j,-1,-1,joueur) 
         mouvement_direction(plateau,i,j,0,-1,joueur)
         mouvement_direction(plateau,i,j,-1,1,joueur) 
         mouvement_direction(plateau,i,j,1,0,joueur) 
         mouvement_direction(plateau,i,j,1,1,joueur) 
         mouvement_direction(plateau,i,j,0,1,joueur) 
         mouvement_direction(plateau,i,j,1,-1,joueur) 
         mouvement_direction(plateau,i,j,-1,0,joueur)
         
         set_case(plateau,i,j,joueur)
        

def joueur_peut_jouer (plateau,joueur):
    n=plateau['n']
    i=0
    j=0
    while i<n:
        j=0
        while j<n:
            if mouvement_valide(plateau,i,j,joueur):
                    return True
            j=j+1
        i=i+1
    return False

def fin_de_partie(plateau):
    if joueur_peut_jouer (plateau,1)==False and joueur_peut_jouer (plateau,2)==False:
        return True
    return False



def gagnant (plateau):
    tableau=plateau['cases']
    i=0
    compteur1=0
    compteur2=0
    while i <len(tableau):
        if tableau[i]==1:
            compteur1=compteur1+1
        elif tableau[i]==2:
            compteur2=compteur2+1
        i=i+1

    if compteur1>compteur2 :
        return '1'

    elif compteur2>compteur1:
        return '2'

    elif compteur1==compteur2:
        return '0'
