from datetime import datetime
from random import randint

class Vente:
    id_vente : int
    qte_gallon_gazoline: int
    qte_gallon_diesel: int
    date_vente: datetime

  

    def __init__(self,capacite_Gazoline: int = 0,capacite_diesel:int = 0):
        self.IdVente = randint(1,100)
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel
        self.dateVente = datetime.now()
        self.prix_vente = 0

    def __str__(self) -> str:
        return f"\n Id du vente : {self.id_vente}" \
               f"\n Quantité total de galon diesel vente: {self.qte_gallon_gazoline}" \
               f"\n Quantité total de galon gazoline vente : {self.qte_gallon_diesel}" \
               f"\n Date Vente : {self.date_vente}" \
        
    
