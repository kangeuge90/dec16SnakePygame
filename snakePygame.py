import pygame
import time
from pygame.locals import *
# import global variables from pygame
# https://www.pygame.org/docs/ref/locals.html

SIZE = 40 # snake block size

class Apple:
    def __init__( self, parent_screen ):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load('dec16SnakePygame/resources/apple.jpg').convert()
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def draw( self ):
        self.parent_screen.blit( self.apple, ( self.x, self.y ) )
        pygame.display.flip()


class Snake:
    def __init__( self, parent_screen , length=4 ):
        # block_location = "c:/Users/kange/OneDrive/Desktop/Python Work/dec16SnakePygame/resources/block.jpg"
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("dec16SnakePygame/resources/block.jpg").convert() # method of loading our block image
        self.x = [SIZE] * length # trick that creates identical units in an array
        self.y = [SIZE] * length
        # block_x, block_y = 100, 100
        self.direction = ''

    def draw( self ):
        self.parent_screen.fill( ( 110, 110, 5 ) )
        for i in range( self.length ):
            self.parent_screen.blit( self.block, ( self.x[i], self.y[i] ) )
        pygame.display.flip()
    def move_left( self ):
        self.direction = 'left'
        # self.x -= 10
        # self.draw()
    def move_right( self ):
        self.direction = 'right'
        # self.x += 10
        # self.draw()
    def move_up( self ):
        self.direction = 'up'
        # self.y -= 10
        # self.draw()
    def move_down( self ):
        self.direction = 'down'
        # self.y += 10
        # self.draw()
    def walk( self ):

        for i in range( self.length-1, 0, -1 ):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE   
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()



class Game:
    def __init__( self ):
        pygame.init()
        self.surface = pygame.display.set_mode( ( 1000, 800 ) ) 
        # pixel window size x value, y value
        self.surface.fill( ( 92, 25, 84 ) ) # color values to fill window, usng R, G, B, google has RGB generator
        self.snake = Snake( self.surface, 2 )
        self.snake.draw()
        self.apple = Apple( self.surface )
        self.apple.draw()

    def play( self ):
        self.snake.walk()
        self.apple.draw()

    def run( self ):
        running = True

        while running:
        #infinite loop, but we need to cancel it with a key press
        
            for event in pygame.event.get():
                #for this event (key press in this case) do the following:
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE: # If the escape key if pressed
                        running = False # stop running the game
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT: # QUIT is called when you click the X button to close window
                    # elif is python for else if
                    running = False # stop running the game 

            # self.snake.walk()
            # self.apple.draw()
            # moved to play to make easier, don't have to repeat

            self.play

            time.sleep( 0.3 )

# def draw_block(): # draw block using elements from code below
#     game.surface.fill( ( 110, 110, 5 ) ) # needs to re-draw the background to cover up the previous block
#     game.surface.blit( block, ( block_x, block_y ) )
#     pygame.display.flip() # can also use update method, they have slight function differences

if __name__ == "__main__":
    game = Game()
    game.run()

    # OLD CODE MOVED TO CLASSES ------------------------------------
    # block_x = 100
    # block_y = 100
    # game.surface.blit( block, ( block_x, block_y ) ) # blit will draw this image at set location ( image ( x, y ) )

    # pygame.display.flip() # updating screen with color fill value, and other things that are placed
    # OLD CODE MOVED TO CLASSES ------------------------------------

    # time.sleep(5)
    # # timer to check window, testing purposes

    # event loop is waiting for the user input to act
