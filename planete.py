class Planete:
    def __init__(self, nom: str, co: int, occupe: list[Personnage], detruit: bool)-> None:
        """_summary_

        Args:
            nom (str): cest le nom connard
            co (int): la distance de la planete
            occupe (list[Personnage]): quel perso sont sur la planete
            detruit (bool): si la planete est dettruit
        """
        self.nom = nom
        self.co = co
        self.occupe = occupe
        self.detruit = detruit

    def to_dick(self)-> dict:
        """_summary_

        Returns:
            dict: prepare la planete pour le json
        """
        return {"nom": self.nom, "co": self.co, "occupe": self.occupe, "detruit": self.detruit}
    


