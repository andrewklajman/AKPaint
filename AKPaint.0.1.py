import pygame

RES = (400,400)
WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
gd = pygame.display.set_mode(RES)
gd.fill(WHITE)
clock = pygame.time.Clock()

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

while True:
    checkQuit()
    mPos = pygame.mouse.get_pos()
    mBtn = (pygame.mouse.get_pressed()[0] == 1)

    if mBtn:
        pygame.draw.circle(gd,BLACK,mPos,5)
    
    pygame.display.update()
            
