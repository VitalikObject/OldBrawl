from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.NameCallback import NameCallback
from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class SetNameMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.name = self.read_string()
        print(self.player.name)

    def process(self, crypter):
        DataBase.replaceValue(self, 'name', self.player.name)
        NameCallback(self.client, self.player).send(crypter)