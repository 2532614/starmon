from arme import Arme
from armure import Armure
from vaisseau import Vaisseau
from planete import Planete
from inventaire import Inventaire
from perso import Perso
from shop import Shop
from images import image
from pp import Pp
import matplotlib.pyplot as plt
import requests
import random
import json
import os

 
#t-rn4_put3+s410p3
 
class Gestion():
    """gère le programe
    """
    def __init__(self) -> None:
        """decole la gestion du programme
        """
        self.shop = Shop()
        self.pp = Pp("pp", "pp", "PP", 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none"))
        self.personnages:list[Perso] = []
        self.inventaire = Inventaire([], [], 0, Vaisseau("Tas de ferailles", "inconnu", 5, 31), [])
        self.primes = []
 
        self.planetes = []
        self.planete = ""
   
    def call_apis(self) -> None:
        """appel des apis
        """
        try:
            self.charger_json()
        except FileNotFoundError:
 
            dragon_request = requests.Session().get("https://swapi.info/api/planets").json()
            for planete in dragon_request:
                if planete["name"] == "Mustafar":
                    mustafar = Planete(planete["name"], planete["orbital_period"], False)
                elif "Coruscant" == planete["name"]:
                    self.planetes.append(Planete(planete["name"], -1, False))
                else:
                    self.planetes.append(Planete(planete["name"], (planete["orbital_period"]), False))
            orb = 1
            for planete in self.planetes:
                if planete.co == "unknown":
                    planete.co = orb
                    orb += 1
                else:
                    planete.co = int(planete.co)
            self.planetes = self.tri_planete(self.planetes)
            

            self.planetes.insert(50, mustafar)
            self.planetes.append(Planete("Death Star", 0, False))
 
            co = 0
            for id_planete in range(61):
                self.planetes[id_planete].co = co
                co += 31
 
            dragon_request = requests.Session().get("https://akabab.github.io/starwars-api/api/all.json").json()
            for perso in dragon_request:
                if "Jabba Desilijic Tiure" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Hutt clan", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("poing")], self.shop.armurerie("none")))
                    self.planetes[20].occupants.append(self.personnages[len(self.personnages) - 1])
                elif "Grievous" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Separatist Droid", perso["species"], 200, [self.shop.armurerie("mini poing"), self.shop.armurerie("sabre laser")], self.shop.armurerie("none")))
                    self.planetes[30].occupants.append(self.personnages[len(self.personnages) - 1])
                elif "Darth Maul" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 200, [self.shop.armurerie("etranglement de force"), self.shop.armurerie("double sabre maul"), self.shop.armurerie("mini poing")], self.shop.armurerie("none")))
                    self.planetes[40].occupants.append(self.personnages[len(self.personnages) - 1])
                elif "Darth Vader" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 400, [self.shop.armurerie("etranglement de force"), self.shop.armurerie("sabre vader"), self.shop.armurerie("poing vader")], self.shop.armurerie("none")))
                    self.planetes[50].occupants.append(self.personnages[len(self.personnages) - 1])
                elif "Palpatine" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 1000, [self.shop.armurerie("poing sidious"), self.shop.armurerie("eclaire(badass)")],  self.shop.armurerie("none")))
                    self.planetes[60].occupants.append(self.personnages[len(self.personnages) - 1])
                elif "Sith" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("sabre laser"), self.shop.armurerie("la force(trop mainsteam)")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "Jedi Order" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Jedi", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("sabre laser"), self.shop.armurerie("la force(trop mainsteam)")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "IG-88" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 29, [self.shop.armurerie("poing"), self.shop.armurerie("Pistolet blaster DL-44")], self.shop.armurerie("none")))
                elif "C-3PO" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("C3-poingO")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "droid" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("zap")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "wookiee" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "Wookie", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("arbalete laser(cool)")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "Green Squadron" in perso["affiliations"] or "Red Squadron" in perso["affiliations"] or "Black Squadron" in perso["affiliations"] or "Gold Squadron" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Colored Squadron", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster DC17")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "New Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "New Republic", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "Resistance" in perso["affiliations"]:
                    arme = ""
                    match (random.randint(0,6)):
                        case 0:
                            arme = "zap"
                        case 1:
                            arme = "Pistolet blaster DL-44"
                        case 2:
                            arme = "blaster(pas cool)"
                        case 3:
                            arme = "blaster DC17"
                        case 4:
                            arme = "DC15 blaster"
                        case 5:
                            arme = "pistolet westar 35(cool)"
                    self.personnages.append(Perso(perso["name"], "Resistance", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie(arme)], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                elif "Galactic Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none")))
                    try:
                        self.habitant(perso["homeworld"])
                    except KeyError:
                        id_planete = random.randint(0, 61)
                        if id_planete == 21 or id_planete == 31 or id_planete == 41 or id_planete == 51 or id_planete == 61:
                            id_planete -= 1
                else:
                    self.personnages.append(Perso(perso["name"], "None", perso["species"], 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none")))
                    try:
                        if isinstance(perso["homeworld"], list):
                            self.habitant("rodia")
                        else:
                            self.habitant(perso["homeworld"])
                    except KeyError:
                        play = True
                        while play:
                            id_planete = random.randint(0, 61)
                            if id_planete == 20 and id_planete == 30 and id_planete == 40 and id_planete == 50 and id_planete == 6:
                                id_planete -= 1
                                play = False
            self.personnages.append(Perso("battle droid B1", "Droid", "Droid", 30, [self.shop.armurerie("poing"), self.shop.armurerie("fusil blaster E-5(pas cool)")], self.shop.armurerie("none")))
            for id_planete in range(61):
                if id_planete != 20 and id_planete != 30 and id_planete != 40 and id_planete != 50 and id_planete != 60:
                    self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages) - 1])
            self.personnages.append(Perso("battle droid B2", "Droid", "Droid", 70, [self.shop.armurerie("poing"), self.shop.armurerie("blaster integre")], self.shop.armurerie("none")))
            for id_planete in range(61):
                if id_planete != 20 and id_planete != 30 and id_planete != 40 and id_planete != 50 and id_planete != 60:
                    self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages) - 1])
            self.personnages.append(Perso("clone", "clone army", "clone", 100, [self.shop.armurerie("poing"), self.shop.armurerie("DC15 blaster"), self.shop.armurerie("blaster DC17")], self.shop.armurerie("none")))
            for id_planete in range(61):
                if id_planete != 20 and id_planete != 30 and id_planete != 40 and id_planete != 50 and id_planete != 60:
                    self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages) - 1])
            self.personnages.append(Perso("Storm trooper", "storm trooper army", "storm trooper", 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none")))
            for id_planete in range(61):
                self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages) - 1])

            vaisseaux = []
            dragon_request = requests.Session().get("https://swapi.info/api/starships").json()
            for vaisseau in dragon_request: 
                if "Death Star" == vaisseau["name"]:
                    pass
                elif "TIE Advanced x1" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 30000, vaisseau["max_atmosphering_speed"]))
                elif "Rebel transport" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 45000, vaisseau["max_atmosphering_speed"]))
                elif "Slave 1" ==vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 100000, vaisseau["max_atmosphering_speed"]))
                elif "Republic Cruiser" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 14000000, vaisseau["max_atmosphering_speed"]))
                elif "Droid control ship" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 7500000, vaisseau["max_atmosphering_speed"]))
                elif "Naboo Royal Starship" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 60000, vaisseau["max_atmosphering_speed"]))
                elif "AA-9 Coruscant freighter" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 50000, vaisseau["max_atmosphering_speed"]))
                elif "H-type Nubian yacht" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 45000, vaisseau["max_atmosphering_speed"]))
                elif "Republic Assault ship" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 7000000, vaisseau["max_atmosphering_speed"]))
                elif "Naboo star skiff" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 55000, vaisseau["max_atmosphering_speed"]))
                elif "Millennium Falcon" == vaisseau["name"]:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], 100000, vaisseau["max_atmosphering_speed"]))
                else:
                    vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], int(int(vaisseau["cost_in_credits"])/10), vaisseau["max_atmosphering_speed"]))
                
            vaisseaux.append(Vaisseau("Tas de ferailles", "inconnu", 0, 0))
            self.shop.vaisseaux = vaisseaux
        
            self.planete = self.planetes[1]


    def tri_planete(self, planetes:list[Planete]) -> list:
        """tri la liste de planete
 
        Args:
            planetes (list[Planete]): la liste de planete non trier
 
        Returns:
            list: la  liste de planete trier
        """
        lst_a_trier = planetes.copy()
       
        if len(lst_a_trier) <= 1:
            return lst_a_trier
       
        pivot = lst_a_trier[len(lst_a_trier) - 1]
 
        petit = []
        grand = []
 
        for num_plan in range(len(lst_a_trier)-1):
            if lst_a_trier[num_plan].co < pivot.co:
                petit.append(lst_a_trier[num_plan])
            else:
                grand.append(lst_a_trier[num_plan])
 
        return self.tri_planete(petit) + [pivot] + self.tri_planete(grand)
           
    def habitant(self, habite:str) -> None:
        """assigne les personnage à leur planetes respective
 
        Args:
            habite (str): la planete en question
        """
        for planete in self.planetes:
            if habite in planete.nom.lower():
                planete.occupants.append(self.personnages[len(self.personnages) - 1])
                return
   
    def charger_json(self) -> None:
        with open("perso.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
 
            for perso in donnees:
                self.personnages.append(Perso(perso["nom"], perso["groupe"], perso["race"], perso["pv"], [], self.shop.armurerie(perso["armure"])))
                for arme in perso["armes"]:
                    self.personnages[len(self.personnages) - 1].armes.append(self.shop.armurerie(arme))
 
        with open("planetes.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
 
            for planete in donnees:
                self.planetes.append(Planete(planete["nom"], planete["co"], planete["detruit"]))
                for habitant in planete["occupants"]:
                    for perso in self.personnages:
                        if habitant == perso.nom:
                            self.planetes[len(self.planetes) - 1].occupants.append(perso)
 
        with open("vaisseaux.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
 
            for vaisseau in donnees:
                self.shop.vaisseaux.append(Vaisseau(vaisseau["nom"], vaisseau["modele"], vaisseau["prix"],vaisseau["vitesse"]))
        
        
        with open("team.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
            pp = 1
            for perso in donnees:
                if pp == 1:
                    pp += 1
                    self.pp = Pp(perso["nom"], perso["groupe"], perso["race"], perso["pv"], [], self.shop.armurerie(perso["armure"]))
                    for arme in perso["armes"]:
                        self.pp.armes.append(self.shop.armurerie(arme))

                else:        
                    self.inventaire.equipage.append(Perso(perso["nom"], perso["groupe"], perso["race"], perso["pv"], [], self.shop.armurerie(perso["armure"])))
                    for arme in perso["armes"]:
                        self.personnages[len(self.personnages) - 1].armes.append(self.shop.armurerie(arme))

        with open("inventaire.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

            self.inventaire.argent = donnees[0]
            self.shop.vaisseau_pp(donnees[1], self.inventaire)
            self.inventaire.nb_carotte = donnees[2]
            self.inventaire.nb_carburant = donnees[3]
            for planete in self.planetes:
                if donnees[4] == planete.nom:
                    self.planete = planete
            self.inventaire.money = donnees[5]
            self.inventaire.mark = donnees[6]
            self.inventaire.black = donnees[7]
            self.inventaire.transactions = donnees[8]
                
    def enregistrer_json(self) -> None:
        lst_dict = []
        for perso in self.personnages:
            lst_dict.append(perso.to_dick_uh_i_mean_dict())
        with open("perso.json", "w", encoding="utf-8") as fichier:
            json.dump(lst_dict, fichier, indent=4)
        lst_dict = []
        for planete in self.planetes:
            lst_dict.append(planete.to_dick_uh_i_mean_dict())
        with open("planetes.json", "w", encoding="utf-8") as fichier:
            json.dump(lst_dict, fichier, indent=4)
        lst_dict = []
        for vaisseau in self.shop.vaisseaux:
            lst_dict.append(vaisseau.to_dick_uh_i_mean_dict())
        with open("vaisseaux.json", "w", encoding="utf-8") as fichier:
            json.dump(lst_dict, fichier, indent=4)
        lst_dict = [self.pp.to_dick_uh_i_mean_dict()]
        for perso in self.inventaire.equipage:
            lst_dict.append(perso.to_dick_uh_i_mean_dict())
        with open("team.json", "w", encoding="utf-8") as fichier:
            json.dump(lst_dict, fichier, indent=4)
        lst_dict = [self.inventaire.argent, self.inventaire.vaisseau.nom, self.inventaire.nb_carotte, self.inventaire.nb_carburant, self.planete.nom, self.inventaire.money, self.inventaire.mark, self.inventaire.black, self.inventaire.transactions]
        with open("inventaire.json", "w", encoding="utf-8") as fichier:
            json.dump(lst_dict, fichier, indent=4)


    def combattre(self) -> bool:
        """permet de faire combattre
        """
        mort = False
        play = True
        enemies = []
        boss = False
        for numero_membre in range(len(self.inventaire.equipage) + 1):
            while play:
                perso = self.planete.occupants[random.randint(0, len(self.planete.occupants)-1)].copy()
                if ("Jabba Desilijic Tiure" in perso.nom or "Grevious" in perso.nom or "Darth Maul" in perso.nom or "Darth Vader" in perso.nom or "Palpatine" in perso.nom) and boss:
                    pass
                elif "Jabba Desilijic Tiure" in perso.nom or "Grevious" in perso.nom or "Darth Maul" in perso.nom or "Darth Vader" in perso.nom or "Palpatine" in perso.nom:
                    boss = True
                    play = False
                else:
                    play = False
            enemies.append(perso)
            play = True
        while play:
            again = True
            while again:
                nb = 0

                print("=" * 100)
                print("VOTRE TOUR")
                print("=" * 100)
                print("")
                print("les enemis sont:")
                for enemie in enemies:
                    print(f"{enemie.nom}")
                    encore = True
                print("")
                print("1. attaquer")
                print("2. attraper")
                print("3. fuir")

                choix = input("que voulez vous faire?: ")
                print("")
                match choix:
                    case "1":

                        for enemie in enemies:
                            print(f"{nb}. {enemie.nom}")
                            nb += 1
                            encore = True
                        while encore == True:
                            try:
                                nb_target = int(input("quel adversaire attaquez vous?: "))
                                print("")
                                enemies[nb_target].subir_degats(self.pp.attaquer())
                                if enemies[nb_target].pv == 0 :
                                    print(f"{enemies[nb_target].nom} est mort")
                                    for prime in self.primes:
                                        if  enemies[nb_target].nom in prime["perso"]:
                                            money = random.randint(5000, 15000)
                                            print("+" * 100)
                                            print(f"prime reçu: {money}")
                                            print("+" * 100)
                                            self.inventaire.spend(-money, False, False)
                                            self.primes.remove(prime)
                                    enemies.pop(nb_target)
                                else:
                                    print(f"{enemies[nb_target].nom} est a {enemies[nb_target].pv} pv")
                                encore = False
                                again = False
    
        
                            except ValueError:
                                print("valeur impossible")
                                print("")
                            except IndexError:
                                print("valeur impossible")
                                print("")

                    case "2":
                        print("vous essayez de recruter un adversaire")
                        for enemie in enemies:
                            print(f"{nb}. {enemie.nom}")
                            nb += 1
                        try:
                            choix = int(input("qui est la cible?: "))
                            if enemies[choix].pv < random.randint(10, 45):
                                if len(self.inventaire.equipage) <= 3:
                                    self.inventaire.equipage.append(enemies[choix].copy())
                                    print(f"vous avez recruté {enemies[choix].nom}, il fait maintenant partie de votre equipe")
                                    enemies.pop(choix)

                                else:
                                    print("votre équipe est pleine (4 aliés max)")
                                
                            else:
                                print("vous avez échoué")
                            encore = False
                            again = False
                            print("")
                        except ValueError:
                            print("valeur impossible")
                            print("")
                        except IndexError:
                            print("valeur impossible")
                            print("")

                    case "3":
                        print("vous prenez la fuite")
                        play = False
                        again = False
                    case _:
                        print("ceci n'est pas une option")

            for aly in self.inventaire.equipage:
                try:
                    nb_target = random.randint(0,len(enemies)-1)
                    print(f"{aly.nom} attaque")
                    print(f"il vise {enemies[nb_target].nom}")
                
                    enemies[nb_target].subir_degats(aly.attaquer())
                    if enemies[nb_target].pv == 0 :
                        print(f"{enemies[nb_target].nom} est mort")
                        for prime in self.primes:
                            if  enemies[nb_target].nom in prime["perso"]:
                                money = random.randint(5000, 15000)
                                print("+" * 100)
                                print(f"prime reçu: {money}")
                                print("+" * 100)
                                self.inventaire.spend(-money, False, False)
                                self.primes.remove(enemies[nb_target])
                        enemies.pop(nb_target)
                    else :
                        print(f"{enemies[nb_target].nom} est a {enemies[nb_target].pv} pv")


                    if aly.nom == "grievious":
                        print("grievious attaque une seconde fois")


                        nb_target = random.randint(0,len(enemies)-1)
                        print(f"il vise {enemies[nb_target].nom}")
                
                        enemies[nb_target].subir_degats(aly.attaquer())
                        if enemies[nb_target].pv == 0 :
                            print(f"{enemies[nb_target].nom} est mort")
                            for prime in self.primes:
                                if  enemies[nb_target].nom in prime["perso"]:
                                    money = random.randint(5000, 15000)
                                    print("+" * 100)
                                    print(f"prime reçu: {money}")
                                    print("+" * 100)
                                    self.inventaire.spend(-money, False, False)
                                    self.primes.remove(enemies[nb_target])
                            enemies.pop(nb_target)
                        else :
                            print(f"{enemies[nb_target].nom} est a {enemies[nb_target].pv} pv")
                    print("")
                except ValueError:
                    pass


            for enemie in enemies:
                if enemie.nom == "Jabba Desilijic Tiure":
                    attaque = random.randint(2)
                    if attaque == 0:
                        print(f"{enemie.nom} attaque")
                    nb_target = random.randint(0,len(self.inventaire.equipage))
                    try:
                        print(f"il vise {self.inventaire.equipage[nb_target].nom}")
                    except IndexError:
                        print("il vise Pépé")
                
                    try:
                        self.inventaire.equipage[nb_target].subir_degats(enemie.attaquer())
                        if self.inventaire.equipage[nb_target].pv == 0 :
                            print(f"{self.inventaire.equipage[nb_target].nom} est mort")
                            self.inventaire.equipage.pop(nb_target)
                        else :
                            print(f"{self.inventaire.equipage[nb_target].nom} est a {self.inventaire.equipage[nb_target].pv} pv")
                    except IndexError:
                        self.pp.subir_degats(enemie.attaquer())
                        if self.pp.pv == 0 :
                            print(f"{self.pp.nom} est mort")
                        else :
                            print(f"{self.pp.nom} est a {self.pp.pv} pv")
                    else:
                        nb_sbire = random.randint(3)+1
                        print(f"Jabba Desilijic Tiure appelle {nb_sbire} sbire")
                        for nb in nb_sbire:
                            enemies.append(perso[22])
                        

                else:
                    print(f"{enemie.nom} attaque")
                    nb_target = random.randint(0,len(self.inventaire.equipage))
                    try:
                        print(f"il vise {self.inventaire.equipage[nb_target].nom}")
                    except IndexError:
                        print("il vise Pépé")
                
                    try:
                        self.inventaire.equipage[nb_target].subir_degats(enemie.attaquer())
                        if self.inventaire.equipage[nb_target].pv == 0 :
                            print(f"{self.inventaire.equipage[nb_target].nom} est mort")
                            self.inventaire.equipage.pop(nb_target)
                        else :
                            print(f"{self.inventaire.equipage[nb_target].nom} est a {self.inventaire.equipage[nb_target].pv} pv")
                    except IndexError:
                        self.pp.subir_degats(enemie.attaquer())
                        if self.pp.pv == 0 :
                            print(f"{self.pp.nom} est mort")
                        else :
                            print(f"{self.pp.nom} est a {self.pp.pv} pv")

                    if enemie.nom == "grievious":
                        print("grievious attaque une seconde fois")
                            
                        nb_target = random.randint(0,len(self.inventaire.equipage) + 1)
                        try:
                            print(f"il vise {self.inventaire.equipage[nb_target].nom}")
                        except IndexError:
                            print("il vise Pépé")
                
                        try:
                            self.inventaire.equipage[nb_target].subir_degats(enemie.attaquer())
                            if self.inventaire.equipage[nb_target].pv == 0 :
                                print(f"{self.inventaire.equipage[nb_target].nom} est mort")
                                self.inventaire.equipage.pop(nb_target)
                            else :
                                print(f"{self.inventaire.equipage[nb_target].nom} est a {self.inventaire.equipage[nb_target].pv} pv")
                        except IndexError:
                            self.pp.subir_degats(enemie.attaquer())
                            if self.pp.pv == 0 :
                                print(f"{self.pp.nom} est mort")
                            else :
                                print(f"{self.pp.nom} est a {self.pp.pv} pv")
            
            
            if self.pp.pv == 0 :
                image("game_over")
                try:
                    os.remove("perso.json")
                    os.remove("planetes.json")
                    os.remove("vaisseaux.json")
                    os.remove("team.json")
                    os.remove("inventaire.json")
                except FileNotFoundError:
                    pass
                return True
            elif len(enemies) == 0:
                print("Victiore")
                print("")
                print("-" * 100)
                print("")
                return False
        return False

 
    def changer_arme(self)->None:
        """permet de changer d'arme
        """
        if len(self.inventaire.armes) > 0:
            print("=" * 100)
            print("changement d'arme")
            print("=" * 100)
            print("")
            nb = 0
            for arme in self.inventaire.armes:
                print(f"{nb}. {arme.nom}: {arme.damage} damage")
                nb += 1
            print("")
            try:
                choix = int(input("quel arme  voulez vous equiper?: "))
                self.inventaire.armes.append(self.pp.armes[1])
                self.pp.armes[1] = self.inventaire.armes.pop(choix)
                print(f"vous avez equiper {self.pp.armes[1]}")
            except ValueError:
                print("choix invalide")
            except IndexError:
                print("choix invalide")

    
    def changer_armure(self)->None:
        """permet de changer d'arme
        """
        if len(self.inventaire.armures) > 0:
            print("=" * 100)
            print("changement d'armure")
            print("=" * 100)
            print("")
            nb = 0
            for armure in self.inventaire.armures:
                print(f"{nb}. {armure.nom}: {armure.pv} point de vie restant")
                nb += 1
            print("")
            try:
                choix = int(input("quel armure  voulez vous equiper?: "))
                if self.pp.armure.pv > 0:
                    self.inventaire.armures.append(self.pp.armure)
                self.pp.armure = self.inventaire.armures.pop(choix)
                print(f"vous avez equiper {self.pp.armure}")
            except ValueError:
                print("choix invalide")
            except IndexError:
                print("choix invalide")
                
 
    def prime(self)-> None:
        """permete de generer une prime
        """
        print("=" * 100)
        print("cantina")
        print("=" * 100)
        play = True
        while play:
            planete1 = self.planetes[random.randint(0, len(self.planetes) - 1)]
            if len(planete1.occupants) != 4:
                play = False
        prime1 = planete1.occupants[random.randint(0, len(planete1.occupants) - 1)]

        play = True
        while play:
            planete2 = self.planetes[random.randint(0, len(self.planetes) - 1)]
            if len(planete2.occupants) != 4:
                play = False
        prime2 = planete2.occupants[random.randint(0, len(planete2.occupants) - 1)]

        play = True
        while play:
            planete3 = self.planetes[random.randint(0, len(self.planetes) - 1)]
            if len(planete3.occupants) != 4:
                play = False
        prime3 = planete3.occupants[random.randint(0, len(planete3.occupants) - 1)]
 
       
        print("")
        print(f"1. {prime1.nom} sur {planete1}")
        print(f"2. {prime2.nom} sur {planete2}")
        print(f"3. {prime3.nom} sur {planete3}")
        choix = input("quel prime accepter vous?: ")
 
        if choix == "1":
            print(f"la prime pour {prime1.nom} a été accepter")
            self.primes.append({"planete" : planete1, "perso" : prime1.nom})
        elif choix == "2":
            print(f"la prime pour {prime2.nom} a été accepter")
            self.primes.append({"planete" : planete2, "perso" : prime2.nom})
        elif choix == "3":
            print(f"la prime pour {prime3.nom} a été accepter")
            self.primes.append({"planete" : planete3, "perso" : prime3.nom})
        else:
            print("aucune prime n'a été accepter")
        


    def voir_prime(self)-> None:
        """permet de voir les primes en cours
        """
        for prime in self.primes:
            print(f"vous avez accepter une prime pour {prime["perso"]} sur la planete {prime["planete"]}")


    def voyager(self)-> None:
        print("-" * 100)
        print("")
        nb = 0
        for planete in self.planetes:
            if planete.detruit == False:
                if self.inventaire.vaisseau.nom == "Tas de ferailles":
                    print("T'a pas de vaisseau")
                    print("")
                    print("-" * 100)
                    print("")
                    return
                else:
                    if planete.co < (self.planete.co + self.inventaire.nb_carburant) and planete.co > (self.planete.co - self.inventaire.nb_carburant):
                        print(f"{nb}. {planete}")
                    nb += 1
        choix = input("ou voulez vous aller?(nom/numero): ")
        for planete in range(len(self.planetes)):
            if (self.planetes[planete].nom == choix or str(planete) == choix) and self.planetes[planete].detruit == False:
                distance = self.planetes[planete].co - self.planete.co
                if distance < 0:
                    distance = -distance
                if distance < self.inventaire.nb_carburant:
                    self.planete = self.planetes[planete]
                    image("vroum_vroum")
            
                    for x in range(len(self.inventaire.equipage) + 1):
                        if self.inventaire.nb_carotte != 0:
                            self.inventaire.nb_carotte -= 1
                            try:
                                self.inventaire.equipage[x].pv = self.inventaire.equipage[x].pv_max
                                print(f"{self.inventaire.equipage[x].nom} est restoré")
                            except IndexError:
                                self.pp.pv = self.pp.pv_max
                                print("vous etes restoré")

                            print("")
                            print("-" * 100)
                            print("")
                            return
                else:
                    print("manque de carburant")
                    print("")
                    print("-" * 100)
                    print("")
                    return
        print("aucune planete ne porte ce nom ou ce numero")
        print("")
        print("-" * 100)
        print("")

    def cheat_code(self)->None:
        
        self.inventaire.spend(-100000000000, False, False)
        self.pp.armes[1] = self.shop.armurerie("eclaire(badass)")#sabre laser ametiste si legite, eclair de force sinon
        self.pp.armure = Armure("plot armor", 200, 70000) #armure mendalorienne
        self.inventaire.equipage = [self.personnages[15], self.personnages[77], self.personnages[42], self.personnages[3]] #jabba, grievious, maul, vader
        self.shop.vaisseau_pp("Star Destroyer", self.inventaire) #c good
        self.inventaire.nb_carburant = 10000000
        self.inventaire.nb_carotte = 10000000
        print("skill issue")

    def menu_principale(self)->None:
        print("")
        print("0. changer d'arme/armure")
        print("1. aller au market")
        print("2. voyager")
        print("3. combattre")
        print("4. obtenir une prime")
        print("5. voir les statz")
        print("6. voir inventaire")
        print("7. voir carte")
        print("8. chercher du travail")
        print("9. sauvegarder et quitter")
        vader = False
        for vador in self.inventaire.equipage:
            if vador.nom == "Darth Vader":
                vader = True
        if self.planete.nom == "Death Star" and vader :
            print("3131. detruire planete")
        print("")

    def detruire_planete(self)->None:
        nb = 0
        for planete in self.planetes:
            if planete.detruit == False:
                print(f"{nb}. {planete}")
                nb += 1
        
        choix = input("entree votre requete monsieur le chancelier?(nom/numero): ")
        detruit = 0

        for planete in range(len(self.planetes)):
            if (self.planetes[planete].nom == choix or str(planete) == choix) and self.planetes[planete].detruit == False:
                self.planetes[planete].detruit = True
                image("boom")
                print(f"la planete {self.planetes[planete].nom} n'existe plus")
                detruit = 31
        if detruit == 0 :
            print("aucune planete detruite")

    def pie_chart(self):
        detruit = 0
        safe = 0
        for planete in self.planetes:
            if planete.detruit:
                detruit += 1
            else:
                safe += 1
        donnees = [safe, detruit]
        boom = ['planetes en vie', 'planetes détruites']
        colors = [(0, .5, 1), (0.5, 0, 0)]

        plt.pie(donnees, labels=boom, colors=colors, autopct = "%1.2f%%", startangle=90,)

        # Display the plot
        plt.show()
        
    def line_chart(self) -> None:
        """fait un graph avec les dépenses et l'argent
        """
        plt.cla()
        plt.plot(self.inventaire.transactions, self.inventaire.mark, label="market", color=(0, 1, 1), linestyle="-")
        plt.plot(self.inventaire.transactions, self.inventaire.black, label="black market", color=(0.4, 0, 0.6), linestyle="-")
        plt.plot(self.inventaire.transactions, self.inventaire.money, label="argent", color=(1, 1, 0), linestyle="-")

        plt.xlabel("transaction")
        plt.ylabel("argent")
        plt.title("argent posséder et total au fil des transactions")
        plt.legend()
        plt.show()

    def statz(self) -> None:
        insultes = 0
        print("")
        print("-" * 100)
        for insulte in self.inventaire.nico.to_dick_uh_i_mean_dict:
            insultes += 1
        print(f"nos insultes envers nico au cours du projet: {insultes}")
        print("-" * 100)

        print("")

        vaisseau_rapide = self.tri_vaisseaux(self.shop.vaisseaux)
        print("-" * 100)
        print("les 10 vaisseaux les plus rapide:")
        for rapide in range(10):
            print(f"{rapide + 1}. {vaisseau_rapide[rapide].nom}, vitesse: {vaisseau_rapide[rapide].vitesse}")
        print("-" * 100)
        print("")
        print("-" * 100)
        print("définir le nombre de presonnes par groupe:")
        print("0. None")
        print("1. Sith")
        print("2. Jedi")
        print("3. Droid")
        print("4. Wookie")
        print("5. Colored Squadron")
        print("6. New Republic")
        print("7. Resistance")
        print("8. Galactic Republic")
        print("9. Hutt clan")
        choix = input("choisissez un goupe: ")
        print("")
        nb = 0
        match choix:
            case "0":
                for perso in self.personnages:
                    if "None" in perso.groupe:
                        nb += 1
            case "1":
                for perso in self.personnages:
                    if "Sith" in perso.groupe:
                        nb += 1
            case "2":
                for perso in self.personnages:
                    if "Jedi" in perso.groupe:
                        nb += 1
            case "3":
                for perso in self.personnages:
                    if "Droid" in perso.groupe:
                        nb += 1
            case "4":
                for perso in self.personnages:
                    if "Wookie" in perso.groupe:
                        nb += 1
            case "5":
                for perso in self.personnages:
                    if "Colored Squadron" in perso.groupe:
                        nb += 1
            case "6":
                for perso in self.personnages:
                    if "New Republic" in perso.groupe:
                        nb += 1
            case "7":
                for perso in self.personnages:
                    if "Resistance" in perso.groupe:
                        nb += 1
            case "8":
                for perso in self.personnages:
                    if "Galactic Republic" in perso.groupe:
                        nb += 1
            case "9":
                for perso in self.personnages:
                    if "Hutt clan" in perso.groupe:
                        nb += 1
        print(f"il y a {nb} pesonnes dans ce groupe")
        print("-" * 100)
        print("")
        print("-" * 100)
        nb = 0
        for planete in self.planetes:
            nb += len(planete.occupants)

        print(f"la moyenne de personnes par planète est de {(nb / 61):.2f} personnes")

        print("-" * 100)
        print("")


    def tri_vaisseaux(self, lst_vaisseaux) -> list:
        """tri la liste de vaisseau selon la vitesse
 
        Args:
            planetes (list[Planete]): la liste de planete non trier
 
        Returns:
            list: la  liste de vaisseaux trier
        """
        lst_a_trier:list[Planete] = lst_vaisseaux.copy()
       
        if len(lst_a_trier) <= 1:
            return lst_a_trier
       
        pivot = lst_a_trier[len(lst_a_trier) - 1]
 
        petit = []
        grand = []
 
        for num_vaisseau in range(len(lst_a_trier)-1):
            if lst_a_trier[num_vaisseau].vitesse < pivot.vitesse:
                petit.append(lst_a_trier[num_vaisseau])
            else:
                grand.append(lst_a_trier[num_vaisseau])
 
        return self.tri_vaisseaux(grand) + [pivot] + self.tri_vaisseaux(petit)
            
    def recherche_dicoto(self, coordonnées: int) -> str:
        planetes = sorted(self.planetes, key=lambda p: p.co)

        gauche = 0
        droite = len(planetes) - 1

        while gauche <= droite:
            milieu = (gauche + droite) // 2
            planete = planetes[milieu]

            if (planete.co - 15) <= coordonnées <= (planete.co + 15):
                return f"le nom de la planete est {planete.nom}"

            elif planete.co > coordonnées:
                droite = milieu - 1
            else:
                gauche = milieu + 1

        return "aucune planete ne correspond"
            
    def recherche_nom(self, nom:str) -> str:
        for planete in self.planetes:
            if planete.nom == nom:
                return f"la coordonné de {nom} est {planete.co}"
        return "aucune planete ne correspont"

