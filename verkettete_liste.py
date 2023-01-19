class ListElement:
    
    #Class attributes

    def __ini__(self, obj):
        self.obj = obj
        self.nextElement = None

    def setNextItem(self, nextElement):
        self.nextElement = nextElement

    def getNextItem(self):
        return self.nextElement

    def getObject(self):
        return self.obj

class EinfachVerketteteListe:

    def __ini__(self):
        self.startElem = ListElement("Kopf")

    def addLast(self, obj):
        newElem = ListElement(obj)
        lastElem = getLastElem()
        lastElem.setNextItem(newElem)

    def insertAfter(self, prevItem, newItem):
        newElem, nextElem = ListElement(newItem)








