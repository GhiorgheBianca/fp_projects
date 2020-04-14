'''
Created on 29 ian. 2020

@author: asus
'''
from tests.teste import Teste
from validare.validatoare import ValidatorProdus
from services.service import ServiceProdus
from repository.repos import RepoFileProdus
from interfata.ui import Consola
from domeniu.entitati import Produs

def startApp():
    testele = Teste()
    testele.run_tests()
    
    Validator_Produs = ValidatorProdus()
    RepoFile_Produs = RepoFileProdus("produse.txt",Produs.read_produs,Produs.write_produs)
    Service_Produs = ServiceProdus(RepoFile_Produs,Validator_Produs)
    
    ui = Consola(Service_Produs)
    ui.porneste()
    
startApp()