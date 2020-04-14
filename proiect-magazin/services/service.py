from domeniu.entitati import Produs
class ServiceProdus:
    
    def __init__(self,repoProdus,validProdus):
        self.__history = []
        self.__repoProdus = repoProdus
        self.__validProdus = validProdus


    def adaugare_prod(self,id_prod,denumire,pret):
        """
        valideaza componentele obiectului din clasa Produs si conduce spre adaugarea sa in modulul Repo
        input:
            id_prod - id, numar intreg
            denumire - numele produsului, string
            pret - pretul produsului, float
        """
        produs = Produs(id_prod,denumire,pret)
        self.__validProdus.valideaza_produsul(produs)
        
        self.__repoProdus.adauga(produs)
       
       
    def cifra_in_id(self,id_prod,cifra):
        """
        verifica daca o anumita cifra se afla in id
        input:
            id_prod - id, numar intreg
            cifra - cifra cautata in id
        output: 
            True sau False
        returneaza True daca cifra este in id si False in caz contrar
        """
        while id_prod != 0:
            if id_prod % 10 == cifra:
                return True
            id_prod = id_prod // 10
        return False
       
        
    def sterge_cifra(self,cifra):
        """
        conduce in repo pentru stergerea produsului a carui id contine cifra
        input: 
            cifra - cifra cautata in id
        output: 
            contorul - cate produse au fost sterse
        returneaza contorul si lista fara produsele a caror id contine cifra 
        """
        self.__history.append(self.toate_produsele())
        contor = 0
        produse = self.__repoProdus.get_all()
        for produs in produse:
            if self.cifra_in_id(produs.getId(), cifra):
                self.__repoProdus.stergere(produs.getId())
                contor += 1
        return contor
    
    
    def filtreaza(self,denumire,pret):
        """
        filtreaza/elimina din lista de produse acele produse care contin textul si/sau au pretul respectiv
        input:
            denumire - numele produsului, string
            pret - pretul produsului, float
        output:
            produse sau filtrate - ambele sunt liste de obiecte Produs
        returneaza lista de produse filtrata
        """
        produse = self.__repoProdus.get_all()
        filtrate = []
        if denumire != "" or pret != -1:
            for produs in produse:
                if not( (denumire in produs.getDenumire() or denumire == "") and (produs.getPret() == pret or pret == -1) ):
                    filtrate.append(produs)
        else:
            return produse
        return filtrate
    
    
    def undo(self):
        """
        foloseste lista  de liste de obiecte Produs history pentru a inlocui lista actuala cu elemente sterse cu lista dinainte de stergere
        """
        if len(self.__history) == 0:
            raise ValueError("Nu se poate efectua undo!\n")
        
        produse = self.__history[-1]
        for produs in produse:
            self.__validProdus.valideaza_produsul(produs)
        
        self.__repoProdus.set_all(produse)
        self.__history.remove(self.__history[-1])
    
        
    def toate_produsele(self):
        """
        returneaza lista cu toate produsele
        output:
            lista cu elementele preluata din modulul Repo
        """
        return self.__repoProdus.get_all()