from random import choice
from string import ascii_uppercase
import json
import time
import random

from Logic.Player import Players
from Packets.Messages.Server.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Messages.Server.MyAllianceMessage import MyAllianceMessage

from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class LoginMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = str(self.read_string())
        self.read_int()
        self.read_int()
        self.read_int()

    def process(self, crypter):
        if len(self.player.Token) == 40:
            LoginOkMessage(self.client, self.player).send(crypter)
            DataBase.loadAccount(self)
            OwnHomeDataMessage(self.client, self.player).send(crypter)
            MyAllianceMessage(self.client, self.player).send(crypter)
        else:
            self.player.LowID = random.randint(0, 2147483647)
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits(self)
            LoginOkMessage(self.client, self.player).send(crypter)
            DataBase.createAccount(self)
            OwnHomeDataMessage(self.client, self.player).send(crypter)
            MyAllianceMessage(self.client, self.player).send(crypter)
