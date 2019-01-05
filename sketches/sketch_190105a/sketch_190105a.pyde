"""
Watch your step 
by Anna Lukina

An implementation of moving staircase

"""

from tile import Tile

def setup():
    global tiles, tileW, tileH, myKey, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT, enabled, img_dancers, img_hearts_logics
    size(1500, 1000, P3D)
    rectMode(CENTER)
    strokeWeight(2)
    stroke(0)
    fill(60)
    
    nbTilesW = 10
    nbTilesH = 14
    gapW = 4
    gapH = 4
    TILE_WIDTH = 100
    TILE_HEIGHT = 1000/13
    tileW = TILE_WIDTH
    tileH = TILE_HEIGHT
    enabled = 1
    myKey = ''
    tiles = [[0 for x in range(nbTilesH)] for y in range(nbTilesW)] 

    # load all the images
    img_dancers = []
    img_hearts_logics = []
    
    img_dancers.append(loadImage("Men_Dancers_PURE.gif"))
    img_dancers.append(loadImage("Red_dancer_PURE.gif"))
    img_dancers.append(loadImage("Lavanda_Dancer_PURE.gif"))
    img_dancers.append(loadImage("Grey_Dancer_PURE.gif"))
    img_dancers.append(loadImage("PINK_Dancer_PURE.gif"))
    img_hearts_logics.append(loadImage("Heart Red.gif"))
    img_hearts_logics.append(loadImage("Heart Gold.gif"))
    img_hearts_logics.append(loadImage("Heart Green.gif"))
    img_hearts_logics.append(loadImage("Logic_A.gif"))
    img_hearts_logics.append(loadImage("Logic_U.gif"))
    img_hearts_logics.append(loadImage("Logic_V.gif"))
    img_hearts_logics.append(loadImage("Logic_L.gif"))
    
    #for img in img_dancers:
    #    scale(0.5)
    #for img in img_hearts:
    #    scale(0.2) 
    #for img in img_logics:
    #    scale(0.2)
    
    initialize()

def initialize():
    global tiles, tileW, tileH, myKey, enabled, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT, img_dancers, img_hearts_logics
    myKey = key
    totalW = (tileW + gapW) * nbTilesW - gapW
    totalH = (tileH + gapH) * nbTilesH - gapH
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            ind_dancer = int(random(0, len(img_dancers)))
            ind_logic = int(random(0, len(img_hearts_logics)))
            tiles[i][j] = Tile(i*(tileW + gapW)-totalW/2, map(j, 0, nbTilesH, 0, totalH)-totalH/2, i, j, tileW, tileH, enabled, img_dancers[ind_dancer], img_hearts_logics[ind_logic])
    
def draw():
    global tiles, tileW, tileH, myKey, enabled, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT
    lights()
    if myKey == CODED:
        if keyCode == UP:
            tileH += 2
            initialize()
        if keyCode == DOWN:
            tileH -= 2
            initialize()
        if keyCode == RIGHT:
            tileW += 2
            initialize()
        if keyCode == LEFT:
            tileW -= 2
            initialize()
        if keyCode == SHIFT:
            enabled = not enabled
    
        tileW = constrain(tileW, 15, width/2)
        tileH = constrain(tileH, 15, height/2)
    else:
        if (myKey == ENTER or myKey == RETURN): 
            tileW = TILE_WIDTH
            tileH = TILE_HEIGHT
            initialize()

    myKey = chr(0)

    background(0)
    translate(width/2, height/2)
    strength = PVector(mouseX-pmouseX, mouseY-pmouseY)
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            tiles[i][j].process(tiles, mouseX, mouseY, strength, nbTilesW, nbTilesH)
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            tiles[i][j].display(tileW, tileH)
    #saveFrame("frame-######.png")

def keyPressed():
    global myKey
    # make sure that keys are taken into account BEFORE a loop starts
    myKey = key