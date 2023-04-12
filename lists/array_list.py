import random

class ArrayList(): 
    def __init__(self):
        self.arr = []
        self.size = 10

    def len1(self):
        return(len(self.arr))

    def getFirstElem(self):
        return self.arr[0]

    def getLastElem(self):
        return self.arr[-1]
    
    def getAllElements(self):
        allElements = '['

        for i in self.arr:
            allElements += str(i)+', '
        allElements = allElements[:-2]

        return allElements + "]"
    
    def addElem(self, elem):
        self.arr.append(elem)
        if len(self.arr) < self.size:
            return True
        else: 
            self.size *= 2

    def deleteAllOcurrences(self, elem):  
        while self.arr.__contains__(elem):
            self.arr.remove(elem)
        if len(self.arr) <= self.size/2:  
            self.size /= 2
    
    def contains1(self, obj):
        return self.arr.__contains__(obj)
    
    def getItemAtIndex(self,index):
        return self.arr[index]
    
    def indexOf(self,obj):
        return self.arr.index(obj)
    
    def isEmpty(self):
        if self.arr is []:
            return True
        return False

    def addAtIndex(self,index,obj): 
        self.arr.insert(index,obj)
        if len(self.arr) >= self.size:
            self.size *= 2

    def sort1(self):
        self.arr.sort()

def main():
    myList = ArrayList()

    length = int(input("Länge: "))

    for i in range(length):
        myList.addElem(random.randint(0,10))

    print(myList.getAllElements())
    print()

    print("Länge: " + str(myList.len1()))
    print()

    print("Erstes Element " + str(myList.getFirstElem()))
    print("Letztes Element " + str(myList.getLastElem()))
    print()

    searchElem = int(input("contains: "))
    print(myList.contains1(searchElem))
    print()

    print("isEmpty: " + str(myList.isEmpty()))
    print()

    searchElem = int(input("indexOf: "))
    print(myList.indexOf(searchElem))
    print()

    searchIdx = int(input("getItemAtIndex: "))
    print(myList.getItemAtIndex(searchIdx))
    print()
    
    print(myList.getAllElements())
    print()

    print("addItemAtIndex")
    print("==============")
    setIdx = int(input("Idx: "))
    setElem = int(input("Item: "))
    myList.addAtIndex(setIdx, setElem)
    print()
    print(myList.getAllElements())
    print()

    delElem = int(input("deleteAllOcurrences: "))
    myList.deleteAllOcurrences(delElem)
    print()
    print(myList.getAllElements())
    print()

    print("sort")
    myList.sort1()
    
    print(myList.getAllElements())

if __name__ == '__main__':
    main()