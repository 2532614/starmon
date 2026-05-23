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
             pass
        case "6" :
            gestion.inventaire.voir_inventaire()
        case "7" :
            pass
        case "8" :
            gestion.enregistrer_json()
            break
        case "3131":
            if gestion.planete.nom != "Death Star":
                print("piratage de la station :Death Star: à distance en cours")
            gestion.detruire_planete()
        case "t-rn4_put3+s410p3":
            gestion.cheat_code()


