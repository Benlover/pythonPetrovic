#IMPORTATION DES MODULES
from typing import ClassVar
from modele.commande import Commande
import logging
from modele.approvisionnement import Approvisionnement
from modele.station import Station
from modele.vente import Vente

class Petrole:
    s_lalue = dict
    s_tabarre = {}
    s_clercine = {}
    s_petionville = {}
    stationGenerale: list[Station]
    nomStation = ''
    capacite_Gazoline: int = 0
    capacite_diesel: int =0 
    station : Station
    diesel: ClassVar[int]
    gazoline: ClassVar[int]
    

#COLLECTION COMMANDE
    commandes:list =[Commande]
    commande = Commande()

    station: Station
#Collection pour approvisionnenment

    appro :set = (Approvisionnement)
    approvisionnement = Approvisionnement()

#Collection pour vente     
   
    ventes : list = [Vente]
    vente : Vente ()
  
    def __init__(self):
          self.s_lalue = dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_clercine= dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_tabarre = dict({
            'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          }) 
          self.s_petionville = dict({
               'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.nomStation = ''
          self.stationGenerale = []
          self.station = Station()
          self.commande = []

          
          

    def enregistrerStation(self):
        self.station.nomStation = Petrole.choixStation(message =' Choisir une station svp !!')

        try:
    
            self.station.capacite_Gazoline = int(input('Saisir la capacité de gazoline !!:'))
        except ValueError as e:
            logging.error(e)      
        try:
             self.station.capacite_diesel = int(input('Saisir la capacité de diesel !! :'))
        except ValueError as e:
            logging.error(e) 
        
      
        match self.station.nomStation.lower():
            case 'lalue':
                self.s_lalue.update(self.station.__dict__)
                self.stationGenerale.append(Station(nomStation=self.s_lalue.get('nomStation'),
                capacite_Gazoline=self.s_lalue.get('capacite_Gazoline'),capacite_diesel=self.s_lalue.get('capacite_diesel') ))

            case 'tabarre':
                self.s_tabarre.update(self.station.__dict__)
                self.stationGenerale.append(self.station)   
            case 'clercine':
                self.s_clercine.update(self.station.__dict__)
                self.stationGenerale.append(self.station)  
            case 'Petion-ville':
                self.s_petionville.update(self.station.__dict__)
                self.stationGenerale.append(self.station)

        print('Save avec succes') 

       

    def afficherStation(self):
        stat:str = Petrole.choixStation(message='Choisir une station a aficher svp' )

        match stat:

            case 'lalue':
                Petrole.afficher(self.s_lalue)
            case 'tabarre':
                Petrole.afficher(self.s_tabarre)
            case 'clercine':
                Petrole.afficher(self.s_clercine)
            case 'Petion-ville':
                Petrole.afficher(self.s_petionville)
            case default:
                print('Mauvais choix')    

    def afficherStations(self):
        if len(self.stationGenerale)>0:
          for staG in self.stationGenerale:
            print(staG) 
        else:
            print('List empty')    

    @staticmethod         
    def afficher(dicGenerale:dict):
      
             print('***************************************************')
             print(f" \n Station :{dicGenerale.get('nomStation')}"
                   f"\n capacite de stackage de gazoline {dicGenerale.get('capacite_Gazoline')} "
                   f"\n capacité de stockage diesel :{dicGenerale.get('capacite_diesel')}"
                   f"\n Pourcentage de stockage de gazoline {dicGenerale.get('pourcentageGazoline')} %" 
                   f"\n Pourcentage de stockage de diesel {dicGenerale.get('pourcentageDiesel')} % ")   
             print('*************************************************************\n ')


    def ModifierCapacite(self):
        self.nomStation = Petrole.choixStation(message='Choisir une station svp')
        match self.nomStation:
            case 'lalue':
                if len(self.s_lalue)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')

                    #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                    'nomStation': self.nomStation,
                    'capacite_Gazoline':Petrole.gazoline,
                    'capacite_diesel':Petrole.diesel
                     })
                    self.s_lalue.update(self.s_lalue)
                else:
                    print('')
                       
            case 'tabarre':
                if len(self.s_tabarre)>0:
                    Petrole.gazoline= self.s_tabarre.get('capacite_Gazoline')
                    Petrole.diesel = self.s_tabarre.get('capacite_diesel')

                        #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_tabarre.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_tabarre.update(self.s_tabarre)
            case 'clercine':
                if len(self.s_clercine)>0:
                    Petrole.gazoline= self.s_clercine.get('capacite_Gazoline')
                    Petrole.diesel = self.s_clercine.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_clercine.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_clercine.update(self.s_clercine)

            case 'Petion-ville':
                if len(self.s_petionville)>0:
                    Petrole.gazoline= self.s_petionville.get('capacite_Gazoline')
                    Petrole.diesel = self.s_petionville.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_petionville.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_petionville.update(self.s_petionville)
        print('Modifier avec Succes')        
            #   case default:
            #     print('Mauvais Choix ????')

    @staticmethod
    def choose_essence()->str:
        return input('\n a-GAZOLINE'
                     '\n b-DIESEL'
                     '\n c-LES DEUX'
                     '\n d-PRESSER POUR QUITTER'
                     '\n =====>')
           
    

    @staticmethod
    def choixStation( message: str)->str:
        while True:
            station:str = input(f'******{message}********\n'
                                 '\n a- lalue'
                                '\n b-tabarre'
                                '\n c-clercine'
                                '\n d-Petion-ville'
                                '\n ===>:')
            match station.lower():
                        case 'a':
                            return 'lalue'
                        case 'b':
                             return 'tabarre'
                        case 'c':
                            return 'clercine'
                        case 'Petion-ville':
                            return ''
                        case default:
                           print('Mauvais Choix')   
    @staticmethod                       
    def donnes():
        while True:
            Type_essence:str = Petrole.choose_essence()
            match Type_essence:
                case 'a':
                    Petrole.gazoline= int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                case 'b':
                    Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                case 'c':
                   Petrole.gazoline = int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                   Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                
                case default:
                    break


#**************************MODULE COMMANDE ******************

   
    def quantite_gazoline(self):
        totG = 0 
        if len(self.stationGenerale)>0:
          for s in self.stationGenerale:
             totG = totG + s.capacite_Gazoline
        return totG

    def quantite_diesel(self):
        totG = 0 
        if len(self.stationGenerale)>0:
          for s in self.stationGenerale:
             totG = totG + s.capacite_diesel
        return totG   

#QUANTITE TOTAL ESSENCE POUR UN STATION DONNEE
    def total_essence(self):
        return self.quantite_gazoline() + self.quantite_diesel()

#POURCENTAGE TOTAL D'ESSNCE
    
    def pourcentage_total_essence(self,qtediesel_and_gazoline_utilise :float)-> float:
        return (qtediesel_and_gazoline_utilise * 100) / self.total_essence()

# METHODE PERMETTANT ENREGISTRER UNE COMMANDE             
    def save_commande(self):
        if len(self.stationGenerale)>0:
            qtediesel_and_gazoline_utilise : float = 0
            for stat in self.stationGenerale:
                qteGazole_ut = stat.quantite_gazoline_utilise()
                qteDiese_ut = stat.quantite_diesel_utilise()
                # stat.quantite_diesel_utilise
                qtediesel_and_gazoline_utilise += qteGazole_ut + qteDiese_ut
                #Affichage des donnees 
                Petrole.afficher_qte_disponible_and_qte_utilise(station=stat,qteGazole_ut = qteGazole_ut ,qteDiese_ut = qteDiese_ut)
                pourcentageTotal :float = self.pourcentage_total_essence(qtediesel_and_gazoline_utilise=qtediesel_and_gazoline_utilise) 
            
            if pourcentageTotal >= 50:
                if self.valide_commande():
                    self.commande = Commande(qte_gallon_gazoline=self.quantite_gazoline(),qte_gallon_diesel=self.quantite_diesel())
                    self.valide_commande = True
                        
                    self.commandes.append(self.commande)
                   
                    print('Commande affectuer avec succes')
                else:
                    print('Mot de passe de incorrect')   

            else:
                print(' Pourcentage 50')
        else:
            print('Aucune station')
    

    
    @staticmethod
    def afficher_qte_disponible_and_qte_utilise(station: Station ,qteGazole_ut : float,qteDiese_ut:float):
        print(f"\n Quantité de gazoline utilisée est {int(qteGazole_ut)}"
              f"\n Quantité de diesel utilisée est {int(qteDiese_ut)}"
              f"\n Quantité de Gazoline disponible  {int(station.quantite_gazoline_disponible(qte_vendue = 0))}"
              f"\n Quantité de diesel disponible {int(station.quantite_diesel_disponible(qte_vendue = 0))}"
              )
    def afficher_commande(self):
        if len(self.commandes)>0:
          for lisC in self.commandes:
             print(lisC)
        else:
            print('liste vide')
    @staticmethod
    def valide_commande()-> True:
           return input ('Voulez-vous effectuer de commande : O pour oui N pour non valider la commande !!!') == 'o'
  
    def _status(self):
        if len(self.commandes)>0:
            self.commandes.eta

    def save_approvisionnenment(self,reverse = True):
        if len(self.stationGenerale) > 0:
            #Entrer le mot de passe pour confirmer l'approvisionnement 
            if Petrole.valide_commande():
                self.commandes.reverse()
                for stat in self.stationGenerale:
                    qtegazoline = int(stat.quantite_diesel_utilise())
                    qtediesel = int(stat.quantite_diesel_utilise())

                    self.approvisionnement = Approvisionnement(qte_gallon_gazoline=qte_gallon_gazoline)
                    
                    self.appro.add(self.approvisionnement)

                    print(f'Approvisionnement {self.station.nomStation} valider')
                else:
                    print(f'pas approvisionnenment pour {self.station.nomStation}')    
            else:
                print('Mot de passe incorrect ')
        else:
            print('Aucune Commande')        

    def afficher_appro(self):
        if len(self.appro) > 0:
            for app in self.appro:
                print(app)

          
# Vente
    def enregsitrer_vente(self):
        self.nomStation = Petrole.choixStation(message = ' Choisir une station svp !!!')
        if self.nomStation != '':
            ess = self.getessence()
            match self.nomStation.lower():
                case 'lalue':
                    self.effectuerVente(essence=ess)
                case 'tabarre':
                    self.effectuerVente(self,self.nomStation,ess)
                case 'clercine':
                    self.effectuerVente(self,self.nomStation,ess)
                case 'petion-ville':
                    self.effectuerVente(self,self.nomStation,ess)            
    


    def getessence(self):
        type_gaz = Petrole.choose_essence()
        match type_gaz.lower():
            case 'a':
                self.qte_gallon_gazoline = int(input('Entrer la quantite de gallon de Gazoline ====>'))
                return 'gazoline'
            case 'b':
                self.qte_gallon_diesel = int(input('Entrer la quantite de gallon de diesel ==>'))
                return 'diesel'
            case 'gazo_and_dies':
                 self.qte_gallon_gazoline = int(input('Entrer la quantite de gallon de Gazoline ==>'))
                 
                 self.qte_gallon_diesel = int(input('Entrer la quantite de gallon de diesel ==>'))
                 return 'gazo_and_dies'
    
    def effectuerVente(self,essence):
        if essence == 'gazoline':
             qteGazolineDispo = self.station.capacite_Gazoline
             if qteGazolineDispo >= self.qte_gallon_gazoline:
                 self.prix_vente = self.qte_gallon_gazoline * Station.prix_unitaire_gazoline
                 newqte = qteGazolineDispo - self.qte_gallon_gazoline
                 self.station.capacite_Gazoline(newqte)
                 self.ventes.append(self.vente)
                 print('Qte de gallon de Gazoline: {} prix: {}'.format(self.qte_gallon_gazoline,self.prix_vente))
             else:
                print('Quante de gallon de gazoline insuffisante pour effectuer la vente')
        elif essence == 'diesel':
             qteDieselDispo = self.station.capacite_Gazoline
             if qteDieselDispo >= self.capacite_diesel:
                 self.prix_vente = self.qte_gallon_diesel * Station.prix_unitaire_diesel
                 newqte = qteDieselDispo - self.qte_gallon_diesel
                 self.station.capacite_diesel(newqte)
                 self.ventes.append(self.ventes)
                 print('Qte de gallon de Gazoline: {} prix: {}'.format(self.qte_gallon_diesel,self.prix_vente))
             else:
                print('Quante de gallon de gazoline insuffisante pour effectuer la vente')    

        elif essence == 'gazo_and_dies':
            if qteGazolineDispo >= self.station.capacite_Gazoline and qteDieselDispo >= self.station.capacite_diesel:


                #CALCUL DE LA VENTE
                prix_vente_gazoline = self.capacite_Gazoline * Station.prix_unitaire_gazoline
                prix_vente_diesel = self.capacite_diesel * Station.prix_unitaire_diesel
                self.prix_vente = prix_vente_gazoline * prix_vente_diesel

                #Affectation de la nouvelle capacite
                newqtegazo = qteGazolineDispo - self.qte_gallon_gazoline
                newqtediese = qteDieselDispo - self.qte_gallon_diesel

                self.station.capacite_Gazoline(newqtegazo)
                self.station.capacite_diesel(newqtediese)

                print('Qte de gallon de Gazoline: {} prix: {}'.format(self.qte_gallon_gazoline,self.prix_vente))
                print('Qte de gallon de Gazoline: {} prix: {}'.format(self.qte_gallon_diesel,self.prix_vente))
        else:
            print('Mauvais choix')

    def afficher_vente(self):
        if len(self.ventes) > 0:
            for ven in self.ventes:
                print(ven)
        else:
            print('Aucun vente ')        
if __name__ == '__main__':    

    Petrole = Petrole()
    Petrole.enregistrerStation()
    Petrole.afficherStations()

