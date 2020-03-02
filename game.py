# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     

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
            ypos-=0.01
        if pressed[pygame.K_s]:
            ypos+=0.01
        if pressed[pygame.K_a]:
            xpos-=0.01
        if pressed[pygame.K_d]:
            xpos+=0.01

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Pressed left")
                if event.key == pygame.K_RIGHT:
                    print("Pressed right")
                if event.key == pygame.K_UP:
                    print("Pressed up")
                if event.key == pygame.K_DOWN:
                    print("Pressed down")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print("The left arrow key was released.")
                if event.key == pygame.K_RIGHT:
                    print("The right arrow key was released.")
                if event.key == pygame.K_UP:
                    print("The up arrow key was released.")
                if event.key == pygame.K_DOWN:
                    print("The down arrow key was released.")
            """


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