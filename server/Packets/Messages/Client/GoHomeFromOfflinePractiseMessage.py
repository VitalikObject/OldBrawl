from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class GoHomeFromOfflinePractiseMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        if self.player.tutorial < 2:
            self.player.tutorial += 1
            DataBase.replaceValue(self, 'tutorial', self.player.tutorial)
        OwnHomeDataMessage(self.client, self.player).send(crypter)