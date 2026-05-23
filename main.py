from arme import Arme
from armure import Armure
from gestion import Gestion
from inventaire import Inventaire
from perso import Perso
from planete import Planete
from shop import Shop
from vaisseau import Vaisseau

mort = False

gestion = Gestion()

gestion.call_apis()

while mort == False:
    gestion.menu_principale()
    choix = input("que voulez vous faire?: ")
    match choix:
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
                    nom = input("quel est le nom de la planette: ")
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
            
        case "8" :
            gestion.enregistrer_json()
            break
        case "9":
            gestion.inventaire.argent += 200
            print("vous recevez 200 credit")
        case "3131":
            if gestion.planete.nom != "Death Star":
                print("piratage de la station :Death Star: à distance en cours")
            gestion.detruire_planete()
        case "t-rn4_put3+s410p3":
            gestion.cheat_code()

        case _:
            print("nico Tes tellement nul, on va drop ton adresse")
            print("3929 Rue de Lyon")



