from Utils.Writer import Writer

class FacebookAccountBoundMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24201
        self.player = player

    def encode(self):
        self.writeInt(0)
        print("[INFO] Message FacebookAccountBoundMessage has been sent.")