from exception.errors import RepoError
from domeniu.entitati import Produs
class RepoFileProdus:
    
    def __init__(self,filename,read_produs,write_produs):
        self.__entitati = []
        self.__filename = filename
        self.__read_produs = read_produs
        self.__write_produs = write_produs
    
    
    def __read_all_from_file(self):
        """
        citeste din fisier produsele, le transforma in obiecte Produs si le adauga in lista cu toate produsele
        """
        self.__entitati = []
        with open(self.__filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_produs(line)
                    self.__entitati.append(obj)
    
    
    def __write_all_to_file(self):
        """
        scrie in fisier toate obiectele Produs din lista dupa ce le transforma in string-uri, cu virgula intre elemente
        """
        with open(self.__filename,"w") as f:
            for obj in self.__entitati:
                line = self.__write_produs(obj)
                f.write(line+"\n")
    
    
    def adauga(self,produs):
        """
        adauga un obiect Produs in lista de produse si rescrie fisierul cu produse
        input:
            produs - obiect de tip Produs cu toate caracteristicile sale
        """
        self.__read_all_from_file()
        
        if produs in self.__entitati:
            raise RepoError("Id existent!\n")
        self.__entitati.append(produs)
        
        self.__write_all_to_file()
    
    
    def stergere(self,id_prod):
        """
        sterge un obiect Produs din lista de produse si rescrie fisierul cu produse
        input:
            id_prod - id-ul produsului care trebuie sters
        """
        self.__read_all_from_file()
        
        prod_sterg = Produs(id_prod,None,None)
        if prod_sterg in self.__entitati:
            self.__entitati.remove(prod_sterg)
        
        self.__write_all_to_file()
    
    
    def set_all(self,produse):
        """
        se inlocuieste lista veche de produse cu o lista noua de produse si se rescrie fisierul cu produse
        input:
            produse - lista cu obiecte de tip Produs
        """
        self.__entitati = produse
        self.__write_all_to_file()
    

    def get_all(self):
        """
        returneaza o copie a listei cu produse
        """
        self.__read_all_from_file()
        return self.__entitati[:]