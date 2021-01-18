class Players:
	
	HighID = 0
	LowID = 0
	Token = None
	ready = 0
	mapid = 7

	def __init__(self, device):
		self.device = device