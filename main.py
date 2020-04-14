from teste.teste import Teste
from validare.validatoare import ValidareFilm,ValidareClient,ValidareInchiriere
#from infrastructura.repos import RepoFilm,RepoClient,RepoInchiriere 
from infrastructura.repos import FileRepoClient,FileRepoFilm,FileRepoInchiriere
from business.services import ServiceFilme,ServiceClienti,ServiceInchiriere
from prezentare.ui import Consola
from domeniu.modele import client, film, inchiriere


def start():
    
    teste = Teste()
    teste.all_tests()
    validFilm = ValidareFilm()
    validClient = ValidareClient()
    validInchiriere = ValidareInchiriere()
    
    #repoFilme = RepoFilm()
    repoFilme = FileRepoFilm("filme.txt",film.read_film,film.write_film)
    #repoClienti = RepoClient()
    repoClienti = FileRepoClient("clienti.txt",client.read_client,client.write_client)
    #repoInchiriere = RepoInchiriere()
    repoInchiriere = FileRepoInchiriere("inchirieri.txt",inchiriere.read_inchiriere,inchiriere.write_inchiriere)
    
    serviceFilme = ServiceFilme(repoFilme,validFilm)
    serviceClienti = ServiceClienti(repoClienti,validClient)
    serviceInchirieri = ServiceInchiriere(repoInchiriere,validInchiriere,repoFilme,repoClienti)
    ui = Consola(serviceFilme,serviceClienti,serviceInchirieri)
    ui.porneste()
    
start()