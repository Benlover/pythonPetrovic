from datetime import datetime
from random import randint
from modele.station import Station

class Approvisionnement:
     id_approvisionnement :int
     qte_gallon_gazoline: int
     qte_gallon_diesel: int
     date_app: datetime

#    ID, Station, quantité gallon Diesel, Quantité gallon Gazoline, date app.
     def __init__(self,qte_gallon_gazoline: int = 0 , qte_gallon_diesel:int = 0):
        self.id_approvisionnement = randint(1,100)
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.qte_gallon_diesel = qte_gallon_diesel
        self.date_app = datetime.now()
       
     def __str__(self):
         return f"\n Id de l\'approvisionnement {self.id_approvisionnement}" \
                f"\n Quantité total de galon diesel commande {self.qte_gallon_gazoline} " \
                f"\n Quantité total de galon diesel commandé {self.qte_gallon_diesel }" \
                f"\ date de l'\approvisionnenment {self.date_app} "       


