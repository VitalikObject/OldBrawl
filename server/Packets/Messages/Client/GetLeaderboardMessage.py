from Packets.Messages.Server.LeaderboardMessage import LeaderboardMessage

from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.LeaderboardType = self.read_Vint()
        self.player.LeaderboardInfo = self.read_Vint()

    def process(self, crypter):
        LeaderboardMessage(self.client, self.player).send(crypter)
