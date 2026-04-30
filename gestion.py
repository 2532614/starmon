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
                planete.append(Planete(planete["name"], planete["orbital_period"]))
            
            dragon_request = requests.Session().get("https://akabab.github.io/starwars-api/api/all.json").json()
            for perso in dragon_request:
                if "Jabba Desilijic Tiure" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Hutt clan", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("poing")), self.shop.armurerie("none")))
                elif "Darth Vader" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 400, (self.shop.armurerie("etranglement de force"), self.shop.armurerie("sabre vader"), self.shop.armurerie("poing vader")), self.shop.armurerie("none")))
                elif "Darth Maul" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 200, (self.shop.armurerie("etranglement de force"), self.shop.armurerie("double sabre maul"), self.shop.armurerie("mini poing")), self.shop.armurerie("none")))
                elif "Palpatine" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 1000, (self.shop.armurerie("poing sidious"), self.shop.armurerie("eclaire(badass)")), self.shop.armurerie("none")))
                elif "Grievous" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Separatist Droid", perso["species"], 200, (self.shop.armurerie("mini poing"), self.shop.armurerie("sabre")), self.shop.armurerie("none")))
                elif "Sith" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("sabre_laser"), self.shop.armurerie("la force(trop mainsteam)")), self.shop.armurerie("none")))
                elif "Jedi Order" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Jedi", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("sabre_laser"), self.shop.armurerie("la force(trop mainsteam)")), self.shop.armurerie("none")))
                elif "IG-88" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 29, (self.shop.armurerie("poing"), self.shop.armurerie("Pistolet blaster DL-44")), self.shop.armurerie("none")))
                elif "C-3PO" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("C3-poingO")), self.shop.armurerie("none")))
                elif "droid" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("zap")), self.shop.armurerie("none")))
                elif "wookiee" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "wookie", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("arbalete laser(cool)")), self.shop.armurerie("none")))
                elif "Squadron" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "colored Squadron", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster DC17")), self.shop.armurerie("none")))
                elif "New Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "New Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
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
                elif "Galactic Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
                self.personnages.append(Perso("battle droid B1", "Droid", "Droid", 30, (self.shop.armurerie("poing"), self.shop.armurerie("fusil blaster E-5(pas cool)")), self.shop.armurerie("none")))
                self.personnages.append(Perso("battle droid B2", "Droid", "Droid", 70, (self.shop.armurerie("poing"), self.shop.armurerie("blaster integre")), self.shop.armurerie("none")))
                self.personnages.append(Perso("clone", "clone army", "clone", 100, (self.shop.armurerie("poing"), self.shop.armurerie("DC15 blaster"), self.shop.armurerie("blaster DC17", "blaster(pas cool)")), self.shop.armurerie("none")))
                self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, (self.shop.armurerie("poing"), self.shop.armurerie("blaster(pas cool)")), self.shop.armurerie("none")))
