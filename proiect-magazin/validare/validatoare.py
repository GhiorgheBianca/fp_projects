from exception.errors import ValidError

class ValidatorProdus:
    
    def __init__(self):
        pass
    
    def valideaza_produsul(self,produs):
        errors = ""
        
        if produs.getId() < 0:
            errors += "Id invalid!\n"
        if produs.getDenumire() == "":
            errors += "Denumire invalida!\n"
        if produs.getPret() < 0:
            errors += "Pret invalid!\n"
            
        if len(errors) > 0:
            raise ValidError(errors)


