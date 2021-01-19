from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(201)
        self.writeString(self.player.name)
        self.writeByte(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        
        print("[INFO] Message LogicChangeAvatarNameCommand has been sent.")