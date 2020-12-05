import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_heigh))
	pygame.display.set_caption('外星人入侵')

	ship = Ship(ai_setting,screen)

	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_event(ship)

		#每次循环都会更新飞船坐标
		ship.update()

		#每次循环都会重绘屏幕
		gf.update_screen(screen,ai_setting,ship)
		# screen.fill(ai_setting.bg_color)
		# ship.blitme()

		#让最近绘制的屏幕可见
		pygame.display.flip()


run_game()
