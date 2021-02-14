from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.TeamMessage import TeamMessage
from Packets.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage

from Utils.Reader import BSMessageReader


class TeamSetMemberReadyMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        if(self.player.ready == 1):
            self.player.ready = 0
        else:
            self.player.ready = 1
        TeamMessage(self.client, self.player).send(crypter)
        #TeamGameStartingMessage(self.client, self.player).send(crypter)
        