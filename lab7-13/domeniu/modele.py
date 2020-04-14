class film:
    def __init__(self,id,titlu,descriere,gen):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        
        
    def getId(self):
        return self.__id
    
    def getTitlu(self):
        return self.__titlu
    
    def getDescriere(self):
        return self.__descriere
    
    def getGen(self):
        return self.__gen
    
    
    def setId(self,valoare):
        self.__id = valoare
    
    def setTitlu(self,valoare):
        self.__titlu = valoare
    
    def setDescriere(self,valoare):
        self.__descriere = valoare
    
    def setGen(self,valoare):
        self.__gen = valoare
        
    
    @staticmethod
    def read_film(line):
        parts = line.split(",")
        return film(int(parts[0].strip()),parts[1].strip(),parts[2].strip(),parts[3].strip())
    
    @staticmethod
    def write_film(obj):
        return str(obj.getId())+","+obj.getTitlu()+","+obj.getDescriere()+","+obj.getGen()
        
     
        
        
class client:
    def __init__(self,id,nume,cnp):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp
        
    def getId(self):
        return self.__id
    
    def getNume(self):
        return self.__nume
    
    def getCNP(self):
        return self.__cnp
    
    
    def setId(self,valoare):
        self.__id = valoare
    
    def setNume(self,valoare):
        self.__nume = valoare
    
    def setCNP(self,valoare):
        self.__cnp = valoare
        
        
    @staticmethod
    def read_client(line):
        parts = line.split(",")
        return client(int(parts[0].strip()),parts[1].strip(),parts[2].strip())
    
    @staticmethod
    def write_client(obj):
        return str(obj.getId())+","+obj.getNume()+","+obj.getCNP()
    
    
        
        
class inchiriere:
    def __init__(self,clientid,filmid,stareRetur):
        self.__clientid = clientid
        self.__filmid = filmid
        self.__stareRetur = stareRetur
        
    def getClientId(self):
        return self.__clientid
    
    def getFilmId(self):
        return self.__filmid
    
    def getStareRetur(self):
        return self.__stareRetur
    
    
    def setClientId(self,valoare):
        self.__clientid = valoare
        
    def setFilmId(self,valoare):
        self.__filmid = valoare
        
    def setStareRetur(self,valoare):
        self.__stareRetur = valoare
    
    def __str__(self):
        return str(self.getClientId())+" "+str(self.getFilmId())+" "+str(self.getStareRetur())
        
    @staticmethod
    def read_inchiriere(line):
        parts = line.split(",")
        return inchiriere(int(parts[0].strip()),int(parts[1].strip()),int(parts[2].strip()))
    
    @staticmethod
    def write_inchiriere(obj):
        return str(obj.getClientId())+","+str(obj.getFilmId())+","+str(obj.getStareRetur())