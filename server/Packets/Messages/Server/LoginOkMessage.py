import time

from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(0)
        self.writeInt(self.player.LowID)
        self.writeInt(0)
        self.writeInt(self.player.LowID)
        
        self.writeString(self.player.Token)
        self.writeString()
        self.writeString()
        
        self.writeInt(12)
        self.writeInt(198)
        self.writeInt(0)
        
        self.writeString("integration")
        
        self.writeInt(0) #1
        self.writeInt(0) #1
        self.writeInt(0) #61
        
        self.writeString()
        
        #isAtEnd
        
        self.writeString()
        self.writeString()
        
        #isAtEnd
        
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        
        #isAtEnd
        
        self.writeVint(0)
        
        #isAtEnd
        
        #TODO: stringReference
        print("[INFO] Message LoginOkMessage has been sent.")