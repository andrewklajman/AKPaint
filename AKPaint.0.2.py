import pygame

RES = (400,400)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (100,100,100)
TB_HEIGHT = 25
TB_ICONSIZE = (22,22)

ICN_BGND = WHITE
ICN_OTRBRDR = GRAY

SML = 1
MED = 5
LRG = 10
mPos = 0
mBtn = 0
cur_size = SML

pygame.init()
clock = pygame.time.Clock()

mainSurf = pygame.display.set_mode(RES)
paintSurf = pygame.Surface((RES[0],RES[0] - TB_HEIGHT))
toolSurf = pygame.Surface((RES[0],TB_HEIGHT))
paintSurf.fill(WHITE)
toolSurf.fill(RED)
  
def updateScreen():
    mainSurf.blit(toolSurf,(0,0))
    mainSurf.blit(paintSurf,(0,TB_HEIGHT))
    pygame.display.update()

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def draw_pen(size, color):
    if size == 1:
        paintSurf.set_at(mPosPaint, color)
    else:
        pygame.draw.circle(paintSurf,color,mPosPaint,size)

def initVariables():
    global mPos, mBtn, mPosPaint
    mPos = pygame.mouse.get_pos()
    mPosPaint = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - TB_HEIGHT)
    mBtn = (pygame.mouse.get_pressed()[0] == 1)

def populateToolBar():
    font = pygame.font.SysFont('comicsansms', 20)
    text = font.render('+', True, (BLACK))
    icons = [text]
    toolSurf.blit(text,(0,0))

def icon():
    font = pygame.font.SysFont('Calibri', 33)
    icn = pygame.Surface(TB_ICONSIZE)
    icn.fill(ICN_BGND)
    pygame.draw.rect(icn,ICN_OTRBRDR,(0,0,TB_ICONSIZE[0],TB_ICONSIZE[1]),1)

    text = font.render('+', True, (BLACK))
    hgtAdj = int((text.get_size()[1] - TB_ICONSIZE[1]) / -2)
    icn.blit(text,(0,+hgtAdj))

    paintSurf.blit(icn,(100,100))


    pygame.draw.rect(paintSurf,ICN_OTRBRDR,(200,200,TB_ICONSIZE[0],TB_ICONSIZE[1]),1)
    paintSurf.blit(text,(200,200+hgtAdj))




##
##
##
##    paintSurf.blit(text,(100,100))
##    pygame.draw.rect(paintSurf,ICN_OTRBRDR,(100,100,text.get_size()[0],text.get_size()[1]),1)
##    print(text.get_size())
    
icon()
while True:
    checkQuit()
    initVariables()
    updateScreen()

    if mBtn:
        draw_pen(LRG, BLACK)

            
