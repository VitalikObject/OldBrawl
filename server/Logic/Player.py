class Players:
	
	HighID = 0
	LowID = 0
	Token = None
	name = "Guest"
	ready = 0
	roomid = 0
	selected_brawler = 0

	csvid = 15
	mapid = 7

	gold = 20000
	gems = 9999
	tickets = 0
	brawlBoxes = 99999
	bigBoxes = 99999
	profileIcon = 20
	trophies = 15000
	experience = 999999

	def __init__(self, device):
		self.device = device