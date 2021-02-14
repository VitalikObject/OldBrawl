from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players

from Utils.Reader import BSMessageReader


class SetDeviceTokenMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.result = self.read_int()
        if self.result > 1000:
            print('[WARNING] Illegal byte array length encountered.')
        self.read_Bytes(self.result)
        self.read_int()

    def process(self, crypter):
        pass