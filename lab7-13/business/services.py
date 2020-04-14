from domeniu.modele import client,film,inchiriere
import string
import random
from random import randint

class ServiceInchiriere:
    
    
    def __init__(self, repoInchirieri, validInchiriere, repoFilme, repoClienti):
        self.__repoInchirieri = repoInchirieri
        self.__validInchiriere = validInchiriere
        self.__repoFilme = repoFilme
        self.__repoClienti = repoClienti
    
    def add_inchiriere(self,idClient,idFilm,stare):
        self.__repoClienti.cauta(idClient)       
        self.__repoFilme.cauta(idFilm)
        
        inchirierea = inchiriere(idClient,idFilm,stare)
        self.__validInchiriere.valideaza_inchiriere(inchirierea)
        self.__repoInchirieri.adauga(inchirierea)
    
    def update_inchiriere(self,idClient,idFilm):
        self.__repoInchirieri.cauta(idClient,idFilm)
        
        inchirierea = inchiriere(idClient,idFilm,1)
        self.__validInchiriere.valideaza_inchiriere(inchirierea)
        self.__repoInchirieri.actualizeaza(inchirierea)
    
    def cauta_inchirieri(self,cheie):
        idClient = int(cheie[0])
        idFilm = int(cheie[1])
        return self.__repoInchirieri.cauta(idClient,idFilm)
    
    
    
    """def sortare_descr_numar(self,subLista): 
        for i in range(0, len(subLista)): 
            for j in range(0, len(subLista)-i-1): 
                if (subLista[j][1] < subLista[j + 1][1]): 
                    aux = subLista[j] 
                    subLista[j]= subLista[j + 1] 
                    subLista[j + 1]= aux 
        return subLista"""
    
    # SELECTION SORT
    """def sortare_descr_numar(self,subLista): 
        for i in range(0,len(subLista)-1):
            ind = i
            #gasirea celui mai mare element din lista
            for j in range(i+1,len(subLista)):
                if (subLista[j][1]>subLista[ind][1]):
                    ind = j
            if (i<ind):
                #interschimbarea
                aux = subLista[i]
                subLista[i] = subLista[ind]
                subLista[ind] = aux
        return subLista[:]"""
    
    # RECURSIVITATEA SORTARII PRIN SELECTIE
    def maxIndex(self,subLista,i,j):
        if i == j:
            return i
            
        k = self.maxIndex(subLista,i+1,j)
        return (i if subLista[i][1] > subLista[k][1] else k)
          
    def sortare_descr_numar(self,subLista,n=0,index=0):
        n = len(subLista)
        if index == n:
            return subLista
              
        k = self.maxIndex(subLista,index,n-1)
          
        if k != index:
            subLista[k], subLista[index] = subLista[index], subLista[k]

        self.sortare_descr_numar(subLista,n,index+1)
        return subLista
    
    
    """def sortare_cresc_numar(self,subLista): 
        for i in range(0, len(subLista)): 
            for j in range(0, len(subLista)-i-1): 
                if (subLista[j][1] > subLista[j + 1][1]): 
                    aux = subLista[j] 
                    subLista[j]= subLista[j + 1] 
                    subLista[j + 1]= aux 
        return subLista"""   
    
    def cmp_number(self,x,y):
            if x[1] < y[1]:
                return 1
            elif x[1] > y[1]:
                return -1
            return 0
    
    # SELECTION SORT
    def sortare_cresc_numar(self,subLista,cmp):
        for i in range(0,len(subLista)-1):
            ind = i
            #gasirea celui mai mic element din lista
            for j in range(i+1,len(subLista)):
                if cmp(subLista[ind],subLista[j])==-1:
                    ind = j
            if (i<ind):
                #interschimbarea
                aux = subLista[i]
                subLista[i] = subLista[ind]
                subLista[ind] = aux
        return subLista[:]
    
    """def sortare_cresc_alfabet(self,subLista): 
        for i in range(0, len(subLista)): 
            for j in range(0, len(subLista)-i-1): 
                if (subLista[j][0] > subLista[j + 1][0]): 
                    aux = subLista[j] 
                    subLista[j]= subLista[j + 1] 
                    subLista[j + 1]= aux 
        return subLista"""
    
    
    # SHAKE SORT
    """
    Each iteration of the algorithm is broken up into 2 stages:

        1) The first stage loops through the array from left to right, just like the Bubble Sort. During the loop, adjacent items 
        are compared and if value on the left is greater than the value on the right, then values are swapped. At the end of first
        iteration, largest number will reside at the end of the array.
        
        2) The second stage loops through the array in opposite direction- starting from the item just before the most recently 
        sorted item, and moving back to the start of the array. Here also, adjacent items are compared and are swapped if required.
            
    """
    
    def key_word(self,x):
        return x[0]
    
    def sortare_cresc_alfabet(self,subLista,key): 
        n = len(subLista) 
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True): 
      
            # reset the swapped flag on entering the loop, 
            # because it might be true from a previous 
            # iteration. 
            swapped = False
      
            # loop from left to right same as the bubble 
            # sort 
            for i in range (start, end): 
                if key(subLista[i]) > key(subLista[i+1]): 
                    subLista[i], subLista[i+1]= subLista[i+1], subLista[i] 
                    swapped = True
      
            # if nothing moved, then array is sorted. 
            if (swapped == False): 
                break
      
            # otherwise, reset the swapped flag so that it 
            # can be used in the next stage 
            swapped = False
      
            # move the end point back by one, because 
            # item at the end is in its rightful spot 
            end = end - 1
      
            # from right to left, doing the same 
            # comparison as in the previous stage 
            for i in range(end-1, start-1, -1): 
                if key(subLista[i]) > key(subLista[i+1]): 
                    subLista[i], subLista[i + 1] = subLista[i + 1], subLista[i] 
                    swapped = True
      
            # increase the starting point, because 
            # the last stage would have moved the next 
            # smallest number to its rightful spot. 
            start = start + 1
        return subLista 
    
    
    def get_client_totalFilme(self):
        inchirieri = self.__repoInchirieri.get_all()
        client_Filme = {}
        
        clienti = self.__repoClienti.get_all()
        for client in clienti:
            if not client.getId() in client_Filme:
                client_Filme[client.getId()] = []
        
        for inchiriere in inchirieri:
            client_Filme[inchiriere.getClientId()].append(inchiriere.getFilmId())
        
        listaClientFilme = []
        for elem in client_Filme.items():
            idClient = elem[0]
            nume_client = self.__repoClienti.cauta(idClient).getNume()
            numar = len(elem[1])
            clientul = [nume_client,numar]
            listaClientFilme.append(clientul)
        
        return listaClientFilme[:]
    
    
    def get_film_totalInchirieri(self):
        inchirieri = self.__repoInchirieri.get_all()
        filme_Inchirieri = {}
        
        filme = self.__repoFilme.get_all()
        for film in filme:
            if not film.getId() in filme_Inchirieri:
                filme_Inchirieri[film.getId()] = []
        
        for inchiriere in inchirieri:
            filme_Inchirieri[inchiriere.getFilmId()].append(inchiriere.getClientId())
        
        listaFilmInchirieri = []
        for elem in filme_Inchirieri.items():
            idFilm = elem[0]
            nume_film = self.__repoFilme.cauta(idFilm).getTitlu()
            numar = len(elem[1])
            filmul = [nume_film,numar]
            listaFilmInchirieri.append(filmul)
        
        return listaFilmInchirieri[:]
    
    
    def get_gen_totalInchirieri(self):
        inchirieri = self.__repoInchirieri.get_all()
        filme_Inchirieri = {}
        
        filme = self.__repoFilme.get_all()
        for film in filme:
            if not film.getId() in filme_Inchirieri:
                filme_Inchirieri[film.getId()] = []
        
        for inchiriere in inchirieri:
            filme_Inchirieri[inchiriere.getFilmId()].append(inchiriere.getClientId())
        
        listaFilmInchirieri = []
        for elem in filme_Inchirieri.items():
            idFilm = elem[0]
            gen_film = self.__repoFilme.cauta(idFilm).getGen()
            numar = len(elem[1])
            filmul = [gen_film,numar]
            listaFilmInchirieri.append(filmul)
            
        i = 0
        j = 0
        while i != len(listaFilmInchirieri)-1:
            j = i + 1
            while j != len(listaFilmInchirieri):
                if listaFilmInchirieri[i][0] == listaFilmInchirieri[j][0]:
                    listaFilmInchirieri[i][1] += listaFilmInchirieri[j][1]
                    listaFilmInchirieri.remove(listaFilmInchirieri[j])
                else:
                    j += 1
            i += 1
                
        
        return listaFilmInchirieri[:]
    
    
    def get_inchirieri(self):
        return self.__repoInchirieri.get_all()
    
    def sterge_dupa_clienti(self,cheie):
        self.__repoInchirieri.stergere_dupa_client(cheie)
        
    def sterge_dupa_filme(self,cheie):
        self.__repoInchirieri.stergere_dupa_film(cheie)



