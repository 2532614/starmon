from perso import Perso

class Planete:
    def __init__(self, nom: str, co: int, detruit: bool)-> None:
        """_summary_

        Args:
            nom (str): cest le nom connard
            co (int): la distance de la planete
            occupe (list[Personnage]): quel perso sont sur la planete
            detruit (bool): si la planete est dettruit
        """
        self.nom = nom
        self._co = 0
        self.occupants = []
        self.detruit = detruit

        self.co = co

    def to_dick_uh_i_mean_dict(self)-> dict:
        """_summary_

        Returns:
            dict: prepare la planete pour le json
        """
        dick = {"nom": self.nom, "co": self.co, "occupants": [], "detruit": self.detruit}
        for occupant in self.occupants:
            dick["occupants"].append(occupant.nom)
        return dick
    
    @property
    def co(self) -> int:
        return self._co
    
    @co.setter
    def co(self, co:int) -> None:
        if isinstance(co, str):
            self._co = co
        elif co >= -1:
            self._co = co

    def __str__(self):
        return self.nom


