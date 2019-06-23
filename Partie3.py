from Modules.Partie_1 import *
from NewPartie2 import *
from os import system
from json import *

def creer_partie(n):
    partie={}
    partie['joueur']=1
    
    plateau={}
    plateau['n']=n
    plateau['cases']=creer_plateau(n)
    
    partie['plateau']=plateau
    
    return partie

def saisie_valide(partie, s):
    n=partie['plateau']['n']
    
    if s=='M':
        return True
    if int(ord(s[0]))>96 and int(ord(s[0]))<97+n:
        if int(s[1])>0 and int(s[1])<=n:
            return True
    return False

def tour_jeu(partie):
    #system('clear') #pour linux
    system('cls') #pour Windows
    
    plateau=partie['plateau']
    joueur=partie['joueur']
    afficher_plateau(plateau)
    if joueur_peut_jouer(plateau,joueur):
        print("C'est au tour du joueur ",joueur)
        s=input('Donnez la case sur laquelle vous voulez joué ou taper M pour accéeder au menu: ')
        a=False
        while not(a):
            if not(saisie_valide(partie,s)):
                print("Saisie incorrect")
                s=input('Donnez la case sur laquelle vous voulez joué ou taper M pour accéeder au menu : ')
                
            elif s!="M" and not(mouvement_valide(partie["plateau"], int(ord(s[0]))-97, int(s[1])-1, partie["joueur"])):
                print("Mouvement impossible")
                s=input('Donnez la case sur laquelle vous voulez joué ou taper M pour accéeder au menu : ')
            else:
                a=True
        
        if s != "M":
            #Si c'est un mouvement, il est effectué.
            mouvement(partie["plateau"], ord(s[0])-97, int(s[1])-1, partie["joueur"])
            return True
        #Si c'est un retour au menu, renvoie False.
        return False
'''
def saisir_action(partie):
    print(70*"*"+"\n")
    print("Choisissez une action:\n")
    print("0 pour terminer le jeu")
    print("1 pour commencer une nouvelle partie")
    print("2 pour charger une partie")
    print("3 pour sauvegarder une partie (si une partie est en cours)")
    print("4 pour reprendre la partie (si une partie est en cours)")
    print("\n"+70*"*")
    #Le joueur saisi une action.
    s = input()
    if partie == None:
        while s != "0" and s != "1" and s != "2":
            if s == "3" or s == "4":
                print("Vous n'avez aucune partie en cours, veuillez choisir une autre action:")
            else:
                print("Saisie invalide, réesayez:")
            s = input()
    else:
        while s != "0" and s != "1" and s != "2" and s != "3" and s != "4":
            print("Saisie invalide, réesayez:")
            s = input()
    return s
'''
def saisir_action(partie):
    print("- 0 pour terminer le jeu,")
    print("- 1 pour commencer une nouvelle partie,")
    print("- 2 pour charger une partie,")
    print("- 3 pour sauvegarder une partie (si une partie est en cours),")
    print("- 4 pour reprendre la partie (si une partie est en cours).")
    
    if partie == None:
        choix=int(input("Votre choix : "))
        while choix!=0 and choix!=1 and choix!=2:
            if choix == "3" or choix == "4":
                choix=input("Vous n'avez aucune partie en cours, veuillez choisir une autre action:")
            else:
                choix=input("Saisie invalide, réesayez: ")

    else:
        choix=int(input("Votre choix : "))
        while choix!=0 and choix!=1 and choix!=2 and choix!=3 and choix!=4:
            print(choix," n'est pas un choix valide")
            choix=int(input("Votre choix : "))
    
    return choix



def jouer(partie):
    #Tant que la partie n'est pas terminée.
    while not fin_de_partie(partie["plateau"]):
        #Les joueurs jouent chacun leur tour.
        if tour_jeu(partie):
            partie["joueur"] = pion_adverse(partie["joueur"])
        else:
            #Renvoie False si un joueur souhaite retourner au menu.
            return False
    #system('clear')   #LINUX
    system('cls')      #WINDOWS
    winner = gagnant(partie["plateau"])
    afficher_plateau(partie["plateau"])
    print("")
    print(70*"*"+"\n")
    print("La partie est terminée !\n")
    if winner == 0:
        print("Il y a ex æquo.")
    else:
        print("Le joueur "+str(winner)+" à gagné.")
    print("\n"+70*"*")
    #Return True lorsque la partie est terminée.
    return True


'''
def jouer(partie) :
    while not(fin_de_partie(partie['plateau'])):
        if tour_jeu(partie):
            partie['joueur']=pion_adverse(partie['joueur'])
            
        else:#le joueur decide de go au menu
            return False
    system('clear') #pour linux
    #system('cls') #pour Windows
    print(70*"*"+"\n")
    print('La partie est terminé !')
    plateau=partie['plateau']
    gag=gagnant(plateau)
    afficher_plateau(partie["plateau"])
    if gag == 0 :
        print('Quel match tendu ! On fini sur un exequo !')
    else :
        print('Le joueur '+str(gag)+' a gagné le match au la main ! Féliciation !' )
    print(70*"*"+"\n")
'''
def saisir_taille_plateau():
    n=int(input("Donnez la taille du plateau (4, 6 ou 8) : "))
    while n!=4 and n!=6 and n!=8:
        print(n," n'est pas une valeur valide")
        n=int(input("Donnez la taille du plateau (4, 6 ou 8) : "))
    return n

def sauvegarder_partie(partie):
       
    with open("sauvegarde_partie.json","w") as outfile:  
        dump(partie, outfile)
        
def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        print("Le fichier sauvegarde_partie.json existe.")
        with open('sauvegarde_partie.json') as partie:  
            return load(partie)
    else:
        print("Le fichier sauvegarde_partie.json n'existe pas.") 
        return creer_partie(4)
    
def otello():
    partie=None
    action=saisir_action(partie)
    while action !=0:
        
        if action == 1:
            partie=creer_partie(saisir_taille_plateau())
            jouer(partie)
        
        elif action == 2:
            partie=charger_partie()
            jouer(partie)
        
        elif action == 3 :
            sauvegarder_partie(partie)
        
        elif action == 4:
            jouer(partie)
        action=saisir_action(partie)
    #system('clear')   #LINUX
    system('cls')      #WINDOWS

otello()