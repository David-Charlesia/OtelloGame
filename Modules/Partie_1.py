# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:12:37 2019

@author: tidad
"""

def indice_valide (plateau,nb):
    #Retourne True si indice est un indice valide de case pour le plateau (entre 0 et n-1)
    if nb>=0 and nb<=plateau['n']-1 :
        return True
    else :
        return False


def case_valide (plateau,i,j):
    #Retourne True si (i,j) est une case du plateau (i et j sont des indices valides)
    #i=i-1 #parce qu'on commence à 0
    #j=j-1 #parce qu'on commence à 0

    if indice_valide(plateau,i)==True:
        if indice_valide(plateau,j)==True:
            return True
    return False



def get_case(plateau,i,j):
    #Retourne la valeur de la case (i,j). Erreur si (i,j) n'est pas valide.
    if case_valide(plateau,i,j)==False:
        return False
    #i=i-1 #parce qu'on commence à 0
    #j=j-1 #parce qu'on commence à 0
    tab=plateau['cases']
    n=plateau['n']#taille du plateau
    x=(i*n)+j #pour déterminer quel indice : i=ligne j=colone
    return tab[x]


def set_case(plateau,i,j,val):
    #Affecte la valeur val dans la case (i,j). Erreur si (i,j) n'est pas une case ou si val n'est pas entre 0 et 2.
    #Met aussi à jour le nombre de cases libres (sans pion).
    assert val==0 or val==1 or val==2, "Valeurs non-valides"
    case=get_case(plateau,i,j)
    #i=i-1 #parce qu'on commence à 0
    #j=j-1 #parce qu'on commence à 0
    n=plateau['n']#taille du plateau
    x=(i*n)+j #pour déterminer quel indice : i=ligne j=colone
    #assert case==0
    plateau['cases'][x]=val


def creer_plateau(n):
    #Retourne une nouvelle partie. Lève une erreur si n est différent de 4, 6 ou 8.
    #Une partie est un dictionnaire contenant :
    #- n : valeur passée en paramètre
    #- cases : tableau de n*n cases initialisées
    assert n==4 or n==6 or n==8
    cases=[]
    for i in range (n**2):    # <=> cases = [0] * n * n
        cases.append(0)
    cases[int((n/2-1)*n+(n/2-1))]=2
    cases[int((n/2-1)*n+(n/2))]=1
    cases[int((n/2)*n+(n/2-1))]=1
    cases[int((n/2)*n+(n/2))]=2
    return cases

"""
Affiche le plateau à l'écran.
La fonction est divisee en 5 parties comme suit:
  o Step 1: bla
  o Step 2: bla bla
"""
def afficher_plateau(plateau):
    #
    from Modules.termcolor import colored
    cases=plateau['cases']
    n=plateau['n']
    backcolor='on_blue'
    lettres=['   a   ','   b   ','   c   ','   d   ','   e   ','   f   ','   g   ','   h   ']
    esp='       '*(n+2) #le +2 c'est pour les 2 colone des extremités
    premiere_ligne='       '

    # Step 2
    i=0
    x=0 #compteur pour pointer la case dans le tableau parce que le j se réinitialise
    print(colored(esp,color=None,on_color='on_grey'))#l'espace en haut en noir
    for z in range(1,n+1): #pour les chiffres en haut
        premiere_ligne=premiere_ligne+'   '+str(z)+'   '
    print(colored((premiere_ligne+'       '),color='white',on_color='on_grey')) #ligne des chiffres
    print(colored(esp,color=None,on_color='on_grey'))#ligne noir

    # Step 4
    while i<n :
        ch=''
        linter=''
        ch=ch+colored(lettres[i],color='white',on_color='on_grey') #changé couleur
        j=0
        linter=linter+colored('       ',color=None,on_color='on_grey')

        while j<n :
            if backcolor=='on_blue': #pour alterner les couleurs des cases
                backcolor='on_magenta'
            else :
                backcolor='on_blue'


            if cases[x]==0 :    #case vide
                ch=ch+colored('       ',color=None,on_color=backcolor)
            elif cases[x]==1:   #pion noir
                ch=ch+colored('  ###  ',color='grey', on_color=backcolor)
            else :              #pion blanc
                ch=ch+colored('  ###  ',color='white', on_color=backcolor)

            #ligne qui pour faire de l'espace entre les cases
            linter=linter+colored('       ',color=None, on_color=backcolor)
            x=x+1
            j=j+1

        i=i+1

        ch=ch+colored('       ',color=None,on_color='on_grey')
        linter=linter+colored('       ',color=None,on_color='on_grey')

        print(linter)
        print(ch)
        print(linter)


        if backcolor=='on_blue': #pour alterner les couleurs des cases
            backcolor='on_magenta'
        else :
            backcolor='on_blue'


    for y in range (3): #espace noir en bas du plateau
        print(colored(esp,color=None,on_color='on_grey'))

###############################################################################

if __name__ == '__main__':
    print('Exemple de plateau de jeu de taille 6 en début de partie : ')
    n=6
    plateau={}
    plateau['n']=n
    plateau['cases']=creer_plateau(n)
    afficher_plateau(plateau)
