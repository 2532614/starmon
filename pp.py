from arme import Arme
from armure import Armure
from perso import Perso
import random
class Pp(Perso):
    def __init__(self, nom, groupe, race, pv, armes, armure):
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
    
    def subir_degats(self, degats_subit):
        return super().subir_degats(degats_subit)
    
    def to_dick_uh_i_mean_dict(self):
        return super().to_dick_uh_i_mean_dict()
    
    def heal(self, carottes):
        return super().heal(carottes)
    
    def attaquer(self) -> int:
        while True:
            try:
                print("voici vos armes:")
                for (n, arme) in enumerate(self.armes):
                    print(f"{n}. {arme.nom}")
                arme = int(input("quelle arme voules vous utiliser: "))

                if "(pas cool)" in self.armes[arme].nom:
                    if random.randint(0, 9) == 9:
                        print("")
                        return int(self.armes[arme].damage / 10)
                elif "cool" in self.armes[arme].nom or "(badass)" in self.armes[arme].nom:
                    if random.randint(0, 9) == 9:
                            print("")
                            return self.armes[arme].damage * 10
                print("")
                return self.armes[arme].damage
            except ValueError:
                print("valeur impossible")
            except IndexError:
                print("valeur impossible")
