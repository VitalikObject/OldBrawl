from Utils.Writer import Writer
import random

class LogicGiveDeliveryItemsCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):

        self.writeVint(203)
        if self.player.boxID == 5:
            self.writeVint(10)
        elif self.player.boxID == 4:
            self.writeVint(12)
        elif self.player.boxID == 3:
            self.writeVint(11)
        elif self.player.boxID == 1:
            self.writeVint(12)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(random.randrange(100, 1000))


        self.writeVint(0)
        self.writeVint(7)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(random.randrange(1, 20))
        self.writeVint(0)

        self.writeVint(8)  

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        print("[INFO] Message LogicGiveDeliveryItemsCommand has been sent.")