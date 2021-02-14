from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.KeepAliveServerMessage import KeepAliveServerMessage
from Packets.LogicCommandManager import commands

from Utils.Reader import BSMessageReader


class EndClientTurnMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.data = initial_bytes
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.tickCheck = self.read_Vint()
        if self.tickCheck != 0:
            self.commandID = self.read_Vint()

    def process(self, crypter):
        if self.tickCheck != 0:
            if self.commandID in commands:
                print("[INFO] Command ID", self.commandID, "has been handled")
                message = commands[self.commandID](self.client, self.player, self.data)
                message.decode()
                message.process(crypter)
            elif self.commandID > 0:
                print("[INFO] Command ID", self.commandID, "is not handled!")        