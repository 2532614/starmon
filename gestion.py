from arme import Arme
from armure import Armure
from vaisseau import Vaisseau
from planete import Planete
from inventaire import Inventaire
from perso import Perso
from shop import Shop
import requests
import random
import json

"t-rn4_put3+s410p3"

class Gestion():
    """gère le programe
    """
    def __init__(self) -> None:
        """decole la gestion du programme
        """
        self.pp = Perso("pp", "pp", "PP", 100, [self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")], self.shop.armurerie("none"))
        self.personnages:list[Perso] = []
        self.inventaire = Inventaire([], [], 0, "", [])
        self.shop = Shop()
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
                else:
                    self.planetes.append(Planete(planete["name"], planete["orbital_period"], False))
            self.planetes = self.tri_planete(self.planetes)
            if "coruscant" == planete["name"]:
                 Planete(planete["name"], -1)
            
            planete = mustafar
            for position in range(8):
                self.planetes[50+position], planete = planete, self.planetes[50+position]
            self.planetes.append(planete)
            self.planetes.append(Planete("Death Star", 0, False))

            co = 0
            for id_planete in (61):
                self.planetes[id_planete].co = co
                co += 31

            dragon_request = requests.Session().get("https://akabab.github.io/starwars-api/api/all.json").json()
            for perso in dragon_request:
                if "Jabba Desilijic Tiure" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Hutt clan", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("poing")), self.shop.armurerie("none")))
                    self.planetes[21].occupants.append(self.personnages[len(self.personnages)])
                elif "Darth Vader" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 400, (self.shop.armurerie("etranglement de force"), self.shop.armurerie("sabre vader"), self.shop.armurerie("poing vader")), self.shop.armurerie("none")))
                    self.planetes[51].occupants.append(self.personnages[len(self.personnages)])
                elif "Darth Maul" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 200, (self.shop.armurerie("etranglement de force"), self.shop.armurerie("double sabre maul"), self.shop.armurerie("mini poing")), self.shop.armurerie("none")))
                    self.planetes[41].occupants.append(self.personnages[len(self.personnages)])
                elif "Palpatine" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 1000, (self.shop.armurerie("poing sidious"), self.shop.armurerie("eclaire(badass)")),  self.shop.armurerie("none")))
                    self.planetes[61].occupants.append(self.personnages[len(self.personnages)])
                elif "Grievous" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Separatist Droid", perso["species"], 200, (self.shop.armurerie("mini poing"), self.shop.armurerie("sabre")), self.shop.armurerie("none")))
                    self.planetes[31].occupants.append(self.personnages[len(self.personnages)])
                elif "Sith" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("sabre_laser"), self.shop.armurerie("la force(trop mainsteam)")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "Jedi Order" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Jedi", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("sabre_laser"), self.shop.armurerie("la force(trop mainsteam)")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "IG-88" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 29, (self.shop.armurerie("poing"), self.shop.armurerie("Pistolet blaster DL-44")), self.shop.armurerie("none")))
                elif "C-3PO" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("C3-poingO")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "droid" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("zap")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "wookiee" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "wookie", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("arbalete laser(cool)")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "Squadron" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "colored Squadron", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster DC17")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "New Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "New Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "Resistance" in perso["affiliations"]:
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
                    self.personnages.append(Perso(perso["name"], "Resistance", perso["species"], 100, (self.shop.armurerie("poing"), self.shop(arme)), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                elif "Galactic Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
                    self.habitant(perso["homeworld"])
                self.personnages.append(Perso("battle droid B1", "Droid", "Droid", 30, (self.shop.armurerie("poing"), self.shop.armurerie("fusil blaster E-5(pas cool)")), self.shop.armurerie("none")))
                for id_planete in range(61):
                    if id_planete != 21 or id_planete != 31 or id_planete != 41 or id_planete != 51 or id_planete != 61:
                        self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages)])
                self.personnages.append(Perso("battle droid B2", "Droid", "Droid", 70, (self.shop.armurerie("poing"), self.shop.armurerie("blaster integre")), self.shop.armurerie("none")))
                for id_planete in range(61):
                    if id_planete != 21 or id_planete != 31 or id_planete != 41 or id_planete != 51 or id_planete != 61:
                        self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages)])
                self.personnages.append(Perso("clone", "clone army", "clone", 100, (self.shop.armurerie("poing"), self.shop.armurerie("DC15 blaster"), self.shop.armurerie("blaster DC17", "blaster(pas cool)")), self.shop.armurerie("none")))
                for id_planete in range(61):
                    if id_planete != 21 or id_planete != 31 or id_planete != 41 or id_planete != 51 or id_planete != 61:
                        self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages)])


        dragon_request = requests.Session().get("swapi.info/api/starships").json()
        for vaisseau in dragon_request:
            vaisseaux = []
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
                vaisseaux.append(Vaisseau(vaisseau["name"], vaisseau["model"], int(vaisseau["cost_in_credits"]/10), vaisseau["max_atmosphering_speed"]))
            self.shop.vaisseaux = vaisseaux

    def tri_planete(self, planetes:list[Planete]) -> list:
        """tri la liste de planete

        Args:
            planetes (list[Planete]): la liste de planete non trier

        Returns:
            list: la  liste de planete trier
        """
        lst_a_trier:list[Planete] = planetes.copy
        
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
            if habite in planete.nom:
                planete.occupants.append(self.personnages[len(self.personnages)])
    
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
                self.planetes.append(Planete(planete["name"], planete["orbital_period"], planete["detruit"]))
                for habitant in self.planete["occupants"]:
                    for perso in self.personnages:
                        if habitant == perso.nom:
                            self.planetes[len(self.planetes) - 1].append(perso)





    def combattre(self) -> None:
            play = True
            enemies = []
            for numero_membre in len(self.inventaire.equipage):
                enemies.append(self.planete.occupants[random.randint(0, len(self.planete.occupants))])
            
            while play:
                nb = 0
                print("="*8)
                print("VOTRE TOUR")
                print("="*8)
                print("")
                for enemie in enemies:
                    print(f"{nb}. {enemie.nom}")
                    nb += 1
                    encore = True
                    while encore == True:
                        try:
                            choix = int(input("quel adversaire attaquez vous?: "))
                            enemies[choix].subir_degats(self.pp.attaquer())
                            if enemies[nb_target].pv == 0 :
                                print(f"{enemies[nb_target].nom} est mort")
                                enemies[nb_target].pop
                            encore = False


                        except ValueError:
                            print("valeur impossible")


            
                for aly in self.inventaire.equipage:
                    print(f"{aly.nom} attaque")
                    nb_target = random.randint(0,len(enemies))
                    print(f"il vise {enemies[nb_target].nom}")
                
                    enemies[nb_target].subir_degats(aly.attaquer())
                    if enemies[nb_target].pv == 0 :
                        print(f"{enemies[nb_target].nom} est mort")
                    else :
                        print(f"{enemies[nb_target].nom} est a {enemies[nb_target].pv}")


                    if aly.nom == "grievious":
                        print("grievious attaque une seconde fois")


                        nb_target = random.randint(0,len(enemies))
                        print(f"il vise {enemies[nb_target].nom}")
                
                        enemies[nb_target].subir_degats(aly.attaquer())
                        if enemies[nb_target].pv == 0 :
                            print(f"{enemies[nb_target].nom} est mort")
                            enemies[nb_target].pop


                        else :
                            print(f"{enemies[nb_target].nom} est a {enemies[nb_target].pv}")


                for enemie in enemies:
                    print(f"{enemie.nom} attaque")
                    nb_target = random.randint(0,len(self.inventaire.equipage) + 1)
                    try:
                        print(f"il vise {self.inventaire.equipage[nb_target].nom}")
                    except ValueError:
                        print("il vise Pépé")
                
                    try:
                        self.inventaire.equipage[nb_target].subir_degats(enemie.attaquer())
                        if self.inventaire.equipage[nb_target].pv == 0 :
                            print(f"{self.inventaire.equipage[nb_target].nom} est mort")
                        else :
                            print(f"{self.inventaire.equipage[nb_target].nom} est a {self.inventaire.equipage[nb_target].pv}")
                    except ValueError:
                        self.pp.subir_degats(enemie.attaquer())
                        if self.pp.pv == 0 :
                            print(f"{self.pp.nom} est mort")
                        else :
                            print(f"{self.pp.nom} est a {self.pp.pv}")
                
                
                    if self.pp.pv == 0 :
                        print("GAME OVER")
                        play = False
                        mort = True


    def changer_arme(self)->None:
        print("="*8)
        print("CHANGEMENT D'ARME")
        print("="*8)
        nb = 0
        for arme in self.inventaire.armes:
            print(f"{nb}.{arme}")
            nb += 1 
        encore = True
        while encore:
            try:
                choix = int(input("quel arme  voulez vous equiper?: "))
                self.pp.armes[1] = self.inventaire.armes[choix]
                encore = False
            except ValueError:
                print("choix invalide, recommencez")


