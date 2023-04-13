class Firma:
    
    def __init__(self, firmenname):
        self._firmenname = firmenname
        self._abteilungen = []
    
    def add_abteilung(self, abteilung):
        self._abteilungen.append(abteilung)
    
    def remove_abteilung(self, abteilung):
        if abteilung in self._abteilungen:
            self._abteilungen.remove(abteilung)
    
    #Select Methods
    def count_abteilungen(self):
        return len(self._abteilungen)
    
    def count_mitarbeiter(self):
        count = 0
        for a in self._abteilungen:
            count += len(a._mitarbeiter)
        return count

    def count_gruppenleiter(self):
        count = 0
        for a in self._abteilungen:
            count += len(a._gruppenleiter)
        return count
    
    def get_biggest_abteilungung(self):
        #Würde leichter gehen - wollte MAP testen
        ma_pro_abteilung = list(map(lambda a : len(a._mitarbeiter), self._abteilungen))
        idx = ma_pro_abteilung.index(max(ma_pro_abteilung))
        return self._abteilungen[idx]._abteilungsname
        
    def get_percentage_genders(self):
        countFemale = 0
        for a in self._abteilungen:
            female_ma = list(filter(lambda m: m._geschlecht is 'w', a._mitarbeiter))
            countFemale += len(female_ma)
        percFemale = (countFemale / self.count_mitarbeiter()) * 100
        return round(percFemale, 2), round(100 - percFemale, 2)
        
    def __str__(self):
        return self._firmenname + ' ' + self._abteilungen


class Abteilung():

    def __init__(self, abteilungsname, abteilungsleiter):
        self._abteilungsname = abteilungsname
        self._mitarbeiter = []
        self._gruppenleiter = []
        self._abteilungsleiter = abteilungsleiter
        #Abteilungsleiter ist auch ein MA im U
        self._mitarbeiter.append(self._abteilungsleiter)
        
    def add_mitarbeiter(self, mitarbeiter):
        self._mitarbeiter.append(mitarbeiter)
    
    def remove_mitarbeiter(self, mitarbeiter):
        if mitarbeiter in self._mitarbeiter:
            self._mitarbeiter.remove(mitarbeiter)
            
    def add_gruppenleiter(self, gleiter):
        self._gruppenleiter.append(gleiter)
        #Gruppenleiter ist auch ein MA im U
        self._mitarbeiter.append(gleiter)
    
    def remove_gruppenleiter(self, gleiter):
        if gleiter in self._gruppenleiter:
            self._gruppenleiter.remove(gleiter)
        
    def __str__(self):
        return self._abteilungsname + ' ' + self._abteilungsleiter + ' ' + self._mitarbeiter + ' ' + self._gruppenleiter
    
    
class Person():
    
    def __init__(self, geschlecht, name):
        self._geschlecht = geschlecht
        self._name = name
        
    def __str__(self):
        return self._geschlecht + ' ' + self.name
    
    
class Mitarbeiter(Person):
        
    def __init__(self, geschlecht, name, firma):
        super().__init__(geschlecht, name)
        self._firma = firma
    
    def __str__(self):
        super().__str__() + ' ' + self._firma
        

class Abteilungsleiter(Mitarbeiter):
    
    def __init__(self, geschlecht, name, firma):
        super().__init__(geschlecht, name, firma)
    
    def __str__(self):
        super().__str__() + ' Abteilungsleiter'
        
        
class Gruppenleiter(Mitarbeiter):
    
    def __init__(self, geschlecht, name, firma):
        super().__init__(geschlecht, name, firma)
    
    def __str__(self):
        super().__str__() + ' Gruppenleiter'
        
#Main
def main():
    
    #Objekte instanziieren
    firma = Firma('TIWAG')
    
    a1 = Abteilung('Personalmanagement', Abteilungsleiter('m', 'Andi', firma))
    a2 = Abteilung('IT', Abteilungsleiter('w', 'Laura', firma))
    
    firma.add_abteilung(a1)
    firma.add_abteilung(a2)
    
    a1.add_gruppenleiter(Gruppenleiter('m', 'Jan', firma))
    a1.add_gruppenleiter(Gruppenleiter('m', 'Daniel', firma))
    a2.add_gruppenleiter(Gruppenleiter('w', 'Celina', firma))
    
    a1.add_mitarbeiter(Mitarbeiter('m', 'Leo', firma))
    a1.add_mitarbeiter(Mitarbeiter('m', 'Simon', firma))
    a1.add_mitarbeiter(Mitarbeiter('m', 'Johnny', firma))
    a1.add_mitarbeiter(Mitarbeiter('w', 'Katrin', firma))
    
    a2.add_mitarbeiter(Mitarbeiter('m', 'Jakob', firma))
    a2.add_mitarbeiter(Mitarbeiter('w', 'Emma', firma))
    a2.add_mitarbeiter(Mitarbeiter('w', 'Gutrun', firma))
    
    #Abfragen
    print(f'Abteilungen: {firma.count_abteilungen()}')
    print(f'Mitarbeiter: {firma.count_mitarbeiter()}')
    print(f'davon {firma.count_gruppenleiter()} Gruppenleiter')
    print(f'Größte Abteilung: {firma.get_biggest_abteilungung()}')
    percW, percM = firma.get_percentage_genders()
    print(f'Anteile: Frauen {percW} % | Männers {percM} %')
    
if __name__ == '__main__':
    main()