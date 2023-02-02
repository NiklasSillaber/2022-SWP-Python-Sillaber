import random

class ListElement:
    def __init__(self,obj):
        self.obj = obj
        self.nextElem = None

    def setNextElem(self,next):
        self.nextElem = next

    def getNextElem(self):
        return self.nextElem
    
    def getObj(self):
        return self.obj

class VerketteteListe:

    head = ListElement(None)

    def getLast(self):
        curElem = self.head #Am Anfang Header als letztes Elem

        while curElem.getNextElem() != None: #Schauen so lange nächstes Elem None
            curElem = curElem.getNextElem()
        return curElem

    def isEmpty(self):
        return self.head.getObj() == None

    def __len__(self):
        length = 0
        curElem = self.head #beim Head starten

        while curElem != None:
            length += 1
            curElem = curElem.getNextElem() #nextElem beim ListElem default Null ==> keine OutOfBounds
        return length

    def getAllElements(self):
        elements = '['
        curElem = self.head #beim Head starten

        while curElem != None:
            elements += str(curElem.obj)+', '
            curElem = curElem.getNextElem()

        elements = elements[:-2] #letztes Komma löschen
        return elements + ']'

    def addElem(self, obj):
        newElem = ListElement(int(obj))

        if self.head.getObj() == None:  #Wenn kein Head vorhanden
            self.head = newElem
            return
        #Ansonsten Hinten dranhängen
        self.getLast().setNextElem(newElem)
    
    def deleteValue(self, delElem): #Alle Elemente die auf gleiche Instanz zeigen löschen
        curElem = self.head
        nextElem = curElem.getNextElem()

        if curElem.getObj() == int(delElem): #Soll head gelöscht werden?
            self.head = nextElem

        while nextElem != None:

            if nextElem.getObj() == delElem:

                if nextElem.getNextElem() != None:

                    while nextElem.getNextElem().getObj() == delElem:
                        nextElem = nextElem.getNextElem()

                    curElem.setNextElem(nextElem.getNextElem())
                else:
                    curElem.setNextElem(None)

            if curElem.getNextElem() == None: #Abbruchbedingung
                return

            nextElem = curElem.getNextElem()

    def contains(self, value): #Schaun ob bestimmtes Item in der Liste ist
        curElem = self.head

        while curElem != None: 
            if curElem.getObj() == int(value):
                return True

            curElem = curElem.getNextElem()
        return False

    def indexOf(self, value):
        curElem = self.head
        idx = 0

        while curElem.getObj() != int(value):

            if curElem.getNextElem() != None:
                curElem = curElem.getNextElem()
                idx += 1
            else:
                return -1

        return idx
    
    def getItemAtIndex(self, idx):
        idx = int(idx)
        curElem = self.head

        if idx > len(self) - 1:
            raise Exception("Index out of Bounds")

        for i in range(idx): #geht nur bis idx -1
            curElem = curElem.getNextElem()

        return curElem.getObj()

    def addAtIndex(self, idx, value): 
        addElem = ListElement(int(value))
        curElem = self.head
        help = 0
        idx = int(idx) - 1

        if idx > len(self):
            raise Exception("Index out of Bounds")

        while help != idx:
            curElem = curElem.getNextElem()
            help +=1
        
        curElem.nextElem, addElem.nextElem = addElem, curElem.nextElem

    def getFirstElem(self):
        return self.head.getObj()

    def getLastElem(self):
        curElem = self.head #Am Anfang Header als letztes Elem

        while curElem.getNextElem() != None: #Schauen so lange nächstes Elem None
            curElem = curElem.getNextElem()
        return curElem.getObj()

def main():
    myList = VerketteteListe()

    length = int(input("Länge: "))

    for i in range(length):
        myList.addElem(random.randint(0,10))

    print(myList.getAllElements())
    print()

    print("Länge: " + str(len(myList)))
    print()

    print("Erstes Element " + str(myList.getFirstElem()))
    print("Letztes Element " + str(myList.getLastElem()))
    print()

    searchElem = input("contains: ")
    print(myList.contains(searchElem))
    print()

     
    print("isEmpty: " + str(myList.isEmpty()))
    print()

    searchElem = input("indexOf: ")
    print(myList.indexOf(searchElem))
    print()

    searchIdx = input("getItemAtIndex: ")
    print(myList.getItemAtIndex(searchIdx))
    print()
    
    print(myList.getAllElements())
    print()

    print("addItemAtIndex")
    print("==============")
    setIdx = input("Idx: ")
    setElem = input("Item: ")
    myList.addAtIndex(setIdx, setElem)
    print()
    print(myList.getAllElements())
    print()

    delElem = int(input("deleteValue: "))
    myList.deleteValue(delElem)
    print()
    print(myList.getAllElements())

if __name__ == '__main__':
    main()