import pygame

RES = (400,400)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (100,100,100)
TB_HEIGHT = 25
TB_ICONSIZE = (25,25)

ICN_BGND = WHITE
ICN_OTRBRDR = GRAY
MARKER = 'marker'
FELT = 'felt tip pen'
LINE = 'line'
cur_tool = MARKER
cur_color = WHITE
start_pos = (0,0)

SML = 1
MED = 5
LRG = 10
mPos = 0
mBtn = 0
mPosPaintPrv = 0
mPosPaint = 0
cur_size = SML
pygame.init()
clock = pygame.time.Clock()

mainSurf = pygame.display.set_mode(RES)
paintSurf = pygame.Surface((RES[0],RES[0] - TB_HEIGHT))
toolSurf = pygame.Surface((RES[0],TB_HEIGHT))
colorSurf = pygame.Surface((RES[0],TB_HEIGHT))
paintSurf.fill(WHITE)
colorSurf.fill(WHITE)
toolSurf.fill(RED)

def initVariables():
    global mPos, mBtn, mBtnPrv, mPosPaint,mPosPaintPrv
    mPos = pygame.mouse.get_pos()
    mPosPaintPrv = mPosPaint
    mPosPaint = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - TB_HEIGHT)
    mBtnPrv = mBtn
    mBtn = (pygame.mouse.get_pressed()[0] == 1)

  
def updateScreen():
    mainSurf.blit(toolSurf,(0,0))
    mainSurf.blit(paintSurf,(0,TB_HEIGHT))
    mainSurf.blit(colorSurf,(0,RES[1]-TB_HEIGHT))
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


def populateToolbar():
    toolbar = ['S','M','L','M','F','-']
    [toolSurf.blit(icon(toolbar[n],25),(n * TB_ICONSIZE[0],0)) for n in range(len(toolbar))]
    colors = [WHITE,BLACK,RED]
    [pygame.draw.circle(colorSurf,GRAY,(int((c + 0.5) * TB_HEIGHT),int(0.5 * TB_HEIGHT)),int(0.5 * TB_HEIGHT)) for c in range(len(colors))]
    [pygame.draw.circle(colorSurf,colors[c],(int((c + 0.5) * TB_HEIGHT),int(0.5 * TB_HEIGHT)),int(0.45 * TB_HEIGHT)) for c in range(len(colors))]
    

def icon(text, font_size):
    icn = pygame.Surface(TB_ICONSIZE)
    icn.fill(ICN_BGND)
    txtSurf = pygame.font.SysFont('Consolas', font_size).render(text, True, (BLACK))
    icn.blit(txtSurf, ((TB_ICONSIZE[0] - txtSurf.get_size()[0])/2, (TB_ICONSIZE[1] - txtSurf.get_size()[1])/2))
    return icn

def tbSetting():
    global cur_size, cur_tool
    tbPos = (int(mPos[0]/TB_ICONSIZE[0]),int(mPos[1]/TB_ICONSIZE[1]))
    if mBtn and not(mBtnPrv) and tbPos[1] == 0:
        if tbPos[0] == 0:
            cur_size = SML
        if tbPos[0] == 1:
            cur_size = MED
        if tbPos[0] == 2:
            cur_size = LRG
        if tbPos[0] == 3:
            cur_tool = MARKER
        if tbPos[0] == 4:
            cur_tool = FELT
        if tbPos[0] == 5:
            cur_tool = LINE

def colorSetting():
    global cur_color
    cPos = (int(mPos[0]/TB_ICONSIZE[0]),int(mPos[1]/TB_ICONSIZE[1]))
    if mBtn and not(mBtnPrv) and cPos[1] == 15:
        if cPos[0] == 0:
            cur_color = WHITE
        if cPos[0] == 1:
            cur_color = BLACK
        if cPos[0] == 2:
            cur_color = RED
       

def tlSelection():
    global start_pos
    if mBtn and cur_tool == MARKER:
        draw_pen(cur_size, cur_color)
    if mBtn and cur_tool == FELT:
        pygame.draw.line(paintSurf,cur_color,mPosPaint,(mPosPaint[0] - 5,mPosPaint[1] - 10),cur_size)
    if cur_tool == LINE:
        if mBtn and not(mBtnPrv):
            start_pos = mPosPaint
        if not(mBtn) and mBtnPrv:
            end_pos = mPosPaint
            pygame.draw.line(paintSurf, cur_color, start_pos, end_pos, cur_size)

populateToolbar()
while True:
    checkQuit()
    initVariables()
    tbSetting()
    colorSetting()
    tlSelection()
    updateScreen()
    clock.tick(30)

            
