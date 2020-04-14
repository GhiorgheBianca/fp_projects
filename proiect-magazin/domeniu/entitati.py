class Produs:
    
    def __init__(self,id,denumire,pret):
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret
        
    def setId(self,valoare):
        self.__id = valoare
        
    def setDenumire(self,valoare):
        self.__denumire = valoare
        
    def setPret(self,valoare):
        self.__pret = valoare
        
        
    def getId(self):
        return self.__id
    
    def getDenumire(self):
        return self.__denumire
    
    def getPret(self):
        return self.__pret
    
    
    def __str__(self):
        return str(self.__id)+" "+self.__denumire+" "+str(self.__pret)
    
    
    def __eq__(self,other):
        return other.__id == self.__id
    
    
    @staticmethod
    def read_produs(line):
        parts = line.split(",")
        return Produs(int(parts[0]),parts[1],float(parts[2]))
    
    @staticmethod
    def write_produs(obj):
        return str(obj.getId())+","+obj.getDenumire()+","+str(obj.getPret())


