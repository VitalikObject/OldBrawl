from database.DataBase import DataBase
from Utils.Writer import Writer


class ClubInfoMessage(Writer):

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
        self.writeString("<cff2400>V<cff4800>i<cff6d00>t<cfe9100>a<cffb600>l<cffda00>i<cfffe00>k<cffff00>O<cdaff00>b<cb6ff00>j<c91ff00>e<c6dfe00>c<c48ff00>t</c> <c4>and</c> <cff002a>P<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")

        self.writeVint(8)
        #self.writeVint(self.clubbadgeID)
        self.writeVint(0)

        #self.writeVint(self.clubtype)
        self.writeVint(3)
        #self.writeVint(self.clubmembercount) # Club membercount
        self.writeVint(1)

        #self.writeVint(self.clubtrophies)
        self.writeVint(9999)
        #self.writeVint(self.clubtrophiesneeded)
        self.writeVint(10)

        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        print("[INFO] Message ClubInfoMessage has been sent.")
        #else:
         #   self.writeVint(0)
          #  self.writeVint(0)
           # print("[INFO] Message ClubInfoMessage cannot be send because the player is not in a club.")