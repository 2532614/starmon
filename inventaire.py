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
    
    def voir_inventaire(self)->None:
        try:
            print("1. argent")
            print("2. equipage")
            print("3. armes")
            print("4. armures")
            print("5. vaisseau")
            print("6. consommable")
            print("7. tout voir")
            choix = int(input("que voulez vous voir?: "))
            match choix:
                case 1:
                    print("="*8)
                    print(f"vous avez {self.argent} credits")
                    print("="*8)
                case 2:
                    print("="*8)
                    print("votre équipage contient:")
                    for x in self.equipage:
                        print(x.nom)
                    print("="*8)
                case 3:
                    print("="*8)
                    for x in self.armes:
                        print(f"{x.nom}: {x.damage} damage")
                    print("="*8)
                case 4:
                    print("="*8)
                    for x in self.armures:
                        print(f"{x.nom}: {x.pv} point de vie restant")
                    print("="*8)
                case 5:
                    print("="*8)
                    print(f"vous voyager à bord du {self.vaisseau.nom}")
                    print("="*8)
                case 6:
                    print("="*8)
                    print(f"vous avez {self.nb_carotte} carottes et {self.nb_carburant} unités de carburant")
                    print("="*8)
                case 7:
                    print("="*8)
                    print(f"vous avez {self.argent} credits")
                    print("="*8)
                    print("votre équipage contient:")
                    for x in self.equipage:
                        print(x.nom)
                    print("="*8)
                    for x in self.armes:
                        print(f"{x.nom}: {x.damage} damage")
                    print("="*8)
                    for x in self.armures:
                        print(f"{x.nom}: {x.pv} point de vie restant")
                    print("="*8)
                    print(f"vous voyager à bord du {self.vaisseau.nom}")
                    print("="*8)
                    print(f"vous avez {self.nb_carotte} carottes et {self.nb_carburant} unités de carburant")
                    print("="*8)
                case _:
                    pass

        except ValueError:
            pass

