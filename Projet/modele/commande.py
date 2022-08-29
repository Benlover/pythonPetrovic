
from datetime import datetime
from random import randint, random


class Commande:
     id_commande :int
     qte_gallon_gazoline: int
     qte_gallon_diesel: int
     date_commande: datetime
     etat_commande :str

     def __init__(self,qte_gallon_gazoline: int= 0,qte_gallon_diesel: int = 0):

          self.id_commande = randint(1,100)
          self.qte_gallon_gazoline= qte_gallon_gazoline
          self.qte_gallon_diesel= qte_gallon_diesel
          self.date_commande = datetime.now()
          self.etat_commande = 'Nouvelle'
     def __str__(self) -> str:
             return f"\n Id du commamnde : {self.id_commande}" \
               f"\n Quantite total de galon gazoline commande: {self.qte_gallon_gazoline}" \
               f"\n Quantite total de galon diesel commande : {self.qte_gallon_diesel}" \
               f"\n Date commande : {self.date_commande}" \
               f"\n Etat de la commande : {self.etat_commande}\n"