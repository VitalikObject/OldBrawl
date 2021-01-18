from Utils.Writer import Writer


class NameCallback(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(201)
        self.writeString("RetroBrawl")
        self.writeByte(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        
        print("[INFO] Message SetName has been sent.")