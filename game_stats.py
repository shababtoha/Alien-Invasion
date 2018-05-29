class GameStats():
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.high_score = 0
		self.reset_stats()
		self.game_active = False
		self.level = 1
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
