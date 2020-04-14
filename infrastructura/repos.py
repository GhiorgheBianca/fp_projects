from errors.exceptions import RepoError
from domeniu.modele import client, inchiriere

class RepoFilm:
    def __init__(self):
        self._entitati = []

    
    def size(self):
        return len(self._entitati)

    
    def adauga(self,elem):
        for film in self._entitati:
            if elem.getId() == film.getId():
                raise RepoError("Id existent!\n")
        self._entitati.append(elem)

    
    def cauta(self,cheie):
        
        cond = 0
        for film in self._entitati:
            if cheie == film.getId() and cond == 0:
                cond = 1
        if cond == 0:
            raise RepoError("Id inexistent!\n")
         
        for x in self._entitati:
            if x.getId() == cheie:
                return x
            
            
    def stergere(self,cheie):
        film = self.cauta(cheie)
        self._entitati.remove(film)
            
            
    def actualizeaza(self,elem):
        self.cauta(elem.getId())
        for i in range(len(self._entitati)):
            if elem.getId() == self._entitati[i].getId():
                self._entitati[i] = elem

    
    def get_all(self):
        return self._entitati[:]




class RepoClient:
    
    def __init__(self):
        self._entitati = []
        

    
    def size(self):
        return len(self._entitati)

    
    
    def adauga(self,elem):
        for client in self._entitati:
            if elem.getId() == client.getId():
                raise RepoError("Id existent!\n")
        self._entitati.append(elem)

    
    
    def cauta(self,cheie):
        
        cond = 0
        for client in self._entitati:
            if cheie == client.getId() and cond == 0:
                cond = 1
        if cond == 0:
            raise RepoError("Id inexistent!\n")
         
        for x in self._entitati:
            if x.getId() == cheie:
                return x
            
    
    def stergere(self,cheie):
        client = self.cauta(cheie)
        self._entitati.remove(client)

    
    def actualizeaza(self,elem):
        client = self.cauta(elem.getId())
        for i in range(len(self._entitati)):
            if elem.getId() == self._entitati[i].getId():
                self._entitati[i] = elem
            
  
    def get_all(self):
        return self._entitati[:]




class RepoInchiriere:
    def __init__(self):
        self._entitati = []
        

    def size(self):
        return len(self._entitati)

    
    def adauga(self,elem):
        self._entitati.append(elem)

    
    def cauta(self,idClient,idFilm):
        cond = 0
        for inchiriere in self._entitati:
            if idFilm == inchiriere.getFilmId() and idClient == inchiriere.getClientId() and cond == 0:
                cond = 1
        if cond == 0:
            raise RepoError("Inchiriere inexistenta!\n")
        
        for inchirierea in self._entitati:
            if idFilm == inchirierea.getFilmId() and idClient == inchirierea.getClientId():
                return inchirierea
    
    
    def actualizeaza(self,elem):
        for i in range(len(self._entitati)):
            if elem.getFilmId() == self._entitati[i].getFilmId() and elem.getClientId() == self._entitati[i].getClientId():
                self._entitati[i] = elem
    
    
    def get_all(self):
        return self._entitati[:]
    
    def get_stare(self,idClient,IdFilm):
        inchirieri = self._entitati[:]
        for inchiriere in inchirieri:
            if inchiriere.getClientId() == idClient and inchiriere.getFilmId() == IdFilm and inchiriere.getStareRetur() == 1:
                return 1
            elif inchiriere.getClientId() == idClient and inchiriere.getFilmId() == IdFilm and inchiriere.getStareRetur() == 0:
                return 0

    def stergere_dupa_client(self,idClient):
        i = 0
        while i != len(self._entitati):
            if idClient == self._entitati[i].getClientId():
                elem = self._entitati[i]
                self._entitati.remove(elem)
            else:
                i += 1
    
    def stergere_dupa_film(self,idFilm):
        i = 0
        while i != len(self._entitati):
            if idFilm == self._entitati[i].getFilmId():
                elem = self._entitati[i]
                self._entitati.remove(elem)
            else:
                i += 1





class FileRepoClient(RepoClient):
    
    def __init__(self,filename,read_obj,write_obj):
        self.__filename = filename
        self.__read_obj = read_obj
        self.__write_obj = write_obj
        
    def __read_all_from_file(self):
        self._entitati = []
        with open(self.__filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_obj(line)
                    self._entitati.append(obj)
    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as f:
            for obj in self._entitati:
                line = self.__write_obj(obj)
                f.write(line+"\n")           
    
    
    def cauta(self, cheie):
        self.__read_all_from_file()
        return RepoClient.cauta(self,cheie)
    
    def actualizeaza(self, elem):
        self.__read_all_from_file()
        RepoClient.actualizeaza(self,elem)
        self.__write_all_to_file()
    
    def adauga(self, elem):
        self.__read_all_from_file()
        RepoClient.adauga(self,elem)
        self.__write_all_to_file()
    
    def stergere(self, elem):
        self.__read_all_from_file()
        RepoClient.stergere(self,elem)
        self.__write_all_to_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return RepoClient.get_all(self)
    
    
    
class FileRepoFilm(RepoFilm):
    
    def __init__(self,filename,read_obj,write_obj):
        self.__filename = filename
        self.__read_obj = read_obj
        self.__write_obj = write_obj
        
    def __read_all_from_file(self):
        self._entitati = []
        with open(self.__filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_obj(line)
                    self._entitati.append(obj)
    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as f:
            for obj in self._entitati:
                line = self.__write_obj(obj)
                f.write(line+"\n")           
    
    
    def cauta(self, cheie):
        self.__read_all_from_file()
        return RepoFilm.cauta(self,cheie)
    
    def actualizeaza(self, elem):
        self.__read_all_from_file()
        RepoFilm.actualizeaza(self,elem)
        self.__write_all_to_file()
    
    def adauga(self, elem):
        self.__read_all_from_file()
        RepoFilm.adauga(self,elem)
        self.__write_all_to_file()
    
    def stergere(self, elem):
        self.__read_all_from_file()
        RepoFilm.stergere(self,elem)
        self.__write_all_to_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return RepoFilm.get_all(self)
    
    
    
class FileRepoInchiriere(RepoInchiriere):
    
    def __init__(self,filename,read_obj,write_obj):
        self.__filename = filename
        self.__read_obj = read_obj
        self.__write_obj = write_obj
        
    def __read_all_from_file(self):
        self._entitati = []
        with open(self.__filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_obj(line)
                    self._entitati.append(obj)
    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as f:
            for obj in self._entitati:
                line = self.__write_obj(obj)
                f.write(line+"\n")           
    
    
    def cauta(self,idClient,idFilm):
        self.__read_all_from_file()
        RepoInchiriere.cauta(self,idClient,idFilm)
    
    def actualizeaza(self, elem):
        self.__read_all_from_file()
        RepoInchiriere.actualizeaza(self,elem)
        self.__write_all_to_file()
    
    def adauga(self, elem):
        self.__read_all_from_file()
        RepoInchiriere.adauga(self,elem)
        self.__write_all_to_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return RepoInchiriere.get_all(self)
    
    def get_stare(self,idClient,IdFilm):
        self.__read_all_from_file()
        return RepoInchiriere.get_stare(self,idClient,IdFilm)

    def stergere_dupa_client(self,idClient):
        self.__read_all_from_file()
        RepoInchiriere.stergere_dupa_client(self,idClient)
        self.__write_all_to_file()
    
    def stergere_dupa_film(self,idFilm):
        self.__read_all_from_file()
        RepoInchiriere.stergere_dupa_film(self,idFilm)
        self.__write_all_to_file()