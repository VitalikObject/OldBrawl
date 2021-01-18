from Packets.Messages.Client.ClientHello import ClientHello
from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.SetNameMessage import SetNameMessage
from Packets.Messages.Client.GoHomeMessage import GoHomeMessage
from Packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Packets.Messages.Client.TeamSetLocationMessage import TeamSetLocationMessage

packets = {
    10100: ClientHello,
    10101: Login,
    10108: KeepAlive,
    10212: SetNameMessage,
    14109: GoHomeMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14355: TeamSetMemberReadyMessage,
    14363: TeamSetLocationMessage
}
