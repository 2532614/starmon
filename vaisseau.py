class Vaisseau:
    def __init__(self, nom: str, modele: str, prix: int,vitesse: float):
        self.nom = nom
        self.modele = modele
        self._prix = 0
        self._vitesse = 0

        self.prix = prix
        self.vitesse = vitesse



    def to_dick_uh_i_mean_dict(self)-> dict:
        """transforme l'objet en dictionnaire

        Returns:
            dict: un dictionnaire
        """
        return {"nom": self.nom, "modele": self.modele, "prix": self.prix, "cargo": self.cargo, "vitesse": self.vitesse, "capacite_equipe": self.capacite_equipe}
    

    def __str__(self)-> None:

        espaces = 7 - len(str(self.prix))
        return f"{self.prix}" + " " * espaces + f"credits,   {self.nom}"


    @property
    def prix(self) -> int:
        return self._prix
    
    @prix.setter
    def prix(self, prix:int) -> None:
        if prix >= 0:
            self._prix = prix

    @property
    def cargo(self) -> int:
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo:int) -> None:
        if cargo > 31:
            self._cargo = cargo


    @property
    def vitesse(self) -> int:
        return self._vitesse
    
    @vitesse.setter
    def vitesse(self, vitesse:int) -> None:
        if vitesse > 0:
            self._vitesse = vitesse

    @property
    def capacite_equipe(self) -> int:
        return self._capacite_equipe
    
    @capacite_equipe.setter
    def capacite_equipe(self, capacite_equipe:int) -> None:
        if capacite_equipe > 0:
            self._capacite_equipe = capacite_equipe






        