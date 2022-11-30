from random import randrange


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
                print("/[MENU]/[GAME]: --> UNENTSCHIEDEN <--")
            elif symbolComp == self.otherSymbols[0] or symbolComp == self.otherSymbols[2]:
                print("/[MENU]/[GAME]: --> GEWONNEN <--")
            else:
                print("/[MENU]/[GAME]: --> VERLOREN <--")

class game():
    def __init__ (self):
        self.difficulty = None
        self.inputs = ['GAME', 'STATISTICS', 'UPLOAD']
        self.difficulties = [1, 2, 3]
        self.play = True
        self.symbols = ['SCHERE', 'STEIN', 'PAPIER', 'SPOCK', 'ECHSE']
        
        print("\nWilkommen zum SchereStein-Spiel!")
        print("================================\n")
        self.showMenu()
        pass
    
    def showMenu(self):
        action = ''
        print("/[MENU]: Sie befinden sich im Menü. Geben Sie eine der folgenen Funktionen ein! " + str(self.inputs))
        
        while True: 
            action = input('/[MENU]/')
            if self.validateInputMenu(action):
                break
        
        if action == 'GAME':
            self.startGame()
        elif action is 'STATISTICS':
            self.showStatistics()
        else:
            self.uploadToApi()
        
            
    def validateInputMenu(self, input):
        if input not in self.inputs:
            if input is '':
                return False
            print("/[MENU]: Fehler! Geben Sie eine der folgenen Funktionen ein! " + str(self.inputs))
            return False
        return True
    
    def validateInputGame(self, input):
        symbols = self.symbols.copy()
        symbols.append('EXIT')
        if input not in symbols:
            if input is '':
                return False
            print("/[MENU]/[GAME]: Fehler! Geben Sie eines der folgenden Symbole ein! " + str(self.symbols))
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
    
    def uploadToApi(self):
        pass
    
    def showStatistics(self):
        pass
    
    def pickCompSymbol(self, symbolPlayer):
        #Leichter Modus => zufällige Wahl des Gegeners
        if int(self.difficulty) is 1:
            return self.symbols[randrange(0, 5)]
    
    def startGame(self):
        print("/[MENU]/[GAME]: Sie befinden sich im Spiel. Geben Sie eine Schwierigkeit ein! " + str(self.difficulties))
        
        while True: 
            difficulty = input('/[MENU]/[GAME]: ')
            if self.validateInputDifficulty(difficulty):
                break
            
        if self.difficulty == 'EXIT':
            self.difficulty = None
            self.showMenu() 
            
        print("/[MENU]/[GAME]: Die Schwierigkeit " + self.difficulty + " wurde gewählt!")
        print("/[MENU]/[GAME]: Das Spiel startet jetzt! Mit EXIT können Sie das Spiel frühzeitig beenden!")
        print("/[MENU]/[GAME]:")
        
        while self.play:
            print("/[MENU]/[GAME]: PLAYER 0 | 0 COMP")
            print("/[MENU]/[GAME]: Geben Sie ihr Symbol ein! " + str(self.symbols))
            
            while True: 
                symbolPlayer = input('/[MENU]/[GAME]: ')
                if self.validateInputGame(symbolPlayer):
                    break
                
            if symbolPlayer == 'EXIT':
                break
            
            symbolPlayer_obj = Symbol(symbolPlayer)
            symbolComp = self.pickCompSymbol(symbolPlayer)
            print("/[MENU]/[GAME]: PLAYER " + str(symbolPlayer) + " | " + str(symbolComp) + " COMP")
            symbolPlayer_obj.playAgainst(symbolComp)
        
        self.difficulty = None
        self.showMenu()
    
    
            

            
            
            
        
        
    
if __name__ == "__main__":
    game = game()