from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.OwnHomeData import OwnHomeData

from Utils.Reader import BSMessageReader


class GoHomeMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        OwnHomeData(self.client, self.player).send(crypter)