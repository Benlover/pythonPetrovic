
from controller.ControllerService import Petrole


def menu()->str:
    print('************ GESTION MAX LONDON PETROVIC ************')
    print('1-Station')
    print('2-Commande')
    print('3-approvisionnement')
    print('4-vente')
    print('Presser <<q>> pour quitter')
    print('*******************************************************')
    return str (input('votre choix : '))


if __name__ == '__main__':

    choix: str = ''
    Petrole = Petrole()

    while True:
        choix = menu()
        match choix:
          case '1': 
              while True:
                 print('*********************Station***********')
                 autrechoix: str = input('\n a-Enregistrer une stations'
                                        '\n b-Afficher la liste des station'
                                        '\n c-modifier quantité gallon de gazoline et/ou de Diesel d’une station'
                                        '\n d-quitter'
                                        '\n **************************************************'
                                        '\n ==>')
                 match autrechoix:  
                     case 'a':
                        Petrole.enregistrerStation()
                     case 'b':
                         Petrole.afficherStation()
                     case 'c':
                         Petrole.ModifierCapacite()
                     case 'd':
                         break    
                     case default:
                         print('Mauvais Choix!!!!!')                                 
            
          case '2':
              while True:
                print('*************** COMMANDE ****************')
                autrechoix: str = input('\n a-Enregistrer une Commande'
                                        '\n b-Afficher la liste des Commandes'
                                        '\n c-quitter'
                                        '\n **************************************************'
                                        '\n ==>')
                match autrechoix:
                     case 'a':
                         Petrole.save_commande()
                     case 'b':
                         Petrole.afficher_commande()
                     case 'c':
                         break
                     case default:
                         print('Mauvais Choix')         


          case '3':
              while True:
                print('***************** APPR0VISIONNEMENT *********************')
                autrechoix : str = input('\n a- enregistrer approvisionnement'
                                       '\n b- Afficher les approvisionnement'
                                       '\n c- Quitter '
                                       '\n ****************************'
                                       '\n ===>')
                match autrechoix:
                    case 'a':
                        Petrole.save_approvisionnenment()
                    case 'b':
                        Petrole.afficher_appro()
                    case 'c':
                        break
                    case other:
                        print('Mauvais Choix')

          case '4':
              while True:
                print('********************** VENTE ****************')
                autrechoix :str = input('\n a- Enregistrer une vente'
                                        '\n b- Afficher les ventes'
                                        '\n c- quitter'
                                        '\n *********************'
                                        '\n ====>')
                match autrechoix:
                    case 'a':
                        Petrole.enregsitrer_vente()
                    case 'b':
                        pass
                    case 'c':
                        break                        
          case 'q':
              break
          case default:
              print('mauvais choix')
