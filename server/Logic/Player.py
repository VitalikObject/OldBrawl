class Players:
	
	HighID = 0
	LowID = 0
	Token = None
	name = None
	ready = 0
	roomid = 0
	selected_brawler = 0
	tutorial = 0
	leaderboardtype = 0

	csvid = 15
	mapid = 7

	gold = 20000
	gems = 9999
	boxID = 0
	tickets = 0
	brawlBoxes = 99999
	bigBoxes = 99999
	profileIcon = 20
	trophies = 15000
	experience = 999999
	LeaderboardType = 0
	LeaderboardInfo = 0

	def __init__(self, device):
		self.device = device