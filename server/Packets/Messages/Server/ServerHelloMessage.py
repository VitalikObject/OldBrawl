from Utils.Writer import Writer
from Utils.Helpers import Helpers

class ServerHelloMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100
        self.player = player

    def encode(self):
        self.writeInt(24)
        self.writeHexa(Helpers.randomkey(11))
        self.writeHexa('''00446f6e277420747279203a29''')


        
        print("[INFO] Message ServerHelloMessage has been sent.")