import pygame

class Ship():

	def __init__(self,ai_setting,screen,):
		#初始化飞船并设置初始位置
		self.screen = screen
		self.ai_setting = ai_setting

		#加载飞船图像并获取其外接矩形
		self.image = pygame.transform.scale(pygame.image.load('images/ship.bmp'),(60,60))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = self.rect.centerx
		#移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
			# self.rect.centerx += 1.5
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_setting.ship_speed_factor
			# self.rect.centerx -= 1.5
		self.rect.centerx = self.center

	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image,self.rect)