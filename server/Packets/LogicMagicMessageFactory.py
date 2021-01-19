from Packets.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.LoginMessage import LoginMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Packets.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Packets.Messages.Client.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.GetPlayerProfileMessage import GetPlayerProfileMessage

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: ChangeAvatarNameMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14113: GetPlayerProfileMessage,
    #14302: AskAllianceData,
    #14303: AskJoinableAllianceList,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14355: TeamSetMemberReadyMessage,
}
