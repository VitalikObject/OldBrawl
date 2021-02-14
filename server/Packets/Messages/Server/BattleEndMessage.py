from Utils.Writer import Writer
from database.DataBase import DataBase


class BattleEndMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):   
        self.writeVint(2) #Battle End Screen Type
        self.writeVint(1) #Rank Score
            
        self.writeVint(0) #Battle Tokens 
        self.writeVint(0) #Trophies Value
        self.writeVint(0) #Doubled Tokens
        self.writeVint(0) #Token Doubler Remaining
        self.writeVint(0) #Unknown
        self.writeVint(32) #Type (Capped XP, Star Token, Capped Tokens)
        self.writeVint(1) #End Screen Players

        self.writeString(self.player.name) #Your Name
        self.writeVint(1)  
        self.writeVint(16) # CsvID
        self.writeVint(0)  # BrawlerID
        self.writeVint(29) # CsvID
        self.writeVint(0)  
        self.writeVint(9999) #Brawler Trophies
        self.writeVint(10) #Brawler Power Level
        self.writeVint(0)  #Unknown
        
        self.writeVint(0)  #Unknown
        self.writeVint(0)  #Unknown
        self.writeVint(0)  #Unknown
        self.writeVint(28) #Unknown
        self.writeVint(0)  #Unknown
        print("[INFO] Message BattleEndMessage has been sent.")
