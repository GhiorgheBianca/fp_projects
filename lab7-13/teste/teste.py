from domeniu.modele import film,client,inchiriere
from validare.validatoare import ValidareFilm,ValidareClient,ValidareInchiriere
from errors.exceptions import ValidError, RepoError
from infrastructura.repos import RepoFilm,RepoClient,RepoInchiriere,FileRepoClient,FileRepoFilm,FileRepoInchiriere
from business.services import ServiceInchiriere, ServiceFilme, ServiceClienti
import unittest


class Teste(unittest.TestCase):
    
# TESTAREA CREARII DIN CLASE
    
    def __test_creeaza_film(self):
        idFilm = 10
        titlu = "caucazienii"
        descriere = "despre multi catei frumosi!"
        gen = "nature"
        filmul = film(idFilm,titlu,descriere,gen)
        self.assertEqual(filmul.getTitlu(),"caucazienii")
        self.assertEqual(filmul.getDescriere(),"despre multi catei frumosi!")
        self.assertEqual(filmul.getGen(),"nature")
        self.assertTrue(filmul.getId() == 10)
        filmul.setTitlu("catelusii")
        self.assertEqual(filmul.getTitlu(),"catelusii")
        self.__film = filmul
        
        
    def __test_creeaza_client(self):
        idClient = 19
        nume = "DanutIon"
        cnp = "124890349210"
        clientul = client(idClient,nume,cnp)
        self.assertEqual(clientul.getNume(),"DanutIon")
        self.assertEqual(clientul.getCNP(),"124890349210")
        self.assertTrue(clientul.getId() == 19)
        clientul.setNume("DanAndreas")
        self.assertEqual(clientul.getNume(),"DanAndreas")
        self.__client = clientul
        
        
    def __test_creeaza_inchiriere(self):
        idClient = 21
        idFilm = 12
        stareRetur = 0
        inchirierea = inchiriere(idClient,idFilm,stareRetur)
        self.assertTrue(inchirierea.getFilmId() == 12)
        self.assertTrue(inchirierea.getClientId() == 21)
        self.assertTrue(inchirierea.getStareRetur() == 0)
        inchirierea.setFilmId(14)
        self.assertTrue(inchirierea.getFilmId() == 14)
        self.__inchiriere = inchirierea
        
        
        
    # TESTAREA VALIDARILOR

    def __test_valideaza_client(self):
        validClienti = ValidareClient()
        validClienti.valideaza_client(self.__client)
        self.__client_id_rau = client(-31,"Ionica","128913046712")
        self.__client_nume_rau = client(31,"","125783902135")
        self.__client_cnp_rau = client(32,"Georgel","")
        self.__client_rau = client(-31,"","")
        
        with self.assertRaises(ValidError) as eroare:
            validClienti.valideaza_client(self.__client_id_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validClienti.valideaza_client(self.__client_nume_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Nume invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validClienti.valideaza_client(self.__client_cnp_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"CNP-ul trebuie sa aiba exact 12 numere!\nCNP-ul nu poate fi compus din litere!\n")
            
        with self.assertRaises(ValidError) as eroare:
            validClienti.valideaza_client(self.__client_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id invalid!\nNume invalid!\nCNP-ul trebuie sa aiba exact 12 numere!\nCNP-ul nu poate fi compus din litere!\n")
        self.__validareClienti = validClienti
        
        
    def __test_valideaza_film(self):
        validFilme = ValidareFilm()
        validFilme.valideaza_film(self.__film)
        self.__film_id_rau = film(-18,"morometii","de retinut pentru bac","traditional")
        self.__film_titlu_rau = film(18,"","de retinut pentru bac","traditional")
        self.__film_descriere_rea = film(18,"morometii","","traditional")
        self.__film_gen_rau = film(18,"morometii","de retinut pentru bac","")
        self.__film_rau = film(-18,"","","")
        
        with self.assertRaises(ValidError) as eroare:
            validFilme.valideaza_film(self.__film_id_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validFilme.valideaza_film(self.__film_titlu_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Titlu invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validFilme.valideaza_film(self.__film_descriere_rea)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Descriere invalida!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validFilme.valideaza_film(self.__film_gen_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Gen invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validFilme.valideaza_film(self.__film_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id invalid!\nTitlu invalid!\nDescriere invalida!\nGen invalid!\n")
        self.__validareFilme = validFilme


    def __test_valideaza_inchiriere(self):
        validInchirieri = ValidareInchiriere()
        validInchirieri.valideaza_inchiriere(self.__inchiriere)
        self.__inchiriere_idFilm_rau = inchiriere(9,-3,1)
        self.__inchiriere_idClient_rau = inchiriere(-9,3,1)
        self.__inchiriere_status_rau = inchiriere(9,3,2)
        self.__inchiriere_rea = inchiriere(-9,-3,-1)
        
        with self.assertRaises(ValidError) as eroare:
            validInchirieri.valideaza_inchiriere(self.__inchiriere_idFilm_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id-ul filmului este invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validInchirieri.valideaza_inchiriere(self.__inchiriere_idClient_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id-ul clientului este invalid!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validInchirieri.valideaza_inchiriere(self.__inchiriere_status_rau)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Stare de returnare invalida!\n")
        
        with self.assertRaises(ValidError) as eroare:
            validInchirieri.valideaza_inchiriere(self.__inchiriere_rea)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id-ul clientului este invalid!\nId-ul filmului este invalid!\nStare de returnare invalida!\n")
        self.__validareInchirieri = validInchirieri

    
    
    # TESTAREA LUNGIMII
    
    def __test_Client_size(self):
        self.__repoClient = RepoClient()
        self.assertEqual(self.__repoClient.size(),0)
        self.__repoClient.adauga(self.__client)
        self.assertEqual(self.__repoClient.size(),1)
        
        
    def __test_Film_size(self):
        self.__repoFilm = RepoFilm()
        self.assertEqual(self.__repoFilm.size(),0)
        self.__repoFilm.adauga(self.__film)
        self.assertEqual(self.__repoFilm.size(),1)
        
        
    def __test_Inchiriere_size(self):
        self.__repoInchiriere = RepoInchiriere()
        self.assertEqual(self.__repoInchiriere.size(),0)
        self.__repoInchiriere.adauga(self.__inchiriere)
        self.assertEqual(self.__repoInchiriere.size(),1)
        
    
    
    # TESTAREA CAUTARII
    
    def __test_Client_cauta(self):
        self.__repoClient = RepoClient()
        self.__client_inexistent = client(24,"nicolas","123464267345")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.cauta(self.__client_inexistent)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
    
    
    def __test_Film_cauta(self):
        self.__repoFilm = RepoFilm()
        self.__film_inexistent = film(12,"thefilmul","descriereee","action")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.cauta(self.__film_inexistent)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
    
    
    
    # TESTAREA ADAUGARILOR
    
    def __test_adaugare_Client(self):
        self.__repoClient = RepoClient()
        self.assertEqual(self.__repoClient.size(),0)
        self.__client = client(23,"andrei","123567345987")
        self.__repoClient.adauga(self.__client)
        self.assertEqual(self.__repoClient.size(),1)
        cheie_client = self.__client.getId()
        client_gasit = self.__repoClient.cauta(cheie_client)
        self.assertEqual(client_gasit.getNume(),self.__client.getNume())
        self.assertEqual(client_gasit.getCNP(),self.__client.getCNP())
        self.__alt_client_acelasi_id = client(23,None,None)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.adauga(self.__alt_client_acelasi_id)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id existent!\n")
            
        self.__alt_client = client(12,"catalin","123678397098")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.cauta(self.__alt_client)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
            
        clienti = self.__repoClient.get_all()
        self.assertEqual(clienti,[self.__client])
    
    
    def __test_adaugare_Film(self):
        self.__repoFilm = RepoFilm()
        self.assertEqual(self.__repoFilm.size(),0)
        self.__film = film(10,"morometii","o descriere frumoasa","documentar")
        self.__repoFilm.adauga(self.__film)
        self.assertEqual(self.__repoFilm.size(),1)
        cheie_film = self.__film.getId()
        film_gasit = self.__repoFilm.cauta(cheie_film)
        self.assertEqual(film_gasit.getTitlu(),self.__film.getTitlu()) 
        self.assertEqual(film_gasit.getDescriere(),self.__film.getDescriere()) 
        self.assertEqual(film_gasit.getGen(),self.__film.getGen())
        self.__alt_film_acelasi_id = film(10,None,None,None)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.adauga(self.__alt_film_acelasi_id)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id existent!\n")
            
        self.__alt_film = film(9,"dacii","frumos este scris","adventure")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.cauta(self.__alt_film)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
            
        filme = self.__repoFilm.get_all()
        self.assertEqual(filme,[self.__film])
    
    
    def __test_adaugare_Inchiriere(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"morometii","o descriere frumoasa","documentar"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei","123567345987"))
        
        repoInchiriere = RepoInchiriere()
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        self.__repoInchiriere = RepoInchiriere()
        self.assertEqual(self.__repoInchiriere.size(),0)
        self.__serviceInchirieri.add_inchiriere(5, 3, 0)
        self.__inchiriere = inchiriere(5,3,0)
        self.__repoInchiriere.adauga(self.__inchiriere)
        self.assertEqual(self.__repoInchiriere.size(),1)
        
        with self.assertRaises(RepoError) as eroare:
            self.__serviceInchirieri.add_inchiriere(3,5,0)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
            
        inchirierile = self.__repoInchiriere.get_all()
        self.assertEqual(inchirierile,[self.__inchiriere])
       
       
       
    # TESTAREA STERGERILOR
    
    def __test_stergere_Client(self):
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(19,"andrei","123123123123"))
        self.__repoClient.adauga(client(20,"mihai","109847345987"))
        self.__repoClient.adauga(client(21,"tudor","123567410487"))
        self.__repoClient.adauga(client(22,"petricel","123567000087"))
        self.assertEqual(self.__repoClient.size(),4)
        self.__repoClient.stergere(22)
        self.assertEqual(self.__repoClient.size(),3)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.cauta(22)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
            
        self.__repoClient.stergere(19)
        self.assertEqual(self.__repoClient.size(),2)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.cauta(19)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.stergere(1)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
    
    
    def __test_stergere_Film(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(2,"sequel","descrierea prima","horror"))
        self.__repoFilm.adauga(film(3,"prequel","descrierea a doua","action"))
        self.__repoFilm.adauga(film(4,"thehorse","descrierea a treia","adventure"))
        self.__repoFilm.adauga(film(5,"minunatulpython","finish!!!","fight"))
        self.assertEqual(self.__repoFilm.size(),4)
        self.__repoFilm.stergere(4)
        self.assertEqual(self.__repoFilm.size(),3)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.cauta(4)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
            
        self.__repoFilm.stergere(2)
        self.assertEqual(self.__repoFilm.size(),2)
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.cauta(2)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.stergere(50)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
    
    
    def __test_stergere_inchirieri_dupa_client(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"titlu1","descr 1","gen1"))
        self.__repoFilm.adauga(film(4,"titlu2","descr 2","gen2"))
        self.__repoFilm.adauga(film(5,"titlu3","descr 3","gen3"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei1","123567345998"))
        self.__repoClient.adauga(client(6,"andrei2","123567345999"))
        self.__repoClient.adauga(client(7,"andrei3","123567345900"))
        
        self.__repoInchiriere = RepoInchiriere()
        self.__inchiriere = inchiriere(5,3,0)
        self.__repoInchiriere.adauga(self.__inchiriere)
        self.__repoInchiriere.adauga(inchiriere(6,5,1))
        self.__repoInchiriere.adauga(inchiriere(6,4,0))
        self.assertEqual(self.__repoInchiriere.size(),3)
        
        
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        self.__serviceInchirieri.sterge_dupa_clienti(6)
        
        self.assertEqual(self.__repoInchiriere.size(),1)
        inchirierile = self.__repoInchiriere.get_all()
        self.assertEqual(inchirierile,[self.__inchiriere])
        
        
    def __test_stergere_inchirieri_dupa_film(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"titlu1","descr 1","gen1"))
        self.__repoFilm.adauga(film(4,"titlu2","descr 2","gen2"))
        self.__repoFilm.adauga(film(5,"titlu3","descr 3","gen3"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei1","123567345998"))
        self.__repoClient.adauga(client(6,"andrei2","123567345999"))
        self.__repoClient.adauga(client(7,"andrei3","123567345900"))
        
        self.__repoInchiriere = RepoInchiriere()
        self.__inchiriere = inchiriere(5,3,0)
        self.__repoInchiriere.adauga(self.__inchiriere)
        self.__repoInchiriere.adauga(inchiriere(6,5,1))
        self.__repoInchiriere.adauga(inchiriere(7,5,0))
        self.assertEqual(self.__repoInchiriere.size(),3)
        
        
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        self.__serviceInchirieri.sterge_dupa_filme(5)
        
        self.assertEqual(self.__repoInchiriere.size(),1)
        inchirierile = self.__repoInchiriere.get_all()
        self.assertEqual(inchirierile,[self.__inchiriere])
    
    
    
    # TESTAREA MODIFICARILOR
    
    def __test_actualizare_Client(self):
        self.__repoClient = RepoClient()
        self.__client = client(23,"andrei","123567345987")
        self.__repoClient.adauga(self.__client)
        self.__repoClient.actualizeaza(client(23,"andreicata","122122122122"))
        cheie_client = self.__client.getId()
        client_gasit = self.__repoClient.cauta(cheie_client)
        self.assertEqual(client_gasit.getNume(),"andreicata")
        self.assertEqual(client_gasit.getCNP(),"122122122122")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoClient.actualizeaza(client(55,"catalin","122134322122"))
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
        
        self.__serviceClienti = ServiceClienti(self.__repoClient,self.__validareClienti)
        with self.assertRaises(ValidError) as eroare:
            self.__serviceClienti.update_client(23, "", "122134322122111")
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Nume invalid!\nCNP-ul trebuie sa aiba exact 12 numere!\n")
    
    
    def __test_actualizare_Film(self):
        self.__repoFilm = RepoFilm()
        self.__film = film(10,"morometii","o descriere frumoasa","documentar")
        self.__repoFilm.adauga(self.__film)
        self.__repoFilm.actualizeaza(film(10,"morometiiVoinici","o descriere super-mega frumoasa","documentarIstoric"))
        cheie_film = self.__film.getId()
        film_gasit = self.__repoFilm.cauta(cheie_film)
        self.assertEqual(film_gasit.getTitlu(),"morometiiVoinici") 
        self.assertEqual(film_gasit.getDescriere(),"o descriere super-mega frumoasa")
        self.assertEqual(film_gasit.getGen(),"documentarIstoric")
        
        with self.assertRaises(RepoError) as eroare:
            self.__repoFilm.actualizeaza(film(101,"morometiiVoinici","o descriere super-mega frumoasa","documentarIstoric"))
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Id inexistent!\n")
        
        self.__serviceFilme = ServiceFilme(self.__repoFilm,self.__validareFilme)
        with self.assertRaises(ValidError) as eroare:
            self.__serviceFilme.update_film(10,"","","")
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Titlu invalid!\nDescriere invalida!\nGen invalid!\n")
    
    
    def __test_actualizare_Inchiriere(self):
        self.__repoInchiriere = RepoInchiriere()
        self.__repoInchiriere.adauga(inchiriere(5,10,0))
        self.__repoInchiriere.adauga(inchiriere(3,6,0))
        self.__repoInchiriere.actualizeaza(inchiriere(3,6,1))
        self.assertEqual(self.__repoInchiriere.get_stare(3, 6),1)
        self.__repoInchiriere.actualizeaza(inchiriere(5,10,1))
        self.assertEqual(self.__repoInchiriere.get_stare(5, 10),1)
        
        self.__serviceInchiriere = ServiceInchiriere(self.__repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        with self.assertRaises(RepoError) as eroare:
            self.__serviceInchiriere.update_inchiriere(200,56)
        eroarea = str(eroare.exception)
        self.assertEqual(eroarea,"Inchiriere inexistenta!\n")
    
    
    
    # TESTAREA SORTARILOR
    
    def __test_sortare_descresc_numar(self):
        lista = [["dorel",5],["nicolae",1],["alex",7],["george",0],["mihai",1]]
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista_sortata = self.__serviceInchirieri.sortare_descr_numar(lista)
        self.assertEqual(lista_sortata,[["alex",7],["dorel",5],["mihai",1],["nicolae",1],["george",0]])
    
    def __test_sortare_cresc_alfabet(self):
        lista = [["dorel",5],["mihai",1],["alex",7],["george",0],["adrian",2],["nicolae",1]]
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista_sortata = self.__serviceInchirieri.sortare_cresc_alfabet(lista,self.__serviceInchiriere.key_word)
        self.assertEqual(lista_sortata,[["adrian",2],["alex",7],["dorel",5],["george",0],["mihai",1],["nicolae",1]])
        
    
    def __test_sortare_cresc_numar(self):
        lista = [["dorel",5],["mihai",1],["alex",7],["george",0],["adrian",2],["nicolae",1]]
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista_sortata = self.__serviceInchirieri.sortare_cresc_numar(lista,self.__serviceInchiriere.cmp_number)
        self.assertEqual(lista_sortata,[["george",0],["mihai",1],["nicolae",1],["adrian",2],["dorel",5],["alex",7]])
    
    
    
    # TESTAREA CREARII LISTELOR CLIENTI-TOTAL INCHIRIERI SI FILME-TOTAL INCHIRIERI
    
    def __test_get_client_totalFilme(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"titlu1","descr 1","gen1"))
        self.__repoFilm.adauga(film(4,"titlu2","descr 2","gen2"))
        self.__repoFilm.adauga(film(5,"titlu3","descr 3","gen3"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei1","123567345998"))
        self.__repoClient.adauga(client(6,"andrei2","123567345999"))
        self.__repoClient.adauga(client(7,"andrei3","123567345900"))
        
        self.__repoInchiriere = RepoInchiriere()
        self.__repoInchiriere.adauga(inchiriere(5,3,0))
        self.__repoInchiriere.adauga(inchiriere(6,5,1))
        self.__repoInchiriere.adauga(inchiriere(6,4,0))
        
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista = self.__serviceInchirieri.get_client_totalFilme()
        self.assertEqual(lista,[["andrei1",1],["andrei2",2],["andrei3",0]])
        
    
    def __test_get_film_totalInchirieri(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"titlu1","descr 1","gen1"))
        self.__repoFilm.adauga(film(4,"titlu2","descr 2","gen2"))
        self.__repoFilm.adauga(film(5,"titlu3","descr 3","gen3"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei1","123567345998"))
        self.__repoClient.adauga(client(6,"andrei2","123567345999"))
        self.__repoClient.adauga(client(7,"andrei3","123567345900"))
        
        self.__repoInchiriere = RepoInchiriere()
        self.__repoInchiriere.adauga(inchiriere(5,3,0))
        self.__repoInchiriere.adauga(inchiriere(6,5,1))
        self.__repoInchiriere.adauga(inchiriere(6,4,0))
        self.__repoInchiriere.adauga(inchiriere(7,4,0))
        self.__repoInchiriere.adauga(inchiriere(5,4,0))
        self.__repoInchiriere.adauga(inchiriere(6,5,0))
        
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista = self.__serviceInchirieri.get_film_totalInchirieri()
        self.assertEqual(lista,[["titlu1",1],["titlu2",3],["titlu3",2]])
    
    
    def __test_get_gen_totalInchirieri(self):
        self.__repoFilm = RepoFilm()
        self.__repoFilm.adauga(film(3,"titlu1","descr 1","gen1"))
        self.__repoFilm.adauga(film(4,"titlu2","descr 2","gen2"))
        self.__repoFilm.adauga(film(5,"titlu3","descr 3","gen3"))
        
        self.__repoClient = RepoClient()
        self.__repoClient.adauga(client(5,"andrei1","123567345998"))
        self.__repoClient.adauga(client(6,"andrei2","123567345999"))
        self.__repoClient.adauga(client(7,"andrei3","123567345900"))
        
        self.__repoInchiriere = RepoInchiriere()
        self.__repoInchiriere.adauga(inchiriere(5,3,0))
        self.__repoInchiriere.adauga(inchiriere(6,5,1))
        self.__repoInchiriere.adauga(inchiriere(6,4,0))
        self.__repoInchiriere.adauga(inchiriere(7,4,0))
        self.__repoInchiriere.adauga(inchiriere(5,4,0))
        self.__repoInchiriere.adauga(inchiriere(6,5,0))
        
        repoInchiriere = self.__repoInchiriere
        self.__serviceInchirieri = ServiceInchiriere(repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        lista = self.__serviceInchirieri.get_gen_totalInchirieri()
        self.assertEqual(lista,[["gen1",1],["gen2",3],["gen3",2]])
    
    
    # TESTAREA SCRIERII IN FISIER
    
    def __test_writeFileClienti(self):
        self.__repoClient = FileRepoClient("test_clienti.txt",client.read_client,client.write_client)
        self.__serviceFileClienti = ServiceClienti(self.__repoClient,self.__validareClienti)
        self.__serviceFileClienti.add_client(1,"Ionica","192350156283")
        self.__client = self.__repoClient.cauta(1)
        self.assertEqual(self.__repoClient.size(),2)
        self.assertEqual(self.__client.getId(),1) 
        self.assertEqual(self.__client.getNume(),"Ionica")
        self.assertEqual(self.__client.getCNP(),"192350156283")
        self.__serviceFileClienti.sterge_clienti(1)
        
        
    def __test_writeFileFilme(self):
        self.__repoFilm = FileRepoFilm("test_filme.txt",film.read_film,film.write_film)
        self.__serviceFileFilme = ServiceFilme(self.__repoFilm,self.__validareFilme)
        self.__serviceFileFilme.add_film(10,"morometii","este foarte frumos","action")
        self.assertEqual(self.__repoFilm.size(),2)
        film_gasit = self.__repoFilm.cauta(10)
        self.assertEqual(film_gasit.getTitlu(),"morometii") 
        self.assertEqual(film_gasit.getDescriere(),"este foarte frumos")
        self.assertEqual(film_gasit.getGen(),"action")
        self.__serviceFileFilme.sterge_filme(10)
        
    
    def __test_writeFileInchirieri(self):
        self.__repoClient = FileRepoClient("test_clienti.txt",client.read_client,client.write_client)
        self.__serviceFileClienti = ServiceClienti(self.__repoClient,self.__validareClienti)
        self.__serviceFileClienti.add_client(1,"Ionica","192350156283")
        
        self.__repoFilm = FileRepoFilm("test_filme.txt",film.read_film,film.write_film)
        self.__serviceFileFilme = ServiceFilme(self.__repoFilm,self.__validareFilme)
        self.__serviceFileFilme.add_film(10,"morometii","este foarte frumos","action")
        
        self.__repoInchiriere = FileRepoInchiriere("test_inchirieri.txt",inchiriere.read_inchiriere,inchiriere.write_inchiriere)
        self.__serviceFileInchirieri = ServiceInchiriere(self.__repoInchiriere,self.__validareInchirieri,self.__repoFilm,self.__repoClient)
        self.__serviceFileInchirieri.add_inchiriere(1,10,0)
        
        self.assertEqual(self.__repoInchiriere.size(),2)
        self.__serviceFileClienti.sterge_clienti(1)
        self.__serviceFileFilme.sterge_filme(10)
        self.__serviceFileInchirieri.sterge_dupa_clienti(1)
    
    
    
    # TESTAREA CITIRII DIN FISIER
    
    def __test_readFileClienti(self):
        self.assertEqual(self.__repoClient.size(),1)
        self.__client = self.__repoClient.cauta(2)
        self.assertEqual(self.__repoClient.size(),1)
        self.assertEqual(self.__client.getId(),2) 
        self.assertEqual(self.__client.getNume(),"Alex")
        self.assertEqual(self.__client.getCNP(),"111150156283")
        
    def __test_readFileFilme(self):
        self.assertEqual(self.__repoFilm.size(),1)
        film_gasit = self.__repoFilm.cauta(20)
        self.assertEqual(film_gasit.getTitlu(),"Aladin") 
        self.assertEqual(film_gasit.getDescriere(),"ff frumos")
        self.assertEqual(film_gasit.getGen(),"action")
        
        
    def __test_readFileInchirieri(self):
        self.assertEqual(self.__repoInchiriere.size(),1)
        self.__inchiriere = self.__repoInchiriere.cauta(2,20)
        self.assertEqual(self.__inchiriere.getClientId(),2) 
        self.assertEqual(self.__inchiriere.getFilmId(),20)
        self.assertEqual(self.__inchiriere.getStareRetur(),0)
        
    
    
    def all_tests(self):
        self.__test_creeaza_film()
        self.__test_creeaza_client()
        self.__test_creeaza_inchiriere()
        self.__test_valideaza_film()
        self.__test_valideaza_client()
        self.__test_valideaza_inchiriere()
        self.__test_Client_cauta()
        self.__test_Film_cauta()
        self.__test_Client_size()
        self.__test_Film_size()
        self.__test_Inchiriere_size()
        self.__test_adaugare_Client()
        self.__test_adaugare_Film()
        self.__test_adaugare_Inchiriere()
        self.__test_stergere_Client()
        self.__test_stergere_Film()
        self.__test_actualizare_Client()
        self.__test_actualizare_Film()
        self.__test_actualizare_Inchiriere()
        self.__test_sortare_descresc_numar()
        self.__test_sortare_cresc_alfabet()
        self.__test_sortare_cresc_numar()
        self.__test_get_client_totalFilme()
        self.__test_get_film_totalInchirieri()
        self.__test_get_gen_totalInchirieri()
        self.__test_stergere_inchirieri_dupa_client()
        self.__test_stergere_inchirieri_dupa_film()
        self.__test_writeFileClienti()
        self.__test_writeFileFilme()
        self.__test_writeFileInchirieri()
        self.__test_readFileClienti()
        self.__test_readFileFilme()