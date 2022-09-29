import random

def createLottoPool():
    numbers = []
    for i in range(45):
        numbers.append(i + 1)
    return numbers

def createDictionary():
    statistics = {}
    for i in range(45):
        statistics[i + 1] = 0
    return statistics
    
def playLotto():
    
    len = 44
    numbers = createLottoPool()
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
    global statistics
    
    for r in results:
        statistics[r] = statistics[r] + 1


if __name__ == '__main__':
    
    statistics = createDictionary()
    
    print("Es werden einmal 6 Lotto-Zahlen gezogen:")
    print(playLotto())
    
    print("\nEs werden 1000 mal 6 Lotto-Zahlen gezogen:")
    for i in range(1000):
        result = playLotto()
        saveInDictionary(result)
            
    print(statistics)
            
    

    
    
    
    