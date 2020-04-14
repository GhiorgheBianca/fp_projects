from errors.exceptions import ValidError,RepoError
import math
from domeniu.modele import client

class Consola:
    
    
    # AFISARI
    
    def __ui_afiseaza_filme(self,valori):
        filme = self.__serviceFilme.get_filme()
        for film in filme:
            print(str(film.getId()) + " " + film.getTitlu() + " " + film.getDescriere() + " " + film.getGen())
            
            
    def __ui_afiseaza_clienti(self,valori):
        clienti = self.__serviceClienti.get_clienti()
        for client in clienti:
            print(str(client.getId()) + " " + client.getNume() + " " + client.getCNP())
            
            
    def __ui_afiseaza_inchirieri(self,valori):
        inchirieri = self.__serviceInchirieri.get_inchirieri()
        for inchiriere in inchirieri:
            print(str(inchiriere.getClientId()) + " " + str(inchiriere.getFilmId()) + " " + str(inchiriere.getStareRetur()))
    
    
    
    # CAUTARI
    
    def __ui_cauta_clienti(self,valori):
        cheie = int(valori[0])
        client = self.__serviceClienti.cauta_clienti(cheie)
        print(str(client.getId()) + " " + client.getNume() + " " + client.getCNP())
        
    
    def __ui_cauta_filme(self,valori):
        cheie = int(valori[0])
        film = self.__serviceFilme.cauta_filme(cheie)
        print(str(film.getId()) + " " + film.getTitlu() + " " + film.getDescriere() + " " + film.getGen())
    
    
    
    # ADAUGARI
    
    def __ui_add_film(self,valori):
        if len(valori) < 4:
            raise ValueError("Pentru a adauga un film, sunt necesare exact 4 valori!")
        
        descriere = ""
        for nr in range(2,len(valori)-2):
            descriere = descriere + valori[nr] + " "
        if len(valori) - 3 > 1:
            descriere = descriere + valori[nr+1]
        else:
            descriere = valori[2]
        
        idFilm = int(valori[0])
        titlu = valori[1]
        gen = valori[len(valori)-1]
        self.__serviceFilme.add_film(idFilm,titlu,descriere,gen)
        
        
    def __ui_add_client(self,valori):
        if len(valori) != 3:
            raise ValueError("Pentru a adauga un client, sunt necesare exact 3 valori!")
        idClient = int(valori[0])
        nume = valori[1]
        cnp = valori[2]
        self.__serviceClienti.add_client(idClient,nume,cnp)
        
        
    def __ui_add_inchiriere(self,valori):
        if len(valori) != 2:
            raise ValueError("Pentru a adauga o inchiriere, sunt necesare exact 2 valori!")
        idClient = int(valori[0])
        idFilm = int(valori[1])
        stareRetur = 0
        self.__serviceInchirieri.add_inchiriere(idClient,idFilm,stareRetur)
    
    
    
    # GENERARI
    
    def __ui_genereaza_clienti(self,valori):
        if len(valori) != 1:
            raise ValueError("Pentru a genera un numar de clienti, este necesara exact 1 valoare!")
        numar = int(valori[0])
        self.__serviceClienti.genereaza_clienti(numar)
    
    
    def __ui_genereaza_filme(self,valori):
        if len(valori) != 1:
            raise ValueError("Pentru a genera un numar de filme, este necesara exact 1 valore!")
        numar = int(valori[0])
        self.__serviceFilme.genereaza_filme(numar)
    
    
    
    # ACTUALIZARI
    
    def __ui_update_client(self,valori):
        if len(valori) != 3:
            raise ValueError("Pentru a actualiza un client, sunt necesare exact 3 valori!")
        idClient = int(valori[0])
        nume = valori[1]
        cnp = valori[2]
        self.__serviceClienti.update_client(idClient,nume,cnp)
    
    
    def __ui_update_film(self,valori):
        if len(valori) < 4:
            raise ValueError("Pentru a actualiza un film, sunt necesare exact 4 valori!")
        
        descriere = ""
        for nr in range(2,len(valori)-2):
            descriere = descriere + valori[nr] + " "
        if len(valori) - 3 > 1:
            descriere = descriere + valori[nr+1]
        else:
            descriere = valori[2]
        
        idFilm = int(valori[0])
        titlu = valori[1]
        gen = valori[len(valori)-1]
        self.__serviceFilme.update_film(idFilm,titlu,descriere,gen)
    
    
    def __ui_update_inchiriere(self,valori):
        if len(valori) != 2:
            raise ValueError("Pentru a adauga o inchiriere, sunt necesare exact 2 valori!")
        idClient = int(valori[0])
        idFilm = int(valori[1])
        self.__serviceInchirieri.update_inchiriere(idClient,idFilm)
    
    
    
    # STERGERI
    
    def __ui_sterge_client(self,valori):
        idClient = int(valori[0])
        self.__serviceClienti.sterge_clienti(idClient)
        self.__serviceInchirieri.sterge_dupa_clienti(idClient)
    
    
    def __ui_sterge_film(self,valori):
        idFilm = int(valori[0])
        self.__serviceFilme.sterge_filme(idFilm)
        self.__serviceInchirieri.sterge_dupa_filme(idFilm)
    
    
    
    # DATE INITIALE

    def introdu_valori_initiale(self,valori):
        self.__serviceClienti.add_client(1,"Ionica","128913046712")
        self.__serviceClienti.add_client(2,"DanAndreas","124890349210")
        self.__serviceClienti.add_client(3,"PetruPavel","239012783901")
        self.__serviceClienti.add_client(4,"Andrei","785313046712")
        self.__serviceClienti.add_client(5,"Gigel","785000046712")
        self.__serviceClienti.add_client(6,"PetricaPitic","965010046712")
        self.__serviceClienti.add_client(7,"Costel","146313046712")
        
        self.__serviceFilme.add_film(10,"morometii","invatati pentru bac. Foarte bine","drama")
        self.__serviceFilme.add_film(20,"thehorse","si marea cea albastra","adventure")
        self.__serviceFilme.add_film(30,"studentia","the movie","thriller")
        self.__serviceFilme.add_film(40,"python","not the snake but the code","drama")
        
        self.__serviceInchirieri.add_inchiriere(1,20,0)
        self.__serviceInchirieri.add_inchiriere(1,30,1)
        self.__serviceInchirieri.add_inchiriere(2,30,1)
        self.__serviceInchirieri.add_inchiriere(2,10,1)
        self.__serviceInchirieri.add_inchiriere(2,30,0)
        self.__serviceInchirieri.add_inchiriere(3,30,0)
        self.__serviceInchirieri.add_inchiriere(3,20,1)
    
    
    
    # RAPOARTE
    
    def __ui_clienti_dupa_nume(self,valoare):
        lista = self.__serviceInchirieri.get_client_totalFilme()
        lista = self.__serviceInchirieri.sortare_cresc_alfabet(lista)
        for sub_lista in lista:
            print(sub_lista[0],"a inchiriat",sub_lista[1],"film/e")
    
    def __ui_clienti_dupa_inchirieri(self,valoare):
        lista = self.__serviceInchirieri.get_client_totalFilme()
        lista = self.__serviceInchirieri.sortare_descr_numar(lista)
        for sub_lista in lista:
            print(sub_lista[0],"a inchiriat",sub_lista[1],"film/e")
    
    def __ui_filme_dupa_inchirieri(self,valoare):
        lista = self.__serviceInchirieri.get_film_totalInchirieri()
        lista = self.__serviceInchirieri.sortare_descr_numar(lista)
        for sub_lista in lista:
            print("Filmul","'"+sub_lista[0]+"'","a fost inchiriat de",sub_lista[1],"ori")
    
    def __ui_top30_clienti(self,valoare):
        total_clienti = self.__serviceClienti.size()
        clienti_30perc = math.floor((30/100)*total_clienti)
        lista = self.__serviceInchirieri.get_client_totalFilme()
        lista = self.__serviceInchirieri.sortare_descr_numar(lista)
        for i in range(0,clienti_30perc):
            print(lista[i][0],"a inchiriat",lista[i][1],"film/e")
    
    def __ui_statistica_genuri(self,valoare):
        lista = self.__serviceInchirieri.get_gen_totalInchirieri()
        lista = self.__serviceInchirieri.sortare_cresc_numar(lista)
        for sub_lista in lista:
            print("Genul","'"+sub_lista[0]+"'","a avut",sub_lista[1],"film/e inchiriate")
    
    
    # INITIALIZARE CLASA

    def __init__(self, serviceFilme, serviceClienti, serviceInchirieri):
        self.__serviceFilme = serviceFilme
        self.__serviceClienti = serviceClienti
        self.__serviceInchirieri = serviceInchirieri
        self.__comenzi = {
            "adauga_film":self.__ui_add_film,
            "afiseaza_filme":self.__ui_afiseaza_filme,
            "cauta_filme":self.__ui_cauta_filme,
            "adauga_client":self.__ui_add_client,
            "afiseaza_clienti":self.__ui_afiseaza_clienti,
            "cauta_clienti":self.__ui_cauta_clienti,
            "adauga_inchiriere":self.__ui_add_inchiriere,
            "afiseaza_inchirieri":self.__ui_afiseaza_inchirieri,
            "genereaza_clienti":self.__ui_genereaza_clienti,
            "genereaza_filme":self.__ui_genereaza_filme,
            "actualizeaza_client":self.__ui_update_client,
            "actualizeaza_film":self.__ui_update_film,
            "sterge_client":self.__ui_sterge_client,
            "sterge_film":self.__ui_sterge_film,
            "returneaza_film":self.__ui_update_inchiriere,
            "initial":self.introdu_valori_initiale,
            "clienti_dupa_nume":self.__ui_clienti_dupa_nume,
            "clienti_dupa_inchirieri":self.__ui_clienti_dupa_inchirieri,
            "filme_dupa_inchirieri":self.__ui_filme_dupa_inchirieri,
            "top30_clienti":self.__ui_top30_clienti,
            "genuri_dupa_inchirieri":self.__ui_statistica_genuri
            }
        
        
        
    # PORNIRE
        
    def porneste(self):
        while True:
            comanda = input("Comanda: ")
            if comanda == "exit":
                return None
            comanda = comanda.strip()
            segmCmd = comanda.split()
            instructiune = segmCmd[0]
            valori = segmCmd[1:]
            if instructiune in self.__comenzi:
                try:
                    self.__comenzi[instructiune](valori)
                except ValueError as gresitUi:
                    print("UI Error:\n"+str(gresitUi))
                except ValidError as gresitValid:
                    print("Validare Error:\n"+str(gresitValid))
                except RepoError as gresitRepo:
                    print("Repo Error:\n"+str(gresitRepo))
            else:
                print("Comanda invalida!\n")
