import random

def createDictionary():
    statistics = {}
    for i in range(45):
        statistics[i + 1] = 0
    return statistics

statistics = createDictionary()
    
def lotto():
    
    len = 44

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
        27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
        39, 40, 41, 42, 43, 44, 45]
    
    result = []
    
    for i in range(6):
        randomIndex = random.randint(0, len)
        
        number = numbers[randomIndex];
        
        numbers[randomIndex] = numbers[len]
        numbers[len] = number
        
        len = len -1
        
        result.append(number)
    return result

def saveInDictionary(results):
    global statistics
    
    for r in results:
        statistics[r] = statistics[r] + 1

if __name__ == '__main__':
    
    print("Es werden 6 Lotto-Zahlen gezogen:")
    for i in range(1000):
        for i in range(6):
            result = lotto()
            saveInDictionary(result)
            
    print(statistics)
        
            
    

    
    
    
    