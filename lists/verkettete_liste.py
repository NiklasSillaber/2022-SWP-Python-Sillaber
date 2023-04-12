import random

#ListElem
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

class VerketteteListe():

    def __init__(self):
        self.head = ListElement(None)

    def isEmpty(self):
        return self.head.getObj() == None
    
    def getLast(self):
        curElem = self.head #Am Anfang Header als letztes Elem

        while curElem.getNextElem() != None: #Schauen so lange nächstes Elem None
            curElem = curElem.getNextElem()
        return curElem

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
    
    def deleteAllOcurrences(self, delElem):
        el = self.head
        next = el.getNextElem()

        if el.getObj() == delElem:   #Muss Head gelöscht werden
            self.head = self.head.getNextElem()

        while next is not None:
            if next.getObj() == delElem:
                if next.getNextElem() is not None :
                    while next.getNextElem().getObj() == delElem:
                        next = next.getNextElem()
                    el.setNextElem(next.getNextElem())
                else:
                    el.setNextElem(None)
            el = el.getNextElem()
            if el == None:
                return
            next = el.getNextElem()

    def contains(self, value): #Schaun ob bestimmtes Item in der Liste ist
        curElem = self.head

        while curElem != None: 
            if curElem.getObj() == int(value):
                return True

            curElem = curElem.getNextElem()
        return False

    def indexOf(self, value):   #index of first occurrence
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

    def sort(self): #insertion sort
        sorted = None
        current = self.head
        while (current != None):
            next = current.getNextElem()
            sorted = self.sorted_insert(sorted, current)
            current = next
        self.head = sorted

    def sorted_insert(self, head_ref, new_element):
        current = None
        if head_ref == None or (head_ref).getObj() >= new_element.getObj():
            new_element.setNextElem(head_ref)
            head_ref = new_element
        else:
            current = head_ref
            while current.getNextElem() != None and current.getNextElem().getObj() < new_element.getObj():
                current = current.getNextElem()
            new_element.setNextElem(current.getNextElem())
            current.setNextElem(new_element)
        return head_ref

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

    delElem = int(input("deleteAllOcurrences: "))
    myList.deleteAllOcurrences(delElem)
    print()
    print(myList.getAllElements())
    print()

    print("insertion-sort")
    print()
    myList.sort()
    print(myList.getAllElements())


if __name__ == '__main__':
    main()