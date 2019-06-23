from Modules.Partie_1 import *
from NewPartie2 import *

#n=int(input("donne ton n : "))
n=6
plateau={}
plateau['n']=n
plateau['cases']=creer_plateau(n)


afficher_plateau(plateau)



###############################################################################


print('Test de la fonction indice_valide :')
print(indice_valide(plateau, 1),"doit retourner True")
print(indice_valide(plateau, 7),"doit retourner False")
print('')
print('Test de la fonction case_valide :')
print(case_valide (plateau,4,5),"doit retourner True")
print(case_valide (plateau,7,1),"doit retourner False")
print('')
print('Test de la fonction get_case :')
print(get_case(plateau,2,2),"doit retourner 2")
print(get_case(plateau,3,2),"doit retourner 1")
print(get_case(plateau,1,1),"doit retourner 0")
print('')
print("Test de la fonction set_case :")
set_case(plateau,1,2,1)
set_case(plateau,3,1,2)
print("La fonction doit afficher un pion noir dans la case b3 et un pion blanc dans d2")
afficher_plateau(plateau)




n=4
plateau={}
plateau['n']=n
plateau['cases']=creer_plateau(n)

afficher_plateau(plateau)

print(case_valide(plateau,1,3))

print("True doit retourner ",prise_possible_direction(plateau,1,3,0,-1,2))
print("False doit retourner ",prise_possible_direction(plateau,1,3,0,-1,1))
print("False doit retourner ",prise_possible_direction(plateau,1,3,-1,-1,2))
print("True doit retourner ",prise_possible_direction(plateau,1,0,0,1,1))


print("True doit retourner ",mouvement_valide(plateau,1,3,2))
print("False doit retourner ",mouvement_valide(plateau,0,0,2))

mouvement_direction(plateau,0,3,-1,1,2) # ne modifie rien
afficher_plateau(plateau)
mouvement_direction(plateau,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
afficher_plateau(plateau)

print('***********************************************************')
n=4
plateau={}
plateau['n']=n
plateau['cases']=creer_plateau(n)


print('Test de la fonction mouvement')
afficher_plateau(plateau)

mouvement(plateau,0,3,2) # ne modifie rien
afficher_plateau(plateau)
mouvement(plateau,1,3,2) # met la valeur 2 dans les cases (1,2) et (1,3)
afficher_plateau(plateau)


print('***********************************************************')
n=4
plateau={}
plateau['n']=n
plateau['cases']=creer_plateau(n)
set_case(plateau,1,1,1)
set_case(plateau,2,2,1)
afficher_plateau(plateau)
print(joueur_peut_jouer(plateau,1),'doit retourner False') # retourne False

print('***********************************************************')

n=4
plateau={}
plateau['n']=n
plateau['cases']=creer_plateau(n)
afficher_plateau(plateau)
print(fin_de_partie(plateau),'doit retourner False') # retourne False
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(plateau,1,1,1)
set_case(plateau,2,2,1)
afficher_plateau(plateau)
print(fin_de_partie(plateau),'doit retourner True') # retourne True

print(gagnant(plateau),'doit retourner 1') # retourne 1