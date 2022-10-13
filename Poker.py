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
def draw(hand):
    for i in range(hand):
        print(i)

if __name__ == '__main__':
    pool = np.arange(52)
    #testSymbol(pool)
    #testColors(pool)
    draw(5)
    
    
    
    