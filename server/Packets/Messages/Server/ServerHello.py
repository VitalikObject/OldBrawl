from Utils.Writer import Writer
from Utils.Helpers import Helpers

class ServerHello(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100
        self.player = player

    def encode(self):
        self.writeInt(24)
        self.buffer += b'\x13Y\xd8\x13M\x19\xf6\xffv\xe7q{\xb0\x9dl\x0c\x81\xe7)(\x9b\t\xc3\xfc'
        #self.writeHexa(Helpers.randomkey(11))
        #self.writeHexa('''00446f6e277420747279203a29''')


        
        print("[INFO] Message ServerHello has been sent.")