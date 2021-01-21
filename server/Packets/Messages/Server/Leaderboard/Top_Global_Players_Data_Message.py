from Utils.Writer import Writer
from database.DataBase import DataBase


class GetLeaderboardGlobalOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeBoolean(True)
        self.writeVint(0)
        self.writeString()


        self.writeVint(1) # Players Count


        self.writeVint(0) # High ID
        self.writeVint(1) # Low ID

        self.writeVint(1)
        self.writeVint(99999) # Player Trophies

        self.writeVint(1)

        self.writeString("Mr vitalik")  # Player Name
        self.writeString() # Club Name

        self.writeVint(1) # Player Level
        self.writeVint(28)
        self.writeVint(0)
        self.writeVint(0)


        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)

        self.writeString("RO")
