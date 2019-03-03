class Difficulty:
	def __init__(self,Difficulty):
		self.Difficulty = Difficulty

	def getCountDown(self):
		return self.Difficulty.getCountDown()

class Easy(Difficulty):
	def __init__(self):
		self.countdown = 300

	def getCountDown(self):
		return self.countdown

class Medium(Difficulty):
	def __init__(self):
		self.countdown = 200

	def getCountDown(self):
		return self.countdown

class Hard(Difficulty):
	def __init__(self):
		self.countdown = 100

	def getCountDown(self):
		return self.countdown