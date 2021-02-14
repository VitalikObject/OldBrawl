from Utils.Writer import Writer
from database.DataBase import DataBase
from Logic.PlayerHome import PlayerHome
from Utils.Helpers import Helpers

from datetime import datetime


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):        
        PlayerHome.encodeHome(self)
        PlayerHome.encodeAvatar(self)

        self.writeVint(int(datetime.timestamp(datetime.now())))


        print("[INFO] Message OwnHomeDataMessage has been sent.")