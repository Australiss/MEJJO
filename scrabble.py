import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
#colours
black = (0,0,0)
white = (255,255,255)
red = (185,0,0)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green =(0,255,0)



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MEJJO Scrabble')
clock = pygame.time.Clock()



def quit_Game():
    pygame.quit()
    quit()

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None): #message,X co-ord,Y co-ord,Width,Height,Inactive colour, Active Colour, action
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action =='play':
                game_loop()
            #elif action == 'highscore'
                #highscore()
            #elif action == 'dictionary'
                #dictionary()
            #elif action == 'profile_leaderboard'
               #profile_leaderboard()
            elif action == "quit":
                quit_Game()


    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)







#PAUSE FUNCTION
#def paused():
   ## TextSurf, TextRect = text_objects("Paused", largeText)
    #TextRect.center = ((display_width / 2), (display_height / 2))
    #gameDisplay.blit(TextSurf, TextRect)

    #while pause:
        #for event in pygame.event.get():

            #if event.type == pygame.QUIT:
                #pygame.quit()
                #quit()

        # gameDisplay.fill(white)


        #button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
       # button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

       # pygame.display.update()
       # clock.tick(15)

def game_mainmenu():
    mainmenu = True

    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("MEJJO SCRABBLE", largeText)
        TextRect.center = ((display_width / 2), (display_height / 3))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 350, 280, 160, 40, green, bright_green,"start")
        button("HIGHSCORES", 350, 330, 160, 40, green, bright_green,)#FUNCTION GOES HERE)
        button("DICTIONARY", 350, 380, 160, 40, green, bright_green,)#FUNCTION GOES HERE)
        button("LEADERBOARD",350,430,160,40,green,bright_green,)#FUNCTION GOES HERE)
        button("PROFILE", 350, 480, 160, 40, green, bright_green, )#FUNCTION GOES HERE)
        button("QUIT", 350, 530, 160, 40, red, bright_red, "quit")
        pygame.display.update()
        clock.tick(60)


def game_loop():


    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        pygame.display.update()
        clock.tick(60)


game_mainmenu()
game_loop()
quit_Game()

#def main():

    #Board render

    #scores/ Timer

    #Last event log

    #Enter text area

    #Total tiles remaining



#Parse commands
#def commands():
    #how many players
    #player names for scoreboard
    #player provided dictionary
        #add word to dictionary
    #new game
    #viewhighscore
    #make move(B3:B8-WORD)
        #Preview move
        #confirm move (really?)
    #get new tiles/ shuffle
        #nominate how many


    #Check word
        #check dictionary
        #calculate point value

    #Quit game
        #Display highscore table
        #wait for player command
            #new game
            #quit
#def logic():
    #game rules
        #permissible moves
        #bonus points
    #turn based
