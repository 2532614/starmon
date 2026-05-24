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
        self.transactions = [0]
        self.mark = [0]
        self.black = [0]
        self.money = [0]
        

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
            print("=" * 100)
            print("")
            print("1. argent")
            print("2. equipage")
            print("3. armes")
            print("4. armures")
            print("5. vaisseau")
            print("6. consommable")
            print("7. tout voir")
            choix = int(input("que voulez vous voir?: "))
            print("")
            match choix:
                case 1:
                    print("="*8)
                    print("")
                    print(f"vous avez {self.argent} credits")
                    print("")
                    print("="*8)
                case 2:
                    print("="*8)
                    print("")
                    print("votre équipage contient:")
                    for perso in self.equipage:
                        print(perso.nom)
                    print("")
                    print("="*8)
                case 3:
                    print("="*8)
                    print("")
                    for arme in self.armes:
                        print(f"{arme.nom}: {arme.damage} damage")
                    print("")
                    print("="*8)
                case 4:
                    print("="*8)
                    print("")
                    for armure in self.armures:
                        print(f"{armure.nom}: {armure.pv} point de vie restant")
                    print("")
                    print("="*8)
                case 5:
                    print("="*8)
                    print("")
                    print(f"vous voyager à bord du {self.vaisseau.nom}")
                    print("")
                    print("="*8)
                case 6:
                    print("="*8)
                    print("")
                    print(f"vous avez {self.nb_carotte} carottes et {self.nb_carburant} unités de carburant")
                    print("")
                    print("="*8)
                case 7:
                    print("="*8)
                    print("")
                    print(f"vous avez {self.argent} credits")
                    print("")
                    print("="*8)
                    print("")
                    print("votre équipage contient:")
                    for perso in self.equipage:
                        print(perso.nom)
                    print("")
                    print("="*8)
                    print("")
                    print("vos armes en stock sont:")
                    for arme in self.armes:
                        print(f"{arme.nom}: {arme.damage} damage")
                    print("")
                    print("="*8)
                    print("")
                    print("vos armures en stock sont:")
                    for armure in self.armures:
                        print(f"{armure.nom}: {armure.pv} point de vie restant")
                    print("")
                    print("="*8)
                    print("")
                    print(f"vous voyager à bord du {self.vaisseau.nom}")
                    print("")
                    print("="*8)
                    print("")
                    print(f"vous avez {self.nb_carotte} carottes et {self.nb_carburant} unités de carburant")
                    print("")
                    print("="*8)
                    print("")
                case _:
                    print("valeur invalide")

        except ValueError:
            print("valeur invalide")

    def spend(self, argent:int, black:bool, mark:bool) -> None:
        if self.argent < argent:
            argent = self.argent
        self.argent -= argent
        self.transactions.append(self.transactions[len(self.transactions) - 1] + 1)
        self.money.append(self.argent)
        if black:
            self.black.append(self.black[len(self.black) - 1] + argent)
            self.mark.append(self.mark[len(self.mark) - 1])
        elif mark:
            self.mark.append(self.mark[len(self.mark) - 1] + argent)
            self.black.append(self.black[len(self.black) - 1])
        else:
            self.black.append(self.black[len(self.black) - 1])
            self.mark.append(self.mark[len(self.mark) - 1])
