import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''一个对飞船发射进行管理的类'''
	def __init__(self,ai_setting,screen,ship):
		#在飞船所处位置创建一个子弹对象
		super(Bullet, self).__init__()
		self.screen = screen

		#在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_heigh)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor




	