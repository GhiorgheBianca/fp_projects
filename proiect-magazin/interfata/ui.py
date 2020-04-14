from exception.errors import ValidError, RepoError
class Consola:
    
    def __ui_adauga_produs(self,params):
        if len(params) != 3:
            raise ValueError("Trebuie sa avem exact 3 parametrii!\n")
        
        prod_id = int(params[0])
        denumire = params[1]
        pret = float(params[2])
        
        self.__serviceProdus.adaugare_prod(prod_id,denumire,pret)
    
    
    def __ui_printeaza_produsele(self,params):
        produse = self.__serviceProdus.toate_produsele()
        for produs in produse:
            print(produs)
    
    
    def __ui_sterge_cifra(self,params):
        if len(params) != 1:
            raise ValueError("Trebuie sa avem exact un parametru (o cifra)!\n")
        if int(params[0]) < 0 or int(params[0]) > 9:
            raise ValueError("Trebuie sa scrieti exact o cifra!\n")
        
        number = int(params[0])
        contor = self.__serviceProdus.sterge_cifra(number)
        print("Numarul de produse sterse: " + str(contor))
    
    
    def __ui_filtru(self,params):
        if len(params) == 2:
            denumire = params[0]
            pret = float(params[1])
        elif len(params) == 1:
            pret = float(params[0])
            denumire = ""
        else:
            raise ValueError("Nu ati introdus corect parametrii!\n")    
        
        self.__filtru_curent = [denumire,pret]
        print("Filtru curent: " + denumire + " " + str(pret))
        produse = self.__serviceProdus.filtreaza(denumire,pret)
        for produs in produse:
            print(produs)
    
    
    def __ui_undo(self,params):
        self.__serviceProdus.undo()
    
    
    def __init__(self,serviceProdus):
        self.__filtru_curent = ["",-1]
        self.__serviceProdus = serviceProdus
        self.__comenzi = {
            "add_prod":self.__ui_adauga_produs,
            "print_prod":self.__ui_printeaza_produsele,
            "sterg_cifra":self.__ui_sterge_cifra,
            "filtru":self.__ui_filtru,
            "undo":self.__ui_undo
            }
    
    def porneste(self):
        self.__ui_filtru(self.__filtru_curent)
        while True:
            print("\n\n")
            print("add_prod")
            print("print_prod")
            print("sterg_cifra")
            print("filtru")
            print("\n")
            self.__ui_filtru(self.__filtru_curent)
            print("\n\n")
            comenzi = input("Comanda: ")
            comenzi = comenzi.strip()
            comenzi = comenzi.split()
            comanda = comenzi[0]
            params = comenzi[1:]
        
            if comanda in self.__comenzi:
                try:
                    self.__comenzi[comanda](params)
                except ValueError as value_err:
                    print(str(value_err))
                except ValidError as valid_err:
                    print(str(valid_err))
                except RepoError as repo_err:
                    print(str(repo_err))
            else:
                print("Comanda invalida!")