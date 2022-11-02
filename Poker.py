import random
import numpy as np

#13 verschiedene Symbole % 13
def testSymbols(arr):
    for i in arr:
        print(i % 13)

#4 verschiedene Farben % 2
def testColors(arr):
    for i in arr:
        print(i % 2)
        
#5 Karten ziehen
def drawFromPool(hand):
    #Pool erstellen
    pool = np.arange(52)
    
    lastIndex = len(pool)
    result = []
    
    #Karten ziehen, ohne sie zurück in den Pool zu legen
    for i in range(hand):
        randomIndex = random.randint(0, lastIndex - 1)
        pick = pool[randomIndex];
        
        pool[randomIndex], pool[lastIndex - 1] = pool[lastIndex - 1], pick
        lastIndex = lastIndex -1
        
        result.append(pick)
        
    return result
        
#===============Kombinationen=============

#Zwei Karten selbes Symbol
def paar(hand):
    for i in hand:
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                return True
    return False

#Zwei Paare ---------------------------------
def zweiPaare(hand): 
    counter = 2
    for i in hand:
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                return True
    return False

#Drei Karten selbes Symbol ---------------------------
def drilling(hand):
    for i in hand:
        counter = 2
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                counter = counter - 1
                if counter == 0:
                    return True
    return False

#Vier Karten selbes Symbol
def vierling(hand):
    for i in hand:
        counter = 3
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                counter = counter - 1
                if counter == 0:
                    return True
    return False
        

if __name__ == '__main__':
    
    for i in range(1000):
        hand = drawFromPool(5)
        if vierling(hand):
            print(hand)
    
    
    
    
    