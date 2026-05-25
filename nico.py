from perso import Perso
import random

class Nico(Perso):
    """c toi bro
    """
    def __init__ (self, nom, groupe, race, pv, armes, armure) -> None:
        """ça te defini
        """
        self.to_dick_uh_i_mean_dict = {"est ma pute":True, "est utile":False, "est à l heure":False, "est pas drole":True, "est une salope":True, "est capable d ecrire en francais":False, "est dans la mère à corriveau":True, "est un rat":True, "est_soumit": True}
        super().__init__(nom, groupe, race, pv, armes, armure)
    
    @property
    def pv(self):
        return super().pv
    
    @pv.setter
    def pv(self, pv:int) -> None:
        if pv > 0:
            self._pv = pv
        else:
            self._pv = 0
    @property
    def pv_max(self):
        return super().pv_max
    
    @pv_max.setter
    def pv_max(self, pv:int) -> None:
        if pv > 0:
            self._pv_max = pv
        else:
            pv = 0

    def attaquer(self):
        ap = "'"
        match random.randint(0,3):
            case 0:
                print(f'Nico: "Elle j{ap}y vends de la drogue"')
            case 1:
                print(f'Nico: "Coding session"')
            case 2:
                print(f'Nico: "Chu votre pute"')
            case 3:
                print(f'Nico: "Vous êtes mes esclaves"')
            case 4:
                print(f'Nico: "Arrêtez de m{ap}intimider"')
        return 0
        
    def copy(self):
        return Nico(self.nom, self.groupe, self.race, self.pv, self.armes.copy(), self.armure)