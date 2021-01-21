from Packets.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.LoginMessage import LoginMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Packets.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Packets.Messages.Client.TeamSetRankedLocationMessage import TeamSetRankedLocationMessage
from Packets.Messages.Client.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.GetPlayerProfileMessage import GetPlayerProfileMessage
from Packets.Messages.Client.Get_Leaderboard_Message import GetLeaderboardMessage
from Packets.Messages.Client.FacebookConnect import FacebookConnect
from Packets.Messages.Client.AskForPlayingFacebookFriends import AskForPlayingFacebookFriends

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: ChangeAvatarNameMessage,
    10513: AskForPlayingFacebookFriends,
    14109: GoHomeFromOfflinePractiseMessage,
    14113: GetPlayerProfileMessage,
    14201: FacebookConnect,
    #14302: AskAllianceData,
    #14303: AskJoinableAllianceList,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14355: TeamSetMemberReadyMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14403: GetLeaderboardMessage
}
