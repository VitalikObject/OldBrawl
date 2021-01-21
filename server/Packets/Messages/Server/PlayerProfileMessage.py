from Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(0) #HighID
        self.writeVint(1) #LowID
        self.writeString("dsadsad")
        self.writeVint(0)

        self.writeVint(1)

        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(11)

        self.writeVint(1)
        self.writeVint(1) # Total victories

        self.writeVint(2)
        self.writeVint(2) # Player experience

        self.writeVint(3)
        self.writeVint(3) # Trophies

        self.writeVint(4)
        self.writeVint(4) # Highest trophies

        self.writeVint(5)
        self.writeVint(1) # Brawlers count

        self.writeVint(6)
        self.writeVint(0) # Unknown

        self.writeVint(7)
        self.writeVint(0) # Profile icon

        self.writeVint(8)
        self.writeVint(7) # Solo victories

        self.writeVint(9)
        self.writeVint(8) # Best robo rumble time

        self.writeVint(10)
        self.writeVint(9) # Best time as big brawler

        self.writeVint(11)
        self.writeVint(10) # Duo victories

        self.writeVint(0)
        self.writeVint(0)
        print("[INFO] Message PlayerProfileMessage has been sent.")