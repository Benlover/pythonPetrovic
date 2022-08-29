


class Station:
    nomStation: str
    capacite_Gazoline: int
    capacite_diesel:int
    pourcentageGazoline : float
    pourcentageDiesel : float
    qte_vendue : float

    prix_vente : int 

    prix_unitaire_gazoline :int
    prix_unitaire_diesel : int

    def __init__(self, nomStation: str = '', capacite_Gazoline: int = 1,capacite_diesel: int = 1):
        self.nomStation = nomStation
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel
        self.pourcentageGazoline = 0
        self.pourcentageDiesel = 0
        self.prix_vente = 0
        self.qte_vendue = 0
        self.prix_unitaire_gazoline = 250
        self.prix_unitaire_diesel = 350

        if capacite_Gazoline > 0:
             self.pourcentage(qte_vendue = self.capacite_Gazoline, type_gaz = 'gazoline')
        if capacite_diesel > 0:
            self.pourcentage(qte_vendue=self.capacite_diesel, type_gaz= 'diesel')


    #QANTITE GAZOLINE UTILISE
    def quantite_gazoline_utilise(self)->float:   
        return self.pourcentageGazoline * self.capacite_Gazoline / 100
        

    #QANTITE GAZOLINE UTILISE
    def quantite_diesel_utilise(self)->float:
      return self.pourcentageDiesel * self.capacite_diesel / 100


    #QUANTITE GALLON DIESEL DISPONIBLE
    def quantite_diesel_disponible(self,qte_vendue: float =0 )->float:
        return self.capacite_diesel - qte_vendue

    #QUANTITE GALLON GAZOLINE DISPONBLE
    def quantite_gazoline_disponible(self,qte_vendue: float =0 )->float:
        return self.capacite_Gazoline - qte_vendue
    


    def pourcentage(self,qte_vendue:float , type_gaz:str)->None:
        match type_gaz:
            case 'gazoline':
                self.pourcentageGazoline = (qte_vendue * 100) /self.capacite_Gazoline
            case 'diesel':
                self.pourcentageDiesel = (qte_vendue * 100) /self.capacite_diesel
            case default:
                print('')     

   
        
                    
