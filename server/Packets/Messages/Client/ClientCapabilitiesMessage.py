from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players

from Utils.Reader import BSMessageReader


class ClientCapabilitiesMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()

    def process(self, crypter):
        pass