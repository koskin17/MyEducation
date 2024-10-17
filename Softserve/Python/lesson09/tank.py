import pygame
# from pygame import Rect

pygame.init()

game_display = pygame.display.set_mode((800,600)) 

pygame.display.set_caption('My tank game')


done = False
clock = pygame.time.Clock()
STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

tank_icon_base = pygame.image.load("\\Softserve\\lesson09\\tank.png")
tank_size = (50, 50)
tank_icon = pygame.transform.scale(tank_icon_base, tank_size)
tank_pos = [50, 50]
target_pos= [600, 100]
arm = None

keys_down = []
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
        elif event.type == pygame.KEYDOWN:
            print(event)
            key = event.dict.get("key")
            if key in (1073741906, 1073741903, 1073741905, 1073741904):
                keys_down.append(key)
            if key == 32:
                arm = [tank_pos[0]+25, tank_pos[1]+25]

            # match key:
            #     case 1073741906:
            #         tank_pos[1] -= STEP
            #     case 1073741903:
            #         tank_pos[0] += STEP
            #     case 1073741905:
            #         tank_pos[1] += STEP
            #     case 1073741904:
            #         tank_pos[0] -= STEP
        elif event.type == pygame.KEYUP:
            key = event.dict.get("key")
            if key in keys_down:
                keys_down.remove(key)
            # match key:
            #     case 1073741906:
            #         tank_pos[1] -= STEP
            #     case 1073741903:
            #         tank_pos[0] += STEP
            #     case 1073741905:
            #         tank_pos[1] += STEP
            #     case 1073741904:
            #         tank_pos[0] -= STEP

    for key in keys_down:
        match key:
                case 1073741906:
                    if tank_pos[1] > STEP:
                        tank_pos[1] -= STEP
                case 1073741903:
                    if tank_pos[0] < 800 - tank_size[1]:
                        tank_pos[0] += STEP
                case 1073741905:
                    if tank_pos[1] < 600 - tank_size[1]:
                        tank_pos[1] += STEP
                case 1073741904:
                    if tank_pos[0] > 0:
                        tank_pos[0] -= STEP
    
    
    game_display.fill(WHITE)
    
    
    if arm:
        if arm[0] < 800:
            arm[0] += 10
            pygame.draw.circle(game_display, BLACK, arm, 3, width=0)
        else:
            arm = None
    if target_pos:
        pygame.draw.rect(game_display, BLACK, Rect(*target_pos, 20, 20), width=0)
    if arm and target_pos:
        if arm and target_pos[0]-5 <= arm[0] <= target_pos[0] +25 and target_pos[1]-5 <= arm[1] <= target_pos[1] +25:
            print("test")
            target_pos = None

    game_display.blit(tank_icon, tank_pos )
    pygame.display.update()


    clock.tick(60)

