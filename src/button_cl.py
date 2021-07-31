import pygame

class button():
		
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = (0, 0, 0) #black
	width = 180
	height = 70


	def __init__(self, x, y, text, game):
		self.x = x
		self.y = y
		self.text = text
		self.game = game
		self.clicked = False

	def draw_button(self):

		#global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				self.clicked = True
				pygame.draw.rect(self.game.win, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
				self.clicked = False
				action = True
			else:
				pygame.draw.rect(self.game.win, self.hover_col, button_rect)
		else:
			pygame.draw.rect(self.game.win, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(self.game.win, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(self.game.win, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(self.game.win, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(self.game.win, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = self.game.font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		self.game.win.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action