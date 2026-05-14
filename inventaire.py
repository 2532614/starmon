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
        self._argent = 0
        self.vaisseau = vaisseau
        self.equipage = equipage
        self.nico = Nico()
        self.nb_carotte = 5
        self.nb_carburant = 31

        self.argent = argent

    @property
    def argent(self) -> int:
        return self._argent
    
    @argent.setter
    def argent(self, argent) -> None:
        if argent >= 0:
            self._argent = argent
        elif argent < 0 :
            self._argent = 0

    def to_dick_uh_i_mean_dict(self) -> dict:
        """prépare l'inventaire pour le convertir en json 

        Returns:
            dict: les info de l'inventaire  en dict
        """
        dick = {"armes": [], "armures": [], "argent": self.argent, "vaisseau": self.vaisseau.nom, "equpage": []}
        for arme in self.armes:
            dick["armes"].append(arme.nom)
        for armure in self.armures:
            dick["armures"].append(armure.nom)
        for perso in self.equipage:
            dick["equipage"].append(perso.nom)

        return dick