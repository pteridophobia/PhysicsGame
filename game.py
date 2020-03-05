# import the pygame module, so you can use it
import pygame
import random
import math

SIZE = (1280, 720)

class agentObj():
    def __init__(self):
        size = [random.uniform(0, SIZE[i] - 1) for i in range(2)]
        velocity = 0.0
        acceleration = 0.0
        direction = 0.0 #radians
        # pi/2 = 90degrees
        # set to 90 is: self.direction = math.pi / 2

        x_pos = 50
        y_pos = 50
        mass = 0.0
        def getForce(self):
            return ((0.5 * self.mass * (self.velocity * self.velocity))/2)

        def getVelocity(self):
            return self.velocity + self.acceleration

        def getDirection(self):
            return direction * (math.pi / 180)

        def move(self):
            self.x_pos += math.sin(self.getDirection) * self.getVelocity()
            self.y_pos -= math.cos(self.getDirection) * self.getVelocity()
        
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    #agent.move()
    #agent.display()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    player = agentObj()
    player.direction

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
    screen.fill((252,252,252)) #order matters here. Background first means its behind what comes next
    #screen.blit(logo, (0,0)) #use a background image here. the image should be as big or biger than the window
 

    #the next linewill make all pixels matching the defined colo transparant
    #logo.set_colorkey((255,255,255))

    #set alpha value
    logo.set_alpha(128)

    xpos = 50
    ypos = 50

    step_x = 10
    step_y = 10

    screen_width = 240
    screen_height = 180


    screen.blit(logo, (xpos,ypos)) 

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
#write the background over everything
        screen.fill((252,252,252))

        screen.blit(logo, (xpos,ypos)) 
        pygame.display.flip()
        # check if the smiley is still on screen, if not change direction
        #if xpos>screen_width-64 or xpos<0:
        #    step_x = -step_x
        #if ypos>screen_height-64 or ypos<0:
        #    step_y = -step_y
        # update the position of the smiley
        #xpos += step_x # move it to the right
        #ypos += step_y # move it down



        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            player.acceleration += 0.005
            if player.direction < 90:
                player.direction += 10
            elif player.direction > 90 and player.direction < 270:
                player.direction -= 10
            elif player.direction > 269:
                player.direction += 10

            if player.direction >= 360:
                player.direction -= 360

        if pressed[pygame.K_s]:
            player.acceleration += 0.005
            if player.direction < 270 and player.direction > 89:
                player.direction += 10
            elif player.direction > 270:
                player.direction -= 10
            elif player.direction < 90:
                player.direction -= 10

            if player.direction >= 360:
                player.direction -= 360

        if pressed[pygame.K_a]:
            player.acceleration += 0.005
            xpos-=0.01
        if pressed[pygame.K_d]:
            player.acceleration += 0.005
            xpos+=0.01

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            # only do something if the event is of type QUIT
            #key=pygame.key.get_pressed()
            #if key[pygame.K_w]:  ypos-=step_y
            #if key[pygame.K_a]:  xpos-=step_x
            #if key[pygame.K_s]:  ypos+=step_y
            #if key[pygame.K_d]:  xpos+=step_x
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()