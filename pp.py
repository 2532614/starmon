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
    
    @property
    def pv_max(self):
        return super().pv_max
    
    def subir_degats(self, degats_subit):
        return super().subir_degats(degats_subit)
    
    def to_dick_uh_i_mean_dict(self):
        return super().to_dick_uh_i_mean_dict()
    
    def heal(self, carottes):
        return super().heal(carottes)
    
    def attaquer(self) -> int:
        print("voici vos armes:")
        for (n, arme) in enumerate(self.armes):
            print(f"{n}. {arme.nom}")
        arme = input("quelle arme voules vous utiliser: ")

        if "cool" in self.armes[arme] or "(badass)" in self.armes[arme]:
            if random.randint(0, 9) == 9:
                    return self.armes[arme].damage * 10
        elif "(pas cool)" in self.armes[arme].nom:
            if random.randint(0, 9) == 9:
                return int(self.armes[arme].damage / 10)
        return self.armes[arme].damage