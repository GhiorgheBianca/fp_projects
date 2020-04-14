from validare.validatoare import ValidatorProdus
from domeniu.entitati import Produs
from exception.errors import ValidError
from services.service import ServiceProdus
from repository.repos import RepoFileProdus

class Teste:
    
    def __testeaza_validarea(self):
        produs_corect = Produs(1,"patrunjel",12.5)
        Validator = ValidatorProdus()
        Validator.valideaza_produsul(produs_corect)
        
        produs_id_gresit = Produs(-1,"patrunjel",1.35)
        try:
            Validator.valideaza_produsul(produs_id_gresit)
        except ValidError as valid_err:
            assert(str(valid_err) == "Id invalid!\n")
            
        produs_denumire_gresita = Produs(2,"",2.35)
        try:
            Validator.valideaza_produsul(produs_denumire_gresita)
        except ValidError as valid_err:
            assert(str(valid_err) == "Denumire invalida!\n")
            
        produs_pret_gresit = Produs(3,"patrunjel",-0.35)
        try:
            Validator.valideaza_produsul(produs_pret_gresit)
        except ValidError as valid_err:
            assert(str(valid_err) == "Pret invalid!\n")
            
        produs_gresit = Produs(-1,"",-2.35)
        try:
            Validator.valideaza_produsul(produs_gresit)
        except ValidError as valid_err:
            assert(str(valid_err) == "Id invalid!\nDenumire invalida!\nPret invalid!\n")
    
    
    def __testeaza_adaugarea(self):
        Valid = ValidatorProdus()
        Repo = RepoFileProdus("test_produse.txt",Produs.read_produs,Produs.write_produs)
        Service = ServiceProdus(Repo,Valid)
        
        produse = [Produs(1,"sunca",1.5)]
        Service.adaugare_prod(1,"sunca",1.5)
        produse_din_file = Service.toate_produsele()
        assert(produse == produse_din_file)
        
        produse.append(Produs(2,"cascaval",5.4))
        Service.adaugare_prod(2,"cascaval",5.4)
        produse_din_file = Service.toate_produsele()
        assert(produse == produse_din_file)
        
        Repo.stergere(1)
        Repo.stergere(2)
    
    
    def __testeaza_stergerea(self):
        Valid = ValidatorProdus()
        Repo = RepoFileProdus("test_produse.txt",Produs.read_produs,Produs.write_produs)
        Service = ServiceProdus(Repo,Valid)
        
        Service.adaugare_prod(1,"sunca",1.5)
        Service.adaugare_prod(3,"cascaval",5.4)
        Service.adaugare_prod(13,"produs",6.2)
        Service.adaugare_prod(12,"carne",10.2)
        Service.adaugare_prod(21,"ciocolata",4.9)
        
        contor = Service.sterge_cifra(3)
        produse = Service.toate_produsele()
        assert(contor == 2)
        assert(produse == [Produs(1,"sunca",1.5),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        
        contor = Service.sterge_cifra(1)
        produse = Service.toate_produsele()
        assert(contor == 3)
        assert(produse == [])
    
    
    def __testeaza_filtrul(self):
        Valid = ValidatorProdus()
        Repo = RepoFileProdus("test_produse.txt",Produs.read_produs,Produs.write_produs)
        Service = ServiceProdus(Repo,Valid)
        
        Service.adaugare_prod(1,"sunca",6.2)
        Service.adaugare_prod(3,"cascaval",5.4)
        Service.adaugare_prod(13,"produs",6.2)
        Service.adaugare_prod(12,"carne",10.2)
        Service.adaugare_prod(21,"ciocolata",4.9)
        
        assert(Service.filtreaza("",-1) == [Produs(1,"sunca",6.2),Produs(3,"cascaval",5.4),Produs(13,"produs",6.2),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        assert(Service.filtreaza("ca",-1) == [Produs(13,"produs",6.2),Produs(21,"ciocolata",4.9)])
        assert(Service.filtreaza("",6.2) == [Produs(3,"cascaval",5.4),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        assert(Service.filtreaza("ca",6.2) == [Produs(3,"cascaval",5.4),Produs(13,"produs",6.2),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        
        Repo.stergere(1)
        Repo.stergere(3)
        Repo.stergere(13)
        Repo.stergere(12)
        Repo.stergere(21)
    
    
    def __testeaza_undo(self):
        Valid = ValidatorProdus()
        Repo = RepoFileProdus("test_produse.txt",Produs.read_produs,Produs.write_produs)
        Service = ServiceProdus(Repo,Valid)
        
        Service.adaugare_prod(1,"sunca",6.2)
        Service.adaugare_prod(3,"cascaval",5.4)
        Service.adaugare_prod(13,"produs",6.2)
        Service.adaugare_prod(12,"carne",10.2)
        Service.adaugare_prod(21,"ciocolata",4.9)
        
        Service.sterge_cifra(3)
        Service.sterge_cifra(2)
        assert([Produs(1,"sunca",6.2)])
        Service.undo()
        assert([Produs(1,"sunca",6.2),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        Service.undo()
        assert([Produs(1,"sunca",6.2),Produs(3,"cascaval",5.4),Produs(13,"produs",6.2),Produs(12,"carne",10.2),Produs(21,"ciocolata",4.9)])
        
        Repo.stergere(1)
        Repo.stergere(3)
        Repo.stergere(13)
        Repo.stergere(12)
        Repo.stergere(21)
    
    
    def run_tests(self):
        self.__testeaza_validarea()
        self.__testeaza_adaugarea()
        self.__testeaza_stergerea()
        self.__testeaza_filtrul()
        self.__testeaza_undo()