class ServiceFilme:
    
    
    def __init__(self, repoFilme, validFilm):
        self.__repoFilme = repoFilme
        self.__validFilm = validFilm
    
    def add_film(self,idFilm,titlu,descriere,gen):
        filmul = film(idFilm,titlu,descriere,gen)
        self.__validFilm.valideaza_film(filmul)
        self.__repoFilme.adauga(filmul)

    def get_filme(self):
        return self.__repoFilme.get_all()
    
    def cauta_filme(self,cheie):
        return self.__repoFilme.cauta(cheie)
    
    def sterge_filme(self,cheie):
        self.__repoFilme.stergere(cheie)
        
    def update_film(self,idFilm,titlu,descriere,gen):
        filmul = film(idFilm,titlu,descriere,gen)
        self.__validFilm.valideaza_film(filmul)
        self.__repoFilme.actualizeaza(filmul)
        
    
    """def genereaza_filme(self,numar):
        genuri = ["science-fiction","action","adventure","horror","animated","nature","reality-show"]
        while numar != 0:
            idFilm = randint(0,999999)
            titlu = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
            descriere = ''.join(random.choice(string.ascii_uppercase) for _ in range(14))
            gen = genuri[randint(0,6)]
            self.add_film(idFilm,titlu,descriere,gen)
            numar -= 1"""
    
    # RECURSIVITATE
    def genereaza_filme(self,numar):
        genuri = ["science-fiction","action","adventure","horror","animated","nature","reality-show"]
        
        idFilm = randint(0,999999)
        titlu = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        descriere = ''.join(random.choice(string.ascii_uppercase) for _ in range(14))
        gen = genuri[randint(0,6)]
        self.add_film(idFilm,titlu,descriere,gen)
        
        if numar-1 != 0:
            numar -= 1
            return self.genereaza_filme(numar)



class ServiceClienti:
    
    
    def __init__(self, repoClienti, validClient):
        self.__repoClienti = repoClienti
        self.__validClient = validClient
    
    
    def add_client(self,idClient,nume,cnp):
        clientul = client(idClient,nume,cnp)
        self.__validClient.valideaza_client(clientul)
        self.__repoClienti.adauga(clientul)

    def get_clienti(self):
        return self.__repoClienti.get_all()
    
    def cauta_clienti(self,cheie):
        return self.__repoClienti.cauta(cheie)
    
    def size(self):
        return self.__repoClienti.size()
    
    
    def sterge_clienti(self,cheie):
        self.__repoClienti.stergere(cheie)
        
        
    def update_client(self,idClient,nume,cnp):
        clientul = client(idClient,nume,cnp)
        self.__validClient.valideaza_client(clientul)
        self.__repoClienti.actualizeaza(clientul)
        
        
    def genereaza_clienti(self,numar):
        while numar != 0:
            idClient = randint(0,99999)
            nume = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
            cnp = ''.join(random.choice(string.digits) for _ in range(12))
            self.add_client(idClient,nume,cnp)
            numar -= 1