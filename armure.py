class Armure:
    def __init__(self, nom: str, pv:int, prix:int) -> None:
        """_summary_

        Args:
            nom (str): cest le nom
            pv (int): nombre de degat encaissable avant de se detruire
            prix (int): crash le cash
        """
        self._pv = 0
        self._prix = 0
        self.nom = nom

        self.pv = pv
        self.prix = prix


    def __str__(self)-> None:
        """affiche la description de l'Arm-ure dans le shop

        Returns:
            str: la description de l'armure
        """
        espaces = 9 - len(str(self.prix))
        return f"{self.prix}" + " " * espaces + f"credits,   {self.nom}"
    
    @property
    def prix(self)-> int:
        return self._prix
    
    @prix.setter
    def prix(self, prix:int)-> int:
        if prix >= 0:
            self._prix = prix
        elif prix < 0 :
            self._prix = 0

    @property
    def pv(self)-> None:
        return self._pv
    
    @pv.setter
    def pv(self,pv)-> int:
        if pv >= 0:
            self._pv = pv
        elif pv < 0 :
            self._pv = 0 

