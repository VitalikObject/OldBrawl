import json
import string
import random
from tinydb import TinyDB, Query
from Utils.Helpers import Helpers

class DataBase:

    def loadAccount(self):
        db = TinyDB('database/Player/data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.Token))
        if user_data:
            self.player.name = user_data[0]["info"]["name"]
            self.player.LowID = user_data[0]["info"]["lowID"]
            self.player.tutorial = user_data[0]["info"]["tutorial"]
            if False:
                self.player.ClubID = user_data[0]["info"]["clubLowID"]
                self.player.ClubRole = user_data[0]["info"]["clubRole"]
                self.player.gems = user_data[0]["info"]["gems"]
                self.player.gold = user_data[0]["info"]["gold"]
                self.player.tickets = user_data[0]["info"]["tickets"]
                self.player.brawlerID = user_data[0]["info"]["brawlerID"]
                self.player.skinID = user_data[0]["info"]["skinID"]
                self.player.trophies = user_data[0]["info"]["trophies"]
                self.player.profileIcon = user_data[0]["info"]["profileIcon"]
                self.player.brawlBoxes = user_data[0]["info"]["brawlBoxes"]
                self.player.bigBoxes = user_data[0]["info"]["bigBoxes"]
                self.player.shellySkin = user_data[0]["info"]["shellySkin"]
                self.player.nitaSkin = user_data[0]["info"]["nitaSkin"]
                self.player.coltSkin = user_data[0]["info"]["coltSkin"]
                self.player.bullSkin = user_data[0]["info"]["bullSkin"]
                self.player.jessieSkin = user_data[0]["info"]["jessieSkin"]
                self.player.brockSkin = user_data[0]["info"]["brockSkin"]
                self.player.dynamikeSkin = user_data[0]["info"]["dynamikeSkin"]
                self.player.boSkin = user_data[0]["info"]["boSkin"]
                self.player.elprimoSkin = user_data[0]["info"]["elprimoSkin"]
                self.player.barleySkin = user_data[0]["info"]["barleySkin"]
                self.player.pocoSkin = user_data[0]["info"]["pocoSkin"]
                self.player.ricoSkin = user_data[0]["info"]["ricoSkin"]
                self.player.darrylSkin = user_data[0]["info"]["darrylSkin"]
                self.player.pennySkin = user_data[0]["info"]["pennySkin"]
                self.player.piperSkin = user_data[0]["info"]["piperSkin"]
                self.player.pamSkin = user_data[0]["info"]["pamSkin"]
                self.player.frankSkin = user_data[0]["info"]["frankSkin"]
                self.player.mortisSkin = user_data[0]["info"]["mortisSkin"]
                self.player.taraSkin = user_data[0]["info"]["taraSkin"]
                self.player.spikeSkin = user_data[0]["info"]["spikeSkin"]
                self.player.crowSkin = user_data[0]["info"]["crowSkin"]


    def createAccount(self):

        db = TinyDB('database/Player/data.db')

        data = {
            "token": str(self.player.Token),

            "info":
                {
                "name": self.player.name,
                "lowID": self.player.LowID,
                "tutorial": 0,
                "clubLowID": 0,
                "clubRole": 0,
                "gems": 99999,
                "gold": 99999,
                "tickets": 99999,
                "brawlerID": 0,
                "skinID": 0,
                "trophies": 99999,
                "profileIcon": 0,
                "brawlBoxes": 99999,
                "bigBoxes": 99999,
                "shellySkin": 0,
                "nitaSkin": 0,
                "coltSkin": 0,
                "bullSkin": 0,
                "jessieSkin": 0,
                "brockSkin": 0,
                "dynamikeSkin": 0,
                "boSkin": 0,
                "elprimoSkin": 0,
                "barleySkin": 0,
                "pocoSkin": 0,
                "ricoSkin": 0,
                "darrylSkin": 0,
                "pennySkin": 0,
                "piperSkin": 0,
                "pamSkin": 0,
                "frankSkin": 0,
                "mortisSkin": 0,
                "taraSkin": 0,
                "spikeSkin": 0,
                "crowSkin": 0,

                }

        }

        db.insert(data)

    def replaceValue(self, value_name, new_value):
        db = TinyDB('database/Player/data.db')
        query = Query()
        data = db.search(query.token == str(self.player.Token))
        user_data = data[0]
        user_data["info"][str(value_name)] = new_value
        db.update(user_data, query.token == str(self.player.Token))

    def createClub(self, clubid):
        clubdb = TinyDB('database/Club/club.db')
        chatdb = TinyDB('database/Club/chat.db')

        data = {
            "clubID": clubid,
            "info": {
                "name": self.clubName,
                "description": self.clubdescription,
                "region": "IL",
                "badgeID": self.clubbadgeID,
                "type": self.clubtype,
                "trophiesneeded": self.clubtrophiesneeded,
                "trophies": self.player.trophies,
                "members": {
                    "totalmembers": 1,
                    str(self.player.LowID): self.player.name
                }
            }
        }
        clubdb.insert(data)
        if False:
            msgData = {
                clubid: {
                    "Total": 1,
                    "1": {
                        "Event": 2,
                        "Tick": 1,
                        "PlayerID": self.player.low_id,
                        "PlayerName": self.player.name,
                        "PlayerRole": 2,
                        "Message": "Welcome to your new club!"
                    }
                }
            }

    def CountClub(self, minMembers, maxMembers, clubType, maxListLength):
        db = TinyDB('database/Club/club.db')
        query = Query()
        club_list = []

        for club in db.all():
            club_id = club['clubID']
            clubInfo = db.search(query.clubid == club_id)[0]['info']
            print(clubInfo)
            # if info["members"]["totalmembers"] >= minMembers and info["members"]["totalmembers"] < maxMembers and info["type"] <= clubType and self.AllianceCount <= maxListLength:

    def loadClub(self, clubid):
        db = TinyDB('database/Club/club.db')
        query = Query()
        data = db.search(query.clubID == self.player.ClubID)
        club_data = data[0]
        self.plrids = []
        self.clubName = club_data["info"]["name"]
        self.clubdescription = club_data["info"]["description"]
        self.clubregion = club_data["info"]["region"]
        self.clubbadgeID = club_data["info"]["badgeID"]
        self.clubtype = club_data["info"]["type"]
        self.clubtrophiesneeded = club_data["info"]["trophiesneeded"]
        self.clubtrophies = club_data["info"]["trophies"]
        self.clubmembercount = club_data["info"]["members"]["totalmembers"]
        for plridentifier, data in club_data["info"]["members"].items():
            if plridentifier != "totalmembers":
                self.plrids.append(int(plridentifier))

    def GetMemberData(self, clubID):
        db = TinyDB('database/Player/data.db')
        query = Query()
        member_list = []

        for i in db.all():
            token = i['token']
            member = db.search(query.token == str(token))[0]['info']
            if member['clubLowID'] == clubID:
                member_list.append(member)
        return member_list

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4):
        db = TinyDB('database/Club/club.db')
        query = Query()
        data = db.search(query.clubID == target)
        print(data, target)
        club_data = data[0]

        club_data["info"]["description"] = inf1
        club_data["info"]["badgeID"] = inf2
        club_data["info"]["type"] = inf3
        club_data["info"]["trophiesneeded"] = inf4

        db.update(club_data, query.clubID == target)