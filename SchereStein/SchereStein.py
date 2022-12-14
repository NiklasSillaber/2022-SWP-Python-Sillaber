from random import randrange
from tabulate import tabulate
import requests
import json

class Symbol():
        def __init__(self, symbol):
            self.symbol = symbol
            #hier ist die Reihenfolge der Symbole wichtig ==> für Logik
            self.symbols = ['STEIN', 'ECHSE', 'SPOCK', 'SCHERE', 'PAPIER']
            
            leftSymbols = list(filter(lambda x: self.symbols.index(x) < self.symbols.index(self.symbol), self.symbols))
            rightSymbols = list(filter(lambda x: self.symbols.index(x) > self.symbols.index(self.symbol), self.symbols))
            self.otherSymbols = rightSymbols + leftSymbols
            #print(self.otherSymbols)      bei SPOCK =>  [SCHERE, PAPIER, STEIN, ECHSE]
            
        def playAgainst(self, symbolComp):
            if symbolComp == self.symbol:
                return 0
            elif symbolComp == self.otherSymbols[0] or symbolComp == self.otherSymbols[2]:
                return 1
            else:
                return -1
        
        def getCounter(self):
            return self.otherSymbols[1]


class game():
    def __init__ (self):
        self.difficulty = None
        self.inputs = ['GAME', 'STATISTICS', 'UPLOAD']
        self.difficulties = [1, 2, 3]
        self.symbols = ['SCHERE', 'STEIN', 'PAPIER', 'SPOCK', 'ECHSE']
        self.winsPlayer = 0
        self.winsComp = 0
        
        self.statistics = self.getDataFromApi()
        print(self.statistics)
        
        print("\nWilkommen zum SchereStein-Spiel!")
        print("================================\n")
        self.showMenu()
        pass
    
    def showMenu(self):
        action = ''
        print("/[MENU]: Sie befinden sich im Menü. Geben Sie eine der folgenen Funktionen ein! " + str(self.inputs))
        
        while True: 
            action = input('/[MENU]/').upper()
            if self.validateInputMenu(action):
                break
        
        if action == 'GAME':
            self.startGame()
        elif action == 'STATISTICS':
            self.showStatistics()
        else:
            self.uploadToApi()
             
    def validateInputMenu(self, input):
        input = input.upper()
        if input not in self.inputs:
            if input is '':
                return False
            print("/[MENU]: Fehler! Geben Sie eine der folgenen Funktionen ein! " + str(self.inputs))
            return False
        return True
    
    def validateInputGame(self, input):
        input = input.upper()
        symbols = self.symbols.copy()
        symbols.append('EXIT')
        if input not in symbols:
            if input is '':
                return False
            print("/[MENU]/[GAME" + self.difficulty + "]: Fehler! Geben Sie eines der folgenden Symbole ein! " + str(self.symbols))
            return False
        return True
    
    def validateInputDifficulty(self, input):
        difficultiesString = map(lambda x: str(x), self.difficulties)
        if input not in difficultiesString:
            if input is '':
                return False
            elif input == 'EXIT':
                self.difficulty = input
                return True
            print("/[MENU]/[GAME]: Fehler! Geben Sie eine der folgenen Schwierigkeiten ein! " + str(self.difficulties))
            return False
        self.difficulty = input
        return True
    
    def getDataFromApi(self):
        url="http://127.0.0.1:5000/getStatistics"
        data = requests.get(url)
        if data != None:
            data = data.json()
            return data

    def uploadToApi(self):
        url="http://127.0.0.1:5000/uploadData"
        requests.post(url, json.dumps(self.statistics))
        self.showMenu()

    def calcMostPicked(self):
        picksPlayer = self.statistics['PLAYER'][2:]
        max = picksPlayer[0]
        for i in picksPlayer:
            if i > max:
                max = i
        for i in picksPlayer:
            if i == max:
                return picksPlayer.index(i)

    def showStatistics(self):
        #print("/[MENU]: " + str(self.statistics))
        headers = ['NAME', 'WINS', 'DRAWS'] + self.symbols
        playerData = ['PLAYER'] + self.statistics['PLAYER']
        compData = ['COMP'] + self.statistics['COMP']
        data = [playerData, compData]
        
        print(tabulate(data, headers=headers, tablefmt='orgtbl'))
        self.showMenu()
        
    
    def pickCompSymbol(self, symbolPlayer):
        #Leichter Modus => zufällige Wahl des Gegeners
        if int(self.difficulty) == 1:
            return self.symbols[randrange(0, 5)]
        elif int(self.difficulty) == 2:
            mostPicked = self.symbols[self.calcMostPicked()]
            s = Symbol(mostPicked)
            return s.getCounter()
        else:
            s = Symbol(symbolPlayer)
            return s.getCounter()
    
    def handleResult(self, result, symbolP, symbolC):
        self.statistics["PLAYER"][self.symbols.index(symbolP) + 2] += 1
        self.statistics["COMP"][self.symbols.index(symbolC) + 2] += 1
        
        if result is 0:
                print("/[MENU]/[GAME" + self.difficulty + "]: --> UNENTSCHIEDEN <--")
                self.statistics["PLAYER"][1] += 1
                self.statistics["COMP"][1] += 1
        elif result is 1:
            print("/[MENU]/[GAME" + self.difficulty + "]: --> GEWONNEN <--")
            self.winsPlayer += 1
            self.statistics["PLAYER"][0] += 1
        else:
            print("/[MENU]/[GAME" + self.difficulty + "]: --> VERLOREN <--")
            self.winsComp += 1
            self.statistics["COMP"][0] += 1
    
    def exit(self):
        self.difficulty = None
        self.winsPlayer = 0
        self.winsComp = 0
        print("/[MENU]:")
        self.showMenu()
    
    def startGame(self):
        print("/[MENU]/[GAME]: Sie befinden sich im Spiel. Geben Sie eine Schwierigkeit ein! " + str(self.difficulties))
        
        while True: 
            difficulty = input('/[MENU]/[GAME]: ').upper()
            if self.validateInputDifficulty(difficulty):
                break
            
        if self.difficulty == 'EXIT':
            self.exit()
            
        print("/[MENU]/[GAME" + self.difficulty + "]: Die Schwierigkeit " + self.difficulty + " wurde gewählt!")
        print("/[MENU]/[GAME" + self.difficulty + "]: Das Spiel startet jetzt! Mit EXIT können Sie das Spiel frühzeitig beenden!")
        print("/[MENU]/[GAME" + self.difficulty + "]:")
        
        while True:
            print("/[MENU]/[GAME" + self.difficulty + "]: PLAYER " + str(self.winsPlayer) + " | " + str(self.winsComp) + " COMP")
            print("/[MENU]/[GAME" + self.difficulty + "]: Geben Sie ihr Symbol ein! " + str(self.symbols))
            
            while True: 
                symbolPlayer = input('/[MENU]/[GAME' + self.difficulty + ']: ').upper()
                if self.validateInputGame(symbolPlayer):
                    break
                
            if symbolPlayer == 'EXIT':
                break
            
            symbolPlayer_obj = Symbol(symbolPlayer)
            symbolComp = self.pickCompSymbol(symbolPlayer)
            print("/[MENU]/[GAME" + self.difficulty + "]: PLAYER " + str(symbolPlayer) + " | " + str(symbolComp) + " COMP")
            result = symbolPlayer_obj.playAgainst(symbolComp)
            self.handleResult(result, symbolPlayer, symbolComp)
            print("/[MENU]/[GAME" + self.difficulty + "]:")
        
        self.exit()
    
if __name__ == "__main__":
    game = game()