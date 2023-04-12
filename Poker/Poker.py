import random
import time
import numpy as np

#13 verschiedene Symbole % 13
def test_symbols(arr):
    for i in arr:
        print(i % 13)

#4 verschiedene Farben % 4
def test_colors(arr):
    for i in arr:
        print(i % 4)
        
#5 Karten ziehen
def draw_from_pool(hand):
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
    
    helpZweiPaare = hand.copy()
    
    for i in hand:
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                helpZweiPaare.remove(i)
                helpZweiPaare.remove(j)
                return True, helpZweiPaare
    return False, []

#Zwei Paare ---------------------------------
def zwei_paare(hand): 
    isPaar, left3 = paar(hand)
    if isPaar:
        isSecondPaar, left1 = paar(left3)
        if isSecondPaar:
            return True
    return False

#Drei Karten selbes Symbol ---------------------------
def drilling(hand):
    
    for i in hand:
        counter = 2
        
        #Für das Full House werden die beiden Karten, die nicht zum Drilling beitragen, benötigt
        helpFullHouse = hand.copy()
        
        for j in np.delete(hand, np.where(hand == i)):
            if i % 13 == j % 13:
                helpFullHouse.remove(j)
                counter = counter - 1
                if counter == 0:
                    helpFullHouse.remove(i)
                    return True, helpFullHouse
    return False, []

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
        
#Straße
def strasse(hand):
    arr = []
    for i in hand:
        arr.append(i % 13)
    sorted = np.sort(arr)
    
    for i in range(0, 5):
        
        if i == 0:
            continue
            
        if sorted[i] - sorted[i - 1] != 1:
            return False

    return True
    
#Flush
def flush(hand):
    first = hand[0]
    
    for i in np.delete(hand, np.where(hand == first)):
        
        if first % 4 != i % 4:
            return False
    return True

#Full House
def full_house(hand):
    isDrilling, left2 = drilling(hand)
    if isDrilling:
        if left2[0] % 13 == left2[1] % 13:
            return True
    return False

#Straight Flush
def straight_flush(hand):
    if strasse(hand):
        color = hand[0] % 4
        for i in range(1, 5):
            if hand[i] % 4 != color:
                return False
        return True
    return False

#Royal Flush
def royale_flush(hand):
    if straight_flush(hand):
        for i in hand:
            if i % 13 == 12:
                return True
    return False

#Dictionary Anzahl Kombinationen
def recognizeAndAddKombination(hand, kombinations):
    isPaar, left3 = paar(hand)
    isDrilling, left2 = drilling(hand)
    
    if royale_flush(hand):
        kombinations['royaleFlush'] += 1
    elif straight_flush(hand):
        kombinations['straightFlush'] += 1
    elif vierling(hand):
        kombinations['vierling'] += 1
    elif full_house(hand):
        kombinations['fullHouse'] += 1
    elif flush(hand):
        kombinations['flush'] += 1
    elif strasse(hand):
        kombinations['straße'] += 1
    elif isDrilling:
        kombinations['drilling'] += 1
    elif zwei_paare(hand):
        kombinations['zweiPaare'] += 1
    elif isPaar:
        kombinations['paar'] += 1

def calculateProbabilities(kombinations, games, realProbsPerc):
    print('Vergleich der Wahrscheinlichkeiten')
    print('==================================')
    print('Berechnete Wahrscheinlichkeit => Recherchierte Wahrscheinlichkeit')
    
    
    for key in kombinations:
        prob = kombinations[key] * 100 / games
        prob = round(prob, 3)
        print(key + ": " + str(prob) + " % => "+ str(realProbsPerc[key]) + ' %')

def main():
    kombinations = {'paar' : 0, 'zweiPaare' : 0, 'drilling' : 0, 'straße' : 0, 
                    'flush' : 0, 'fullHouse' : 0, 'vierling' : 0, 'straightFlush' : 0,
                    'royaleFlush' : 0}
    
    realProbsPerc = {'paar' : 42.2569, 'zweiPaare' : 4.7539, 'drilling' : 2.1128, 'straße' : 0.3925, 
                    'flush' : 0.1965, 'fullHouse' : 0.1441, 'vierling' : 0.0240, 'straightFlush' : 0.00139,
                    'royaleFlush' : 0.000154}
    
    games = int(input("Wie viele Spiele möchten sie spielen?"))
    starttime = time.time() * 1000
    for i in range(games):
        hand = draw_from_pool(5)
        recognizeAndAddKombination(hand, kombinations)
    endtime = time.time() * 1000
    print("\nAnzahl der Kombinationen")
    print("------------------------")
    print(kombinations)
    calculateProbabilities(kombinations, games, realProbsPerc)
   
    millis = round((endtime-starttime) / 1000, 2)
    print("Zeitbedarf: " + str(millis) + " Sekunden")
    
if __name__ == '__main__':
    main()
   
    
    
    