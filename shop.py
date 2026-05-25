from arme import Arme
from armure import Armure
from inventaire import Inventaire
from vaisseau import Vaisseau
import random



class Shop():
    def __init__(self):
        self.armes = [
            Arme("DC15 blaster", 20, 18000),
            Arme("blaster DC17", 18, 10000),
            Arme("blaster(pas cool)",15, 1000),
            Arme("sabre laser vert", 32, 25000),
            Arme("sabre laser bleu", 32, 27000),
            Arme("sabre laser rouge",32, 35000),
            Arme("sabre laser jaune",32, 42000),
            Arme("sabre laser amethyste(cool)",32, 100000),
            Arme("sabre laser_doree(Cool)",32, 450000),
            Arme("dark saber(cool)",32, 500000),
            Arme("double sabre laser rouge",34, 56000),
            Arme("double sabre laser bleu",34, 43200),
            Arme("double sabre laser vert",34, 40000),
            Arme("double sabre laser jaune(pas cool)",34, 66999),
            Arme("pistolet westar 35(cool)", 17, 15000),
            Arme("fusil blaster lourd DLT-20A", 29, 23000),
            Arme("Pistolet blaster DL-44", 19, 10000 ),
            Arme("arbalete laser(cool)", 32, 25001),
            Arme("vibro-lame(petite)(cool)",10, 3000),
            Arme("vibro-lame(moyenne)", 15, 7000),
            Arme("vibro-lame(grande)",20, 9999),
            Arme("fusil blaster E-5(pas cool)", 5, 69),
            Arme("lance-flamme(cool)", 18, 18000),
            Arme("blaster integre", 10, 0),
            Arme("zap", 6, 0),
            Arme("sabre vader", 64, 0),
            Arme("double sabre maul", 49, 0),
            Arme("mini poing", 20, 0),
            Arme("C3-poingO", -2, 0),
            Arme("poing(pas cool)" , 1, 0),
            Arme("poing vader", 40, 0),
            Arme("etranglement de force", 85, 0),
            Arme("la force(trop mainsteam)", 20, 0),
            Arme("poing sidious",60, 0),
            Arme("sabre laser", 32, 0),
            Arme("eclaire(badass)", 100, 0),
            Arme("poing", 1, 0),
            Arme("branch", 4, 0)
            ]
        
        self.consommable = ["ration", "carburant"]
        self.parti_vaisseau = [{"nom": "renforcement de coque", "prix": 42500}, {"nom": "tourelles optimisées", "prix": 50000}, {"nom":"moteur SRB42", "prix": 57500}, {"nom": "hyperdrive class 9", "prix": 65000}]

        self.armures = [
            Armure("armure mandalorienne(cool)", 200, 70000),
            Armure("armure de clone phase 1", 81, 8100),
            Armure("armure de clone phase 2", 110, 13000),
            Armure("armure de clone commando", 130, 17000),
            Armure("armure de trooper(pas cool)", 20, 100),
            Armure("armure de ferailles(pas cool)", 35, 20),
            Armure("armure de chasseur de Prime", 80, 8000),
            Armure("armure de chevalier jedi", 100, 10020),
            Armure("armure de sith", 100, 10020),
            Armure("armure katarn(cool)", 175, 50000),
            Armure("plot armor", 100000, 0),
            Armure("none", 0, 0)
            ]
        
        self.vaisseaux = []

    def armurerie(self, nom:str) -> Arme | Armure:
        """prend le nom d'un arme/armure et retourne l'objet correspondant

        Args:
            nom (str): le nom de l'objet à retourner

        Returns:
            Arme | Armure: l'objet à retourner
        """
        for arme in self.armes:
            if nom == arme.nom:
                return arme.copy()
        for armure in self.armures:
            if nom == armure.nom:
                return armure.copy()
            
    def vaisseau_pp(self, nom:str, inventaire:Inventaire) -> None:
        """prend le nom d'un vaisseau et met le vaisseau correspondant dans l'inventaire

        Args:
            nom (str): le nom du vaisseau à mettre dans l'inventaire
            inventaire (Inventaire): l'inventaire du pp
        """
        for vaisseau in self.vaisseaux:
            if vaisseau.nom in nom:
                inventaire.vaisseau = vaisseau.copy()
                if " (modifié)" in nom:
                    inventaire.vaisseau.nom = f"{inventaire.vaisseau.nom} (modifié)"

    def print_black_marcket(self) -> None:
        nb=0

        print("="*15)
        print(" LES ARMES")
        print("="*15)

        for arme in self.armes:
            if arme.prix != 0:
                if nb < 10:
                    print(f"{nb}.  {arme}")
                else:
                    print(f"{nb}. {arme}")
                nb += 1
        print("")
        print("="*15)
        print(" LES ARMURES")
        print("="*15)

        for armure in self.armures:
            if armure.prix != 0:
                print(f"{nb}. {armure}")
                nb += 1
                      
        print("")
        print("="*15)
        print(" LES CONSOMMABLES")
        print("="*15)
        for x in range(2):
            print(f"{nb}. 1         credit,    {self.consommable[x]}")
            nb += 1

        print("")
        print("="*15)
        print(" LES AMÉLIORATIONS DE VAISSEAU")
        print("="*15)
        for partie in self.parti_vaisseau:
            print(f"{nb}. {partie["prix"]}     credit,    {partie["nom"]}")
            nb += 1

        print("="*100)
        print(" LES VAISSEAUX")
        print("="*100)

        for vaisseau in self.vaisseaux:
            if vaisseau.prix != 0:
                print(f"{nb}. {vaisseau}")
                nb += 1
        print("")
        print(f"{nb}. ne rien acheter")
        print("")
        
    def print_marcket(self)-> None:
        nb = 0
        print("="*100)
        print(" LES VAISSEAUX")
        print("="*100)

        for vaisseau in self.vaisseaux:
            if vaisseau.prix != 0:
                if nb < 10:
                    print(f"{nb}.  {vaisseau}")
                else:
                    print(f"{nb}. {vaisseau}")
                nb += 1


        print("")
        print("="*15)
        print(" LES CONSOMMABLES")
        print("="*15)
        for x in range(2):
            print(f"{nb}. 1         credit,    {self.consommable[x]}")
            nb += 1
        print("")
        print(f"{nb}. ne rien acheter")
        print("")


    def acheter(self, inventaire:Inventaire)-> None:
        encore = True
        while encore:
            try:
                choix =  input("quel shop voulez-vous allez?(1. marcket, 2. black marcket, 0. quiter): ")

                if choix == "1":
                    self.print_marcket()
                    try:
                        choix2 = int(input("que voulez vous acheter?(uniquelement le #): "))
                        if choix2 >= 0 and choix2 <= 34:

                            if inventaire.argent >= self.vaisseaux[choix2].prix:
                                inventaire.spend(self.vaisseaux[choix2].prix, False, True)
                                inventaire.vaisseau = self.vaisseaux[choix2].copy()
                                print(f"vous avez acheter le {self.vaisseaux[choix2].nom}")
                            else:
                                print("vous n'avez pas les fonds necessaire")
                                
                        elif choix2 >= 35 and choix2 <= 36:
                            try:
                                n = int(input("combien en voulez vous: "))
                                if n < 0:
                                    print("valeur invalide")
                                elif inventaire.argent >= n:
                                    inventaire.spend(n, False, True)
                                    if choix2 == 35 : 
                                        inventaire.nb_carotte += n
                                        print(f"vous avez acheter {n} carottes")
                                    elif choix2 == 36:
                                        inventaire.nb_carburant += n
                                        print(f"vous avez acheter {n} carburant")
                                else:
                                    print("vous n'avez pas les fonds necessaire")
                            except ValueError:
                                print("valeur invalide")
                        elif choix2 == 37:
                            print("vous n'avez rien acheter")
                        else:
                            print("transaction non concluse")
                    except ValueError:
                        print("transaction non concluse")




                    encore = False

                elif choix == "2":
                    self.print_black_marcket()
                    try:
                        choix2 = int(input("que voulez vous acheter?(uniquelement le #): "))
                        if choix2 >= 0 and choix2 <= 22:
                            if inventaire.argent >= self.armes[choix2].prix:
                                inventaire.spend(int(random.randint(101, 111) / 100) * (self.armes[choix2].prix), True, False)
                                inventaire.armes.append(self.armes[choix2])
                                print(f"vous avez acheter un {self.armes[choix2].nom}")
                            else:
                                print("vous n'avez pas les fonds necessaire")
                        elif choix2 >= 23 and choix2 <= 32:
                            if inventaire.argent >= self.armures[choix2 - 23].prix:
                                inventaire.spend(int(random.randint(101, 111) / 100) * (self.armures[choix2 - 23].prix), True, False)
                                inventaire.armures.append(self.armures[choix2 - 23].copy())
                                print(f"vous avez acheter un {self.armures[choix2 - 23].nom}")
                            else:
                                print("vous n'avez pas les fonds necessaire")
                        elif choix2 >= 33 and choix2 <= 34:
                            try:
                                n = int(input("combien en voulez vous: "))
                                if n < 0:
                                    print("valeur invalide")
                                elif inventaire.argent >= n:
                                    inventaire.spend((int(random.randint(101, 111) / 100) * n), True, False)
                                    if choix2 == 33 : 
                                        inventaire.nb_carotte += n
                                        print(f"vous avez acheter {n} carottes")
                                    elif choix2 == 34:
                                        inventaire.nb_carburant += n
                                        print(f"vous avez acheter {n} carburant")
                                else:
                                    print("vous n'avez pas les fonds necessaire")
                            except ValueError:
                                print("valeur invalide")
                        elif choix2 >= 35 and choix2 <= 38:
                            if inventaire.argent >= self.parti_vaisseau[35 - choix2]["prix"]:
                                inventaire.spend(int(random.randint(101, 111) / 100) * (self.parti_vaisseau[choix2 - 35]["prix"]), True, False)
                                try :
                                    inventaire.vaisseau.nom = f"{inventaire.vaisseau.nom} (modifié)"
                                    print(f"vous avez acheter une modification de vaisseau")
                                except:
                                    pass
                            else:
                                print("vous n'avez pas les fonds necessaire")
                        elif choix2 >= 39 and choix2 <= 73 :
                            if inventaire.argent >= self.vaisseaux[choix2 - 39].prix:
                                inventaire.spend(int(random.randint(101, 111) / 100) * (self.vaisseaux[choix2 - 39].prix), True, False)
                                inventaire.vaisseau = self.vaisseaux[choix2 - 39].copy()
                                print(f"vous avez acheter le {self.vaisseaux[choix2 - 39].nom}")
                            else:
                                print("vous n'avez pas les fonds necessaire")
                        elif choix2 == 74:
                            print("vous n'avez rien acheter")
                        else:
                            print("choix inccompris")
                    except ValueError:
                        print("transaction non concluse")

                    encore = False

                elif choix == "0":
                    print("vous etes parti")
                    print("")
                    encore = False
                
                else:
                    print("valeur invalide")
                    print("")

            except ValueError:
                pass
        






    

    