class Vaisseau:
    def __init__(self, nom: str, modele: str, prix: int, cargo: int, vitesse: float, capacite_equipe: int):
        self.nom = nom
        self.modele = modele
        self.prix = prix
        self.cargo = cargo
        self.vitesse = vitesse
        self.capacite_equipe = capacite_equipe


    def to_dick(self)-> dict:
        return {"nom": self.nom, "modele": self.modele, "prix": self.prix, "cargo": self.cargo, "vitesse": self.vitesse, "capacite_equipe": self.capacite_equipe}
    

    def __str__(self)-> None:

        espaces = 7 - len(str(self.prix))
        return f"{self.prix}" + " " * espaces + f"credits,   {self.nom}"






        