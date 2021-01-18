from random import choice
from string import ascii_uppercase
import json
import time

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Packets.Messages.Server.ClubInfoMessage import ClubInfoMessage

from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class Login(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        print(self.read_int())
        print(self.read_int())
        print(self.read_string())
        print(self.read_int())
        print(self.read_int())
        print(self.read_int())

    def process(self, crypter):
        LoginOk(self.client, self.player).send(crypter)
        OwnHomeData(self.client, self.player).send(crypter)
        ClubInfoMessage(self.client, self.player).send(crypter)