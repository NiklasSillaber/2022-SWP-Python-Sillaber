import numpy as np

#13 verschiedene Symbole % 13
def testSymbols(arr):
    for i in arr:
        print(i % 13)

#4 verschiedene Karten % 4
def testColors(arr):
    for i in arr:
        print(i % 4)

if __name__ == '__main__':
    pool = np.arange(52)
    #testSymbol(pool)
    #testColors(pool)
    
    
    
    