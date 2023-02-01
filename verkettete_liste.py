import random


class ListElement:
    def __init__(self,obj):
        self.obj = obj
        self.nextElem = None

    def setNextElement(self,next):
        self.nextElem = next

    def getNextElement(self):
        return self.nextElem
    
    def getObject(self):
        return self.obj

class OwnList:
    first = ListElement(None)

    def getLast(self):
        i = self.first
        while i.getNextElement() is not None:
            i = i.getNextElement()
        return i

    def add(self, obj):
        newElement = ListElement(obj)
        if self.first.getObject() is None:
            self.first = newElement
            return
        lastElement = self.getLast()
        lastElement.setNextElement(newElement)

    def __len__(self):
        length = 0
        help = self.first
        if self.first is None:
            return 0
        while help is not None:
            length += 1
            help = help.getNextElement()
        return length

    def getAllElements(self):
        help = self.first
        allElements = '['
        while help is not None:
            allElements+=str(help.obj)+','
            help = help.getNextElement()
        allElements = allElements[:-1]
        return allElements+"]"
    
    def delete(self,object):
        el = self.first
        next = el.getNextElement()

        if el.getObject() == object:
            self.first = self.first.getNextElement()

        while next is not None:
            if next.getObject() == object:
                if next.getNextElement() is not None :
                    while next.getNextElement().getObject() == object:
                        next = next.getNextElement()
                    el.setNextElement(next.getNextElement())
                else:
                    el.setNextElement(None)
            el = el.getNextElement()
            if el == None:
                return
            next = el.getNextElement()

    def getItem(self, obj):
        le = self.first
        while le != None: 
            if le.getObject() == int(obj):
                return True
            le = le.getNextElement()
    
    def getItemByIndex(self,index):
        el = self.first
        for i in range(int(index)):
            el = el.getNextElement()
        return el.getObject()

    def getIndex(self,obj):
        el = self.first
        i = 0
        while el.getObject() != obj:
            if el.getNextElement() != None:
                el = el.getNextElement()
                i+=1
            else:
                i = "NOT IN LIST"
                return i
        return i
    
    def getStart(self):
        return self.first.getObject()
    
    def getEnd(self):
        el = self.first
        while el.getNextElement() != None:
            el=el.getNextElement()
        return el.getObject()
    
    def isEmpty(self):
        if self.first.getObject() is None:
            return True

    def addByIndex(self,index,obj): 
        obj = ListElement(obj)
        if index > len(self):
            print("INDEX out of range")
        current = self.first
        count = 0
        while current is not None:
            if count == index-1:
                current.nextElem, obj.nextElem = obj, current.nextElem
                break
            current = current.nextElem
            count +=1

def main():
    l = OwnList()

    for i in range(100):
        l.add(random.randint(0,10))

    i = l.getAllElements()
    print("Liste: ")
    print(i)
    
    print()
    auswahl = input("Welchen Wert möchtest du löschen? ")
    l.delete(int(auswahl))

    print()
    a = l.getAllElements()
    print("Liste: ")
    print(a)
    
    print()
    print("Länge der Liste: ")
    print(len(l))
    
    print()
    print("getItem: ")
    find = input("Welchen Wert möchtest du finden? ")
    if l.getItem(find) is True:
        print("Ist Bestandteil der Liste")
    else:
        print("Ist nicht Bestandteil der Liste")
    
    print()
    print("getItemByIndex: ")
    find1 = input("Index von zu holendem Item: ")
    print(l.getItemByIndex(find1))

    print()
    print("getIndex: ")
    find2 = input("Item: ")
    print(l.getIndex(int(find2)))

    print()
    print("getStart and getEnd: ")
    print(l.getStart())
    print(l.getEnd())

    print()
    print("isEmpty: ")
    if l.isEmpty() is True:
        print("leere Liste")
    else:
        print("befüllte Liste")

    print()
    print("addByIndex: ")
    find3 = input("An welchen Index möchtest du das Item einfügen? ")
    find4 = input("Welches Item möchtest du einfügen? ")
    l.addByIndex(int(find3),int(find4))
    y = l.getAllElements()
    print("Liste: ")
    print(y)

if __name__ == '__main__':
    main()