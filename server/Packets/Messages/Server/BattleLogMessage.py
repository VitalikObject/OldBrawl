from Utils.Writer import Writer


class BattleLogMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23458
        self.player = player

    def encode(self):
        self.writeVint(1)
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeBool(False)
        
        self.writeVint(0)
        
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVint(1)
        
        self.writeVint(0)
        self.writeInt(0)
        self.writeInt(0)        
        self.writeVint(0)
        self.writeBool(False)
        self.writeInt(0)
        self.writeInt(0) 

        self.writeVint(0)       

        self.writeVint(0)
        self.writeVint(0)
        print("[INFO] Message BattleLogMessage has been sent.")