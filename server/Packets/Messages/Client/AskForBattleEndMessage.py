from Packets.Messages.Server.BattleEndMessage import BattleEndMessage

from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.GameType = self.read_Vint()
        self.read_Vint()
        self.player.Rank = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.Team = self.read_Vint() #red or blue

        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot5N = self.read_string()
        
    def process(self, crypter):
        BattleEndMessage(self.client, self.player).send(crypter)