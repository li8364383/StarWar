import sys
import pygame

def check_keydown_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_event(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)

def update_screen(screen,ai_setting,ship):
	# 每次循环都会重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.blitme()
