
import pygame


pygame.init()


screen_width = 900
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Button Demo')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (204, 102, 0)



#define global variable
clicked = False
#counter = 0

class button():
		
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = (0, 0, 0) #black
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, 255, 255, 255, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, (255, 255, 255) (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



play = button(375, 200, 'Play')
highscore = button(375, 300, 'Play Again?')
info = button(375, 400, 'Info')
quit = button(375, 500, 'Quit')


run = True
while run:

    screen.fill(bg)

    if play.draw_button():
        print('Again')
    if highscore.draw_button():
	    print('aaaaa')
    if info.draw_button():
	    print('Quit')
    if quit.draw_button():
	    print('Quit')
    
	

	#counter_img = font.render(str(counter), True, red)
	#screen.blit(counter_img, (280, 450))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	


    pygame.display.update()


pygame.quit()