from arme import Arme
from armure import Armure
from gestion import Gestion
from inventaire import Inventaire
from perso import Perso
from planete import Planete
from shop import Shop
from vaisseau import Vaisseau
from images import image
import os

mort = False

gestion = Gestion()

gestion.call_apis()

print("************************")
print("bienvenu dans Starmon")
print("************************")

while mort == False:
    gestion.menu_principale()
    choix = input("que voulez vous faire?: ")
    print("")
    match choix:
        case "0":
            match input("changer (1)d'arme ou (2) d'armure: "):
                case "1":
                    print("")
                    gestion.changer_arme()
                case "2":
                    print("")
                    gestion.changer_armure()
                case _:
                    print("")
                    print("choix invalide")
                    print("")
        case "1":
            gestion.shop.acheter(gestion.inventaire)
        case "2":

            gestion.voyager()
        case "3":
            mort = gestion.combattre()
        case "4":
            gestion.prime()
        case "5":
            choix = input("(1)statz ou (2)graph?: ")
            if choix == "statz" or choix == "1":
                gestion.statz()

            elif choix == "graph" or  choix == "2":
                choix = input("voulez vous voir le nombre de planete detruite(1) ou la variation de l'argent(2)?: ")
                if choix == "1":
                    gestion.pie_chart()
                elif choix == "2":
                    gestion.line_chart()
                else:
                    print("rien ne se passe, nico t'es nul")
            else:
                print("nico Tes tellement nul, on va drop ton adresse")


        case "6" :
            gestion.inventaire.voir_inventaire()
        case "7" :
            print("----------------------------------------------------------------------------------------------------")
            choix = input("voulez vous chercher une planete (1) par le nom ou (2) par sa coordonné: ")
            print("")
            match choix:
                case "1":
                    nom = input("quel est le nom de la planete: ")
                    print(gestion.recherche_nom(nom))
                case "2":
                    try:
                        co = int(input("quel est la coordonée de la planette: "))
                        print(gestion.recherche_dicoto(co))
                    except ValueError:
                        print("valeur impossible")
                case _:
                    print("choix invalide")
            print("----------------------------------------------------------------------------------------------------")
            
        case "8":
            gestion.voir_prime()

        case "9":
            gestion.inventaire.spend(-200, False, False)
            print("vous recevez 200 credit")

        case "10" :
            gestion.enregistrer_json()
            mort = True

        case "3131":
            if gestion.planete.nom != "Death Star":
                print("piratage de la station :Death Star: à distance en cours")
            gestion.detruire_planete()
        case "t-rn4_put3+s410p3":
            gestion.cheat_code()

        case _:
            print("nico Tes tellement nul, on va drop ton adresse")
            print("3929 Rue de Lyon")
    
    detruit = 0
    for planete in gestion.planetes:
        if planete.detruit:
            dertuit += 1

    if detruit == 61:
        mort = True
        image("win")
        try:
            os.remove("perso.json")
            os.remove("planetes.json")
            os.remove("vaisseaux.json")
            os.remove("team.json")
            os.remove("inventaire.json")
        except FileNotFoundError:
            pass



