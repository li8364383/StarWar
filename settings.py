class Settings():
	'''存储所有设置的类'''

	def __init__(self):
		#初始化游戏设置
		#屏幕设置
		self.screen_width = 1200
		self.screen_heigh = 600
		self.bg_color = (0,0,0)
		self.ship_speed_factor = 1.5

		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_heigh = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3
