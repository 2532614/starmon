import requests
from arme import Arme
from armure import Armure
from vaisseau import Vaisseau
from planete import Planete
from inventaire import Inventaire
from perso import Perso
from shop import Shop
import random

class Gestion():
    """gère le programe
    """
    def __init__(self) -> None:
        """decole la gestion du programme
        """
        self.personnages:list[Perso] = []
        self.shop = Shop()
        self.planetes = []
    
    def call_apis(self) -> None:
        """appel des apis
        """
        try:
            self.charger_json()
        except FileNotFoundError:

            dragon_request = requests.Session().get("https://swapi.info/api/planets").json()
            for planete in dragon_request:
                if planete["name"] == "Mustafar":
                    mustafar = Planete(planete["name"], planete["orbital_period"])
                self.planetes.append(Planete(planete["name"], planete["orbital_period"]))
            self.planetes = self.tri_planete(self.planetes)
            
            planete = mustafar
            for position in range(8):
                self.planetes[50+position], planete = planete, self.planetes[50+position]
            self.planetes.append(planete)
            self.planetes.append(Planete("Death Star", 0))

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
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 1000, (self.shop.armurerie("poing sidious"), self.shop.armurerie("eclaire(badass)")), self.shop.armurerie("none")))
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
                self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
                for id_planete in range(61):
                    if id_planete != 21 or id_planete != 31 or id_planete != 41 or id_planete != 51 or id_planete != 61:
                        self.planetes[id_planete].occupants.append(self.personnages[len(self.personnages)])
                        
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
