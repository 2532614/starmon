from arme import Arme
from armure import Armure
import random

class Perso():
    """personnages
    """
    def __init__(self, nom:str, groupe:str, race:str, pv:int, armes:list[Arme], armure:Armure,) -> None:
        """cré le personnage

        Args:
            nom (str): nom du personnage
            groupe (str): classe sociale du personnage
            race (str): race du personnage
            pv (int): pv du personnage
            armes (list[Arme]): armes du personnage
            armure (Armure): armure du personnage
            force (bool): présence de force ou non
        """
        self.nom = nom
        self.groupe = groupe
        self.race = race
        self._pv = 0
        self._pv_max = 0
        self.armes = armes
        self.armure = armure

        self.pv = pv
        self.pv_max = pv

    @property
    def pv(self) -> int:
        return self._pv
    
    @pv.setter
    def pv(self, pv:int) -> None:
        if pv > 0:
            self._pv = pv
        else:
            pv = 0
    
    @property
    def pv_max(self) -> int:
        return self._pv_max
    
    @pv_max.setter
    def pv_max(self, pv:int) -> None:
        if pv > 0:
            self._pv_max = pv
        else:
            pv = 0
    
    def attaquer(self) -> int:
        """attaquer un personnage

        Returns:
            int: degats infliger
        """
        arme_utiliser = random.randint(0, 9)
        if arme_utiliser == 0:
            if "(cool)" in self.armes[0].nom:
                if random.randint(0, 9) == 9:
                    return self.armes[0].damage * 10
            elif "(pas cool)" in self.armes[2].nom:
                if random.randint(0, 9) == 9:
                    return int(self.armes[2].damage / 10)
            return self.armes[0].damage

        if len(self.armes) == 3 and arme_utiliser < 7:
            if "(cool)" in self.armes[2].nom:
                if random.randint(0, 9) == 9:
                    return self.armes[2].damage * 10
            elif "(pas cool)" in self.armes[2].nom:
                if random.randint(0, 9) == 9:
                    return int(self.armes[2].damage / 10)
            return self.arme[2].damage
        if "(cool)" in self.armes[1].nom:
            if random.randint(0, 9) == 9:
                return self.armes[1].damage * 10
        elif "(pas cool)" in self.armes[1].nom:
            if random.randint(0, 9) == 9:
                return int(self.armes[1].damage / 10)
        return self.armes[1].damage
        
    def subir_degats(self, degats_subit:int) -> None:
        """channge la vie d'un personnage

        Args:
            degats_subit (int): _description_
        """
        if "(cool)" in self.armes[1].nom:
            if random.randint(0, 3) == 3:
                pass
            else:
                self.armure.pv -= degats_subit
                if self.armure.pv < 0:
                    self.pv += self.armure.pv
                    self.armure.pv = 0
        elif "(pas cool)" in self.armes[1].nom:
            if random.randint(0,1) == 1:
                self.pv += self.armure.pv
                self.armure.pv = 0
        else:
            self.armure.pv -= degats_subit
            if self.armure.pv < 0:
                self.pv += self.armure.pv
                self.armure.pv = 0

    def to_dick_uh_i_mean_dict(self) -> dict:
        """prépare le personnage pour le convertir en json 

        Returns:
            dict: les info du personnage en dict
        """
        dick = {"nom": self.nom, "groupe": self.groupe, "race": self.race, "pv": self.pv, "armes": [], "armure": self.armure.nom}
        for arme in self.armes:
            dick["armes"].append(arme.nom)
        return dick
    
    def heal(self, carottes:int) -> int:
        """soigne le perso et réduit les carottes

        Args:
            carottes (int): nombre de carotte dans l'inventaire

        Returns:
            int: nombre de carottes restantes après les soins
        """
        if carottes > self.pv_max - self.pv:
            carottes -= self.pv_max - self.pv
            self.pv = self.pv_max
            return carottes
        else:
            pv += carottes
            return 0
        