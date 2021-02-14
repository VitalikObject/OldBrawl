from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

from Utils.Reader import BSMessageReader


class LogicGatchaCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        for x in range(5):
            self.read_Vint()
        
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.boxID = self.read_Vint()

    def process(self, crypter):
        LogicGiveDeliveryItemsCommand(self.client, self.player).send(crypter)