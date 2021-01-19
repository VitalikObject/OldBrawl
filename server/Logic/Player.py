class Players:
	
	HighID = 0
	LowID = 0
	Token = None
	name = "Guest"
	ready = 0
	mapid = 7

	gold = 0
	gems = 0
	tickets = 0
	brawlBoxes = 0
	bigBoxes = 0
	profileIcon = 0
	trophies = 0
	experience = 0

	def __init__(self, device):
		self.device = device