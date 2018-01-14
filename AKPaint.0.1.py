import pygame

RES = (400,400)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

SML = 1
MED = 5
LRG = 10
mPos = 0
mBtn = 0
cur_size = SML

pygame.init()
clock = pygame.time.Clock()



mainSurf = pygame.display.set_mode(RES)
paintSurf = pygame.Surface((RES[0],RES[0] - 25))
toolSurf = pygame.Surface((RES[0],25))
paintSurf.fill(WHITE)
toolSurf.fill(RED)

mainSurf.blit(toolSurf,(0,0))
mainSurf.blit(paintSurf,(0,25))
              


def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def draw_pen(size, color):
    if size == 1:
        paintSurf.set_at(mPos, color)
    else:
        pygame.draw.circle(paintSurf,color,mPos,size)

def initVariables():
    global mPos, mBtn
    mPos = pygame.mouse.get_pos()
    mBtn = (pygame.mouse.get_pressed()[0] == 1)

while True:
    checkQuit()
    initVariables()

    if mBtn:
        draw_pen(SML, BLACK)
    
    pygame.display.update()
            
