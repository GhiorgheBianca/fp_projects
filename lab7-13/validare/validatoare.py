from errors.exceptions import ValidError

class ValidareClient:
    
    def __init__(self):
        pass

    
    def valideaza_client(self, client):
        errors = ""
        if client.getId() < 0:
            errors += "Id invalid!\n"
        if client.getNume() == "":
            errors += "Nume invalid!\n"
        if client.getCNP() == "" or len(client.getCNP()) != 12:
            errors += "CNP-ul trebuie sa aiba exact 12 numere!\n"
            
        try:
            int(client.getCNP())
        except ValueError:
            errors += "CNP-ul nu poate fi compus din litere!\n"
            
        if len(errors) > 0:
            raise ValidError(errors)



class ValidareFilm:
    
    def __init__(self):
        pass

    
    def valideaza_film(self, film):
        errors = ""
        if film.getId() < 0:
            errors += "Id invalid!\n"
        if film.getTitlu() == "":
            errors += "Titlu invalid!\n"
        if film.getDescriere() == "":
            errors += "Descriere invalida!\n"
        if film.getGen() == "":
            errors += "Gen invalid!\n"
        if len(errors) > 0:
            raise ValidError(errors)



class ValidareInchiriere:
    
    def __init__(self):
        pass

    
    def valideaza_inchiriere(self, inchiriere):
        errors = ""
        if inchiriere.getClientId() < 0:
            errors += "Id-ul clientului este invalid!\n"
        if inchiriere.getFilmId() < 0:
            errors += "Id-ul filmului este invalid!\n"
        if inchiriere.getStareRetur() > 1 or inchiriere.getStareRetur() < 0:
            errors += "Stare de returnare invalida!\n"
        if len(errors) > 0:
            raise ValidError(errors)


