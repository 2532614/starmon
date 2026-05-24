class Arme:
    """les armes des personnages
    """
    def __init__(self, nom: str, damage: int, prix: int) -> None:
        """definit les atributs d'une arme

        Args:
            nom (str): nom de l'arme
            damage (int): domagescinfliger par l'arme
            prix (int): le prix d'achat de l'arme
        """
        self._damage = 0
        self._prix = 0
        self.nom = nom

        self.damage = damage
        self.prix = prix

    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, damage:int) -> None:
        if damage > -2:
            self._damage = damage

    @property
    def prix(self) -> int:
        return self._prix
    
    @prix.setter
    def prix(self, prix:int) -> None:
        if prix > 0:
            self._prix = prix

    def __str__(self) -> str:
        """affiche la description de l'Arme dans le shop

        Returns:
            str: la description de l'arme
        """
        espaces = 10 - len(str(self.prix))
        return f"{self.prix}" + " " * espaces + f"credits,   {self.nom}"
    
    def copy(self):
        return Arme(self.nom, self.damage, self.prix)
    
