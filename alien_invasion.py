import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_heigh))
	pygame.display.set_caption('外星人入侵')

	#创建一艘飞船
	ship = Ship(ai_setting,screen)

	#创建一个用于存储子弹的编组
	bullets = Group()

	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_event(ai_setting,screen,ship,bullets)

		#每次循环都会更新飞船坐标
		ship.update()

		#更新子弹的位置坐标，删除消失的子弹
		gf.update_bullets(bullets)

		#每次循环都会重绘屏幕
		gf.update_screen(screen,ai_setting,ship,bullets)

		#让最近绘制的屏幕可见
		pygame.display.flip()


run_game()
