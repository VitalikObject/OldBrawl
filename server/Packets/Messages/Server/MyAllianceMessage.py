from database.DataBase import DataBase
from Utils.Writer import Writer


class MyAllianceMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.player = player
        #self.clubLowID = clubLowID

    def encode(self):
        #if self.clubLowID != 0:
            #DataBase.loadClub(self, self.clubLowID)
        #self.writeVint(self.clubmembercount)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(25)

        #self.writeVint(self.player.ClubRole)
        self.writeVint(2)

        self.writeInt(0)
        #self.writeInt(self.clubLowID)
        self.writeInt(1)

        #self.writeString(self.clubName)
        self.writeString("Test Club")

        self.writeVint(8)
        #self.writeVint(self.clubbadgeID)
        self.writeVint(0)

        #self.writeVint(self.clubtype)
        self.writeVint(3)
        #self.writeVint(self.clubmembercount) # Club membercount
        self.writeVint(100)

        #self.writeVint(self.clubtrophies)
        self.writeVint(9999)
        #self.writeVint(self.clubtrophiesneeded)
        self.writeVint(10)

        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        print("[INFO] Message MyAllianceMessage has been sent.")
        #else:
         #   self.writeVint(0)
          #  self.writeVint(0)
           # print("[INFO] Message ClubInfoMessage cannot be send because the player is not in a club.")