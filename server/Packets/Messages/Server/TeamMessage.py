from Utils.Writer import Writer


class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        if self.player.csvid != 8:
            self.writeVint(1) #mode
        else:
            self.writeVint(0)  # mode
        self.writeByte(0)
        self.writeVint(1)
        self.writeInt(0)
        self.writeInt(1) #teamid
        self.writeVint(0)
        self.writeByte(0)
        self.writeByte(0)
        self.writeVint(0)
        
        self.writeVint(15)
        self.writeVint(self.player.mapid)
        
        self.writeVint(1) # Player count
        
        self.writeByte(1) # Gameroom owner boolean

        self.writeInt(0) #HighID
        self.writeInt(1) #LowID
        self.writeString("<c2>Mr Vitalik</c>")
        self.writeVint(3)

        # Brawler
        self.writeVint(16)
        self.writeVint(self.player.selected_brawler)
        self.writeVint(0)
        self.writeVint(9999) # Trophies
        self.writeVint(9999) # Trophies for rank
        self.writeVint(10)   # Power level

        self.writeVint(3) #Playerstate
        self.writeVint(self.player.ready)

        self.writeVint(2)
        self.writeVint(1)

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(0)




        print("[INFO] Message TeamMessage has been sent.")