from database.DataBase import DataBase
from Packets.Messages.Server.FriendListMessage import FriendListMessage
#from Packets.Messages.Server.Friend.Events.FBAccountDisconnectedOKMessage import FBAccountDisconnectedOKMessage

from Utils.Reader import BSMessageReader

class AskForPlayingFacebookFriendsMessage(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_string()
        #self.player.FacebookToken = self.read_string()

    def process(self, crypter):
        pass
        #self.player.IsFacebookLinked = 1
        #DataBase.replaceValue(self, 'isFBLinked', 1)
        #DataBase.replaceValue(self, 'facebookID', self.player.FacebookID)
        #DataBase.replaceValue(self, 'facebookToken', self.player.FacebookToken)
    
        FriendListMessage(self.client, self.player).send(crypter)