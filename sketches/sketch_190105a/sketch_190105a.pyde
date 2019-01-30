"""
Watch your step 
by Anna Lukina

An implementation of the cubes releasing the logical symbols

"""

palette = []
palette1 = []
deep = 0

from tile import Tile

def setup():
    global back, staircase, tiles, tileW, tileH, myKey, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT, enabled, img_vcla, img_hearts_logics, VCLA
    size(1856, 1158, P3D)
    rectMode(CENTER)
    #strokeWeight(2)
    
    # grid colors
    palette.append('#FFDF0D')
    palette.append('#FF19B7')
    palette.append('#17B200')
    palette.append('#21FF00')
    palette1.append('#0C7F05')
    palette1.append('#FFDF0D')
    palette1.append('#030075')
    palette1.append('#13CC07')
    
    #stroke(0)
    #fill(60)
    
    nbTilesW = 6
    nbTilesH = 9
    gapW = 80.0
    gapH = 1.0
    TILE_WIDTH = 80.0
    TILE_HEIGHT = 80.0
    tileW = TILE_WIDTH
    tileH = TILE_HEIGHT
    enabled = False #True
    myKey = chr(0)
    VCLA = 0
    tiles = [[0 for x in range(nbTilesH)] for y in range(nbTilesW)] 

    # load all the images
    img_dancers = []
    img_hearts_logics = []
    img_vcla = []
    resize_perc = 0
    deep = 0
    
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
    img_vcla.append(loadImage("VCLA_V.gif"))
    img_vcla.append(loadImage("Logic_U.gif"))
    img_vcla.append(loadImage("VCLA_L.gif"))
    img_vcla.append(loadImage("VCLA_A.gif"))
    
    back = loadImage("stone-floor-texture.jpg")
    staircase = loadImage("Projektor_1.jpg")
    
    for img in img_vcla:
        resize_perc = TILE_WIDTH / max(img.width, img.height)
        img.resize(int(img.width * resize_perc), int(img.height * resize_perc))
    for img in img_hearts_logics:
        resize_perc = TILE_WIDTH / max(img.width, img.height)
        img.resize(int(img.width * resize_perc), int(img.height * resize_perc)) 
    
    initialize()

def initialize():
    global back, tiles, tileW, tileH, myKey, enabled, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT, img_vcla, img_hearts_logics, VCLA
    #myKey = key
    totalW = (tileW + gapW) * nbTilesW - gapW
    totalH = (tileH + gapH) * nbTilesH - gapH
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            ind_logic = int(random(0, len(img_hearts_logics)))
            tiles[i][j] = Tile(i*(tileW + gapW)-totalW/3, map(j, 0, nbTilesH, 0, totalH)-totalH+j*tileH-tileH, j*(tileH+j*5)-1100, i, j, tileW, tileH, enabled, img_hearts_logics[ind_logic])
    
def draw():
    global back, staircase, tiles, tileW, tileH, myKey, enabled, nbTilesW, nbTilesH, gapW, gapH, TILE_WIDTH, TILE_HEIGHT, VCLA, img_vcla, deep
    #background(staircase)
    background(0)
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

    #background(0)
    
    # drop the cubes
    translate(width/2, height/2, deep)
    if frameCount > 1500:
        gravity = PVector(0, 0.01)
        for i in range(nbTilesW):
            for j in range(nbTilesH):
                if frameCount == 1501:
                    tiles[i][j].velocity = PVector(0, sin(radians(random(0, 90)))/5)
                tiles[i][j].velocity.add(gravity)
                tiles[i][j].x += tiles[i][j].velocity.x
                tiles[i][j].y += tiles[i][j].velocity.y
                tiles[i][j].z += tiles[i][j].velocity.y
    strength = PVector(3.0, 3.0)#PVector(mouseX-pmouseX, mouseY-pmouseY)

    if frameCount == 1000:
        VCLA = 1
        strength = PVector(300.0, 300.0)
        del tiles[1][6].img[-1]
        del tiles[2][6].img[-1]
        del tiles[3][6].img[-1]
        del tiles[4][6].img[-1]
        tiles[1][6].img.append(img_vcla[0])
        tiles[2][6].img.append(img_vcla[1]) 
        tiles[3][6].img.append(img_vcla[2])
        tiles[4][6].img.append(img_vcla[3])
    
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            if VCLA:
                if j == 6 and i >= 1 and i <= 4:
                    cubeX = width / 2 + tiles[i][j].x
                    cubeY = height / 2 + tiles[i][j].y
                    tiles[i][j].process(tiles, cubeX, cubeY, strength, nbTilesW, nbTilesH)
            s = random(500)
            if s < 100:
                cubeX = random(0, width)
                cubeY = random(0, height)
                tiles[i][j].process(tiles, cubeX, cubeY, strength, nbTilesW, nbTilesH)
    for i in range(nbTilesW):
        for j in range(nbTilesH):
            if VCLA and j == 6 and i >= 1 and i <= 4:
                tiles[i][j].display(tileW, tileH, VCLA, palette, back)
            else:
                tiles[i][j].display(tileW, tileH, 0, palette, back)
 
    if frameCount >= 2200:
        noLoop()   
    #saveFrame("frame_cubes-######.png")

def keyPressed():
    global myKey
    # make sure that keys are taken into account BEFORE a loop starts
    myKey = key
