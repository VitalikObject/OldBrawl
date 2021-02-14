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
from Packets.Messages.Client.GetLeaderboardMessage import GetLeaderboardMessage
from Packets.Messages.Client.BindFacebookAccountMessage import BindFacebookAccountMessage
from Packets.Messages.Client.AskForPlayingFacebookFriendsMessage import AskForPlayingFacebookFriendsMessage
from Packets.Messages.Client.AskForBattleEndMessage import AskForBattleEndMessage
from Packets.Messages.Client.HomeBattleReplayMessage import HomeBattleReplayMessage
from Packets.Messages.Client.PlayerStatusMessage import PlayerStatusMessage
from Packets.Messages.Client.AnalyticEventMessage import AnalyticEventMessage
from Packets.Messages.Client.ClientCapabilitiesMessage import ClientCapabilitiesMessage
from Packets.Messages.Client.SetDeviceTokenMessage import SetDeviceTokenMessage
from Packets.Messages.Client.EndClientTurnMessage import EndClientTurnMessage

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10110: AnalyticEventMessage,
    10113: SetDeviceTokenMessage,
    10212: ChangeAvatarNameMessage,
    10513: AskForPlayingFacebookFriendsMessage,
    14102: EndClientTurnMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14114: HomeBattleReplayMessage,
    14201: BindFacebookAccountMessage,
    #14302: AskAllianceData,
    #14303: AskJoinableAllianceList,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14355: TeamSetMemberReadyMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14366: PlayerStatusMessage,
    14403: GetLeaderboardMessage
}
