from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.PlayerProfileMessage import PlayerProfileMessage

from Utils.Reader import BSMessageReader

class GetPlayerProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_int()
        self.read_int()

    def process(self, crypter):
        PlayerProfileMessage(self.client, self.player).send(crypter)