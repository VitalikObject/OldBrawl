from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.TeamMessage import TeamMessage

from Utils.Reader import BSMessageReader


class TeamSetRankedLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.csvid = self.read_Vint()
        self.player.mapid = self.read_Vint()
    def process(self, crypter):
        TeamMessage(self.client, self.player).send(crypter)