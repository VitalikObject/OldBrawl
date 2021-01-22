from Utils.Writer import Writer
from database.DataBase import DataBase


class BattleResult2Message(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(1)  # Battle End Screen Type
        self.writeVint(0)  # Game Type
        self.writeVint(20)  # Battle Tokens
        self.writeVint(5)  # Trophies Value
        self.writeVint(20)  # Doubled Tokens
        self.writeVint(180)  # Token Doubler Remaining
        self.writeVint(5)  # Unknown (XP??)
        self.writeVint(23)  # Type (Capped XP, Star Token, Capped Tokens)
        self.writeVint(5)  # End Screen Players

        self.writeVint(1)  # Battle End Screen Players

        self.writeString(self.player.name)
        self.writeVint(5)
        self.writeVint(16) # CsvID
        self.writeVint(self.player.brawlerID)  # BrawlerID
        self.writeVint(29)
        self.writeVint(self.player.skinID)
        self.writeVint(500)
        self.writeVint(10)