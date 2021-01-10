import pygame, sys
import numpy as np

pygame.init()

# Constants
HEIGHT = 600
WIDTH = 600
BACKGROUND = (0,0,0)
LINE_COLOR = (255,255,255)
ROWS = 3
COLUMN = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
LINE_WIDTH = 20

screen_size = pygame.display.set_mode( (HEIGHT, WIDTH) )
screen_size.fill( BACKGROUND )

board = np.zeros( (ROWS, COLUMN) )

# Tic-tac-toe lines
def lines():
	pygame.draw.line( screen_size, LINE_COLOR, (0, 200), (600, 200), 10 )
	pygame.draw.line( screen_size, LINE_COLOR, (0, 400), (600, 400), 10 )
	pygame.draw.line( screen_size, LINE_COLOR, (200, 0), (200, 600), 10 )
	pygame.draw.line( screen_size, LINE_COLOR, (400, 0), (400, 600), 10 )
lines()

# Tic-tac-toe board logic
def taken_spot(row, col, player_number):
	board[row][col] = player_number

def available_spot(row, col):
	if board[row][col] == 0:
		return True
	else:
		return False

def draw_game():
	for row in range(ROWS):
		for col in range(COLUMN):
			if board[row][col] == 0:
				return False
	return True

def draw_xo():
	for row in range(ROWS):
		for col in range(COLUMN):
			if board[row][col] == 1:
				pygame.draw.circle (screen_size, LINE_COLOR, (int( col * 200 + 100 ), int( row * 200 + 100 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			
			elif board[row][col] == 2:
				pygame.draw.line( screen_size, LINE_COLOR, (col * 200 + 60, row * 200 + 140), (col * 200 + 140, row * 200 + 60), LINE_WIDTH )
				pygame.draw.line( screen_size, LINE_COLOR, (col * 200 + 60, row * 200 + 60), (col * 200 + 140, row * 200 + 140), LINE_WIDTH )

def win_check(player):
	for col in range(COLUMN):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_ver(col,player)
			return True

	for row in range(ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_hor(row,player)
			return True

	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_dia(player)
		return True

	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_dia2(player)
		return True

def draw_ver(col,player):
	pygame.draw.line( screen_size, LINE_COLOR, (col * 200 + 100, 15), (col * 200 + 100, HEIGHT - 15), LINE_WIDTH )

def draw_hor(row,player):
	pygame.draw.line( screen_size, LINE_COLOR, (15, row * 200 + 100), (WIDTH - 15, row * 200 + 100), LINE_WIDTH )

def draw_dia(player):
	pygame.draw.line ( screen_size, LINE_COLOR, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH )

def draw_dia2(player):
	pygame.draw.line( screen_size, LINE_COLOR, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH )

def restart():
	screen_size.fill( BACKGROUND )
	draw.lines()
	player = 1
	for row in range(ROWS):
		for col in range(COLUMN):
			board[row][col] = 0

player = 1
game = False

# Loop to keep the screen running and allow exit
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game:
			x_axis = event.pos[1]
			y_axis = event.pos[0]

			clicked_row = int(x_axis // 200)
			clicked_col = int(y_axis // 200)

			if available_spot(clicked_row, clicked_col):
				if player == 1:
					taken_spot(clicked_row, clicked_col, 1)
					if win_check(player):
						game = True
					player = 2

				elif player == 2:
					taken_spot(clicked_row, clicked_col, 2)
					if win_check(player):
						game = True
					player = 1
				draw_xo()
	if win_check(player) == True:
		restart()
	
	pygame.display.update()