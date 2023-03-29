import random

class ListElement:
    def __init__(self,obj):
        self.obj = obj
        self.nextElem = None
        self.prevElem = None


    def setNextElem(self,next):
        self.nextElem = next

    def getNextElem(self):
        return self.nextElem
    
    def setPrevElem(self,prev):
        self.prevElem = prev

    def getPrevElem(self):
        return self.prevElem
    
    def getObj(self):
        return self.obj

class DoppeltVerketteteListe:

    def __init__(self):
        self.head = ListElement(None)
        self.tail = ListElement(None)
        self.head.setNextElem(self.tail)
        self.tail.setPrevElem(self.head)

    def getFirstElem(self):
        return self.head.getObj()

    def getLast(self):
        curElem = self.head #Am Anfang Header als letztes Elem

        while curElem.getNextElem() != None: #Schauen so lange nächstes Elem None
            curElem = curElem.getNextElem()
        return curElem
    
    def getLastElem(self):
        return self.getLast().getObj()
    
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
            self.head.setNextElem(self.tail)
            self.tail.setPrevElem(self.head)
            return

        if self.tail.getObj() == None:  #Wenn kein tail vorhanden
            self.tail = newElem
            self.tail.setPrevElem(self.head)
            self.head.setNextElem(self.tail)
            return
        
        #Ansonsten Hinten dranhängen
        lastElem = self.getLast()
        lastElem.setNextElem(newElem)
        newElem.setPrevElem(lastElem)
    
    def delete(self, elem):
        start = self.head

        if elem == start.getObj():
            next = start.getNextElem()
            next.setPrevElem(None)
            self.head = next
        else:
            while start.getNextElem() != None and elem != start.getObj():
                if elem == start.getNextElem().getObj():
                    if start.getNextElem().getNextElem() != None:
                        start.setNextElem(start.getNextElem().getNextElem())
                        start.getNextElem().setPrevElem(start)
                    else:
                        start.setNextElem(None)
                        break
                start = start.getNextElem()

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

    def addAtIndex(self, idxx, value): 
        addElem = ListElement(int(value))
        curElem = self.head
        help = 0
        idx = int(idxx) -1

        if idx >= len(self) - 1:
            raise Exception("Index out of Bounds")

        if int(idxx) == 0:
            
            oldhead = ListElement(self.head.getObj())
            oldhead.setNextElem(self.head.getNextElem())
            self.head.getNextElem().setPrevElem(oldhead)
            self.head = addElem
            self.head.setNextElem(oldhead)
        else:

            while help != idx:
                curElem = curElem.getNextElem()
                help +=1
            
            after = curElem.nextElem
            curElem.nextElem, addElem.nextElem = addElem, after
            addElem.prevElem = curElem
            after.prevElem = addElem
    
    def sort(self):
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
            if head_ref != None:
                head_ref.setPrevElem(new_element)
            head_ref = new_element
        else:
            current = head_ref
            while current.getNextElem() != None and current.getNextElem().getObj() < new_element.getObj():
                current = current.getNextElem()
            new_element.setNextElem(current.getNextElem())
            if current.getNextElem() != None:
                current.getNextElem().setPrevElem(new_element)
            current.setNextElem(new_element)
            new_element.setPrevElem(current)
        return head_ref

def main():
    myList = DoppeltVerketteteListe()

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

    delElem = int(input("deleteValue: "))
    myList.delete(delElem)
    print()
    print(myList.getAllElements())
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

    print("insertion-sort")
    print()
    myList.sort()
    print(myList.getAllElements())

if __name__ == '__main__':
    main()