from random import choice
from string import ascii_uppercase
import json
import time

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData

from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class Login(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = self.read_string()
        print(self.read_int())
        print(self.read_int())
        print(self.read_int())

    def process(self, crypter):
        if self.player.LowID >= 0:
            LoginOk(self.client, self.player).send(crypter)
            DataBase.loadAccount(self)
            OwnHomeData(self.client, self.player).send(crypter)
        else:
            self.player.LowID = Helpers.randomID(self)
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits(self)
            LoginOk(self.client, self.player).send(crypter)
            DataBase.createAccount(self)
            OwnHomeData(self.client, self.player).send(crypter)