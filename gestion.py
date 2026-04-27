import requests
from arme import Arme
from armure import Armure
from vaisseau import Vaisseau
from planete import Planete
from inventaire import Inventaire
from perso import Perso
from shop import Shop

class Gestion():
    """gère le programe
    """
    def __init__(self) -> None:
        """decole la gestion du programme
        """
        personnages:list[Perso] = []
        shop = Shop()
    
    def call_apis(self) -> None:
        """appel des apis
        """
        try:
            self.charger_json()
        except FileNotFoundError:
            
            dragon_request = requests.Session().get("https://akabab.github.io/starwars-api/api/all.json").json()
            for perso in dragon_request:
                if "Sith" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Sith", perso["species"], 100, shop[""], shop[""]))
                elif "Jedi Order" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Jedi", perso["species"], 100, shop[""], shop[""]))
                elif "droid" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "Droid", perso["species"], 100, shop[""], shop[""]))
                elif "wookiee" in perso["species"]:
                    self.personnages.append(Perso(perso["name"], "wookie", perso["species"], 100, shop[""], shop[""]))
                elif "Squadron" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "colored Squadron", perso["species"], 100, shop[""], shop[""]))
                elif "New Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "New Republic", perso["species"], 100, shop[""], shop[""]))
                elif "Resistance" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Resistance", perso["species"], 100, shop[""], shop[""]))
                elif "Galactic Republic" in perso["affiliations"]:
                    self.personnages.append(Perso(perso["name"], "Galactic Republic", perso["species"], 100, shop[""], shop[""]))
                elif "Jabba Desilijic Tiure" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Hutt clan", perso["species"], 100, shop[""], shop[""]))
                elif "Grievous" in perso["name"]:
                    self.personnages.append(Perso(perso["name"], "Separatist Droid", perso["species"], 100, shop[""], shop[""]))
