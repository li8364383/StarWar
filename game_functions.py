import sys
import pygame
from bullet import Bullet

def check_keydown_event(event,ai_setting,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(bullets,ai_setting,screen,ship)
	elif event.key == pygame.K_q:
		sys.exit() #按q键退出


def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_event(ai_setting,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ai_setting,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)

def update_screen(screen,ai_setting,ship,bullets):
	# 每次循环都会重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()

def update_bullets(bullets):
	bullets.update()
	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(bullets,ai_setting,screen,ship):
	# 创建子弹
	if len(bullets) < ai_setting.bullet_allowed:
		new_bullet = Bullet(ai_setting,screen,ship)
		bullets.add(new_bullet)
