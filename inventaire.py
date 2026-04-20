from arme import Arme
from armure import Armure
from vaisseau import Vaisseau
from perso import Perso
from nico import Nico

class Inventaire():
    """tous les biens (nico tu en fais parti) appertenant au joueur
    """
    def __init__(self, armes:list[Arme], armures:list[Armure], argent:int, vaisseau:Vaisseau, equipage:list[Perso]):
        """cré les différente

        Args:
            armes (list[Arme]): les armes du joueur
            armures (list[Armure]): les armures du joueur
            argent (int): l'argent du joueur
            vaisseau (Vaisseau): le vaisseau du joueur
            equipage (list[Perso]): l'equipage du joueur
        """
        self.armes = armes
        self.armures = armures
        self.argent = argent
        self.vaisseau = vaisseau
        self.equipage = equipage
        self.nico = Nico()