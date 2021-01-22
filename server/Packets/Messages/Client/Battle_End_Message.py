from Packets.Messages.Server.Battle_Result2_Message import BattleResult2Message

from Utils.Reader import BSMessageReader


class BattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        NameList = []
        BrawlerID = []
        for i in range(5):
            print(i, self.read_Vint())

        self.playerCount = self.read_Vint()

        for i in range(self.playerCount):
            self.read_Vint()  # CsvID
            BrawlerID.append(self.read_Vint())  # BrawlerID

            self.read_Vint()  # ???

            self.read_Vint()
            self.read_Vint()
            NameList.append(self.read_string())

    def process(self, crypter):
        BattleResult2Message(self.client, self.player).send(crypter)