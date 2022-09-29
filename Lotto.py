import random

def createLottoPool(min, max):
    numbers = []
    for i in range(min, max + 1):
        numbers.append(i)    
    return numbers

def createDictionary(min, max):
    statistics = {}
    for i in range(min, max + 1):
        statistics[i] = 0
    return statistics
    
def playLotto(min, max):
    
    len = max - min
    numbers = createLottoPool(min, max)
    result = []
    
    #draw 6 numbers without putting them back to pool
    for i in range(6):
        randomIndex = random.randint(0, len)
        pick = numbers[randomIndex];
        result.append(pick)
        
        numbers[randomIndex], numbers[len] = numbers[len], pick
        len = len -1
        
    return result

def saveInDictionary(results):
    
    for r in results:
        statistics[r] = statistics[r] + 1

#Zahlen sollen auch dynamisch sein
#man soll eingeben von wo bis wo die Zahlen gehen und die Anzahl der Ziehungen

#in mehrere Python Dateien: Python hat __Variablen__, werden von Python angelegt. in der __name__ steckt immer der Name von jeder Python Datei drinnen
if __name__ == '__main__':
    
    min, max, number_picks = 50, 99, 100000
    
    statistics = createDictionary(min, max)
    
    print("\nEs werden " + str(number_picks) + " mal 6 Lotto-Zahlen gezogen:")
    for i in range(number_picks):
        result = playLotto(min, max)
        saveInDictionary(result)
            
    print(sorted(statistics.values()))
            
    

    
    
    
    