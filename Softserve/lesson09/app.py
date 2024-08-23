import pygame


pygame.init()

game_display = pygame.display.set_mode((800,600)) 

pygame.display.set_caption('My first game')
font = pygame.font.SysFont('Calibri', 25, True, False)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

point_list = []

circle = [30, 30]
circle_color = [20, 20, 20]



# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.


# -------- Main Program Loop -----------
while not done:
# --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        # elif event.type == pygame.KEYDOWN:
        #     print("User pressed a key.", event)
        # elif event.type == pygame.KEYUP:
        #     print("User let go of a key.", event)
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("User pressed a mouse button", event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            data = event.dict
            if data.get("button") == 1:
                point_list.append(data.get("pos"))
            elif data.get("button") == 3:
                point_list.pop()

        
    game_display.fill(WHITE)
    # --- Go ahead and update the screen with what we've drawn.
    if len(point_list) > 2:
        pygame.draw.polygon(game_display, (255,0,0), point_list, width=0)

        for point in point_list:
            text = font.render(f"{point}",True,BLACK)
            # Put the image of the text on the screen at 250x250
            game_display.blit(text, point)

    ### cicle start
    # pygame.draw.circle(game_display, circle_color, circle, 10, width=0)
    # if circle[0] < 800 - 30:
    #     circle[0] += 5
    # else:
    #     circle[0] = 30
    #     circle[1] += 20


    # if circle_color[0] < 255:
    #     circle_color[0] += 1
    # else:
    #     circle_color[0] = 0
    #     circle_color[1] += 1
    #     # circle_color[2] += 1

    ### cicle end
    
    
    pygame.display.update()


    # --- Limit to 60 frames per second
    clock.tick(60)

