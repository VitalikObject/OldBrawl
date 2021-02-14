from Utils.Writer import Writer


class TeamLeftMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24125
        self.player = player

    def encode(self):
        self.writeInt(0)
        print("[INFO] Message TeamLeftMessage has been sent.")