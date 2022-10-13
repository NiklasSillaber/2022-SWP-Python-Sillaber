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
        
        

if __name__ == '__main__':
    #testSymbol(pool)
    #testColors(pool)
    print(drawFromPool(5))
    
    
    
    
    