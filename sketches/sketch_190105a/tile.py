# class of each step of the stairs
class Tile:
    
    def __init__(self, p_x, p_y, p_i, p_j, tileW, tileH, enabled, img_dancer, img_heart_logic):
        self.img = []
        self.img.append(img_dancer)
        self.img.append(img_heart_logic)
        # position
        self.x = p_x
        self.y = p_y
        self.dr = PVector(0, 0) # delta rotation
        self.othersImpact = PVector(0, 0)
        self.r = PVector(0, 0) # rotation
        self.mouseImpacted = False
        self.enabled = enabled
        self.i = p_i
        self.j = p_j
        self.X = self.x + width/2 - tileW/2
        self.Y = self.y + height/2 - tileH/2
        # position on screen
        self.minXY = PVector(screenX(self.X, self.Y, 0), screenY(self.X, self.Y, 0))
        self.maxXY = PVector(screenX(self.X + tileW, self.Y + tileH, 0), screenY(self.X + tileW, self.Y + tileH, 0))

    def process(self, tiles, p_mX, p_mY, p_strength, nbTilesW, nbTilesH):
        if (self.minXY.x < p_mX and p_mX < self.maxXY.x and self.minXY.y < p_mY and p_mY < self.maxXY.y):
            self.dr.x = map(p_strength.y, -15, 15, PI/2, -PI/2)
            self.dr.y = map(p_strength.x, -15, 15, -PI/4, PI/4)
        if (self.enabled):
            self.mouseImpacted = True
            self.processNeighbors(tiles, self.dr.get(), nbTilesW, nbTilesH)
      
    def processNeighbors(self, tiles, p_strength, nbTilesW, nbTilesH):
        l_strength = p_strength.get()
        if (not self.mouseImpacted):
            self.othersImpact.add(l_strength)
        if (l_strength.mag() > 0.1):
            l_strength.mult(0.12)
            if (self.i > 0): 
                tiles[self.i-1][self.j].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # left tile
            if (self.i < nbTilesW-1):
                tiles[self.i+1][self.j].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # right tile
            if (self.j > 0):
                tiles[self.i][self.j-1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # top tile
            if (self.j < nbTilesH-1):
                tiles[self.i][self.j+1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # bottom tile
            l_strength.mult(.6)
            if (self.i > 0 and self.j > 0):
                tiles[self.i-1][self.j-1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # corner top left tile
            if (self.i < nbTilesW-1 and self.j > 0): 
                tiles[self.i+1][self.j-1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # corner top right tile
            if (self.i > 0 and self.j < nbTilesH-1): 
                tiles[self.i-1][self.j+1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # corner bottom left tile
            if (self.i < nbTilesW-1 and self.j < nbTilesH-1): 
                tiles[self.i+1][self.j+1].processNeighbors(tiles, l_strength, nbTilesW, nbTilesH) # corner bottom right tile

    def display(self, tileW, tileH, VCLA):
        self.dr.add(self.othersImpact)
        self.r.add(self.dr)
        self.r.mult(0.9)
        rectMode(CENTER)

        fill(color(map(self.r.x, 0, PI/4, 210, 0), map(self.r.y, 0, PI/4, 210, 0), 210))

        pushMatrix()
        translate(self.x, self.y)
        rotateX(self.r.x)
        #rotateY(self.r.y)
        box(tileW, tileH, min(tileW, tileH)/2)
        noFill()
        noTint()
        noStroke()
        textureMode(NORMAL)
        beginShape()
        texture(self.img[1])
        # Front face.
        vertex(-self.img[1].width/2,
        -self.img[1].height/2,
        min(tileW, tileH)/4,
        0, 0)
        vertex(self.img[1].width/2,
        -self.img[1].height/2,
        min(tileW, tileH)/4,
        1, 0)
        vertex(self.img[1].width/2,
        self.img[1].height/2,
        min(tileW, tileH)/4,
        1, 1)
        vertex(-self.img[1].width/2,
        self.img[1].height/2,
        min(tileW, tileH)/4,
        0, 1)
        endShape()
        if VCLA:
            k = 1
        else:
            k = 0
        beginShape()
        texture(self.img[k])
        # Back face.
        vertex(-self.img[k].width/2,
        -self.img[k].height/2,
        -min(tileW, tileH)/4,
        1, 1)
        vertex(self.img[k].width/2,
        -self.img[k].height/2,
        -min(tileW, tileH)/4,
        0, 1)
        vertex(self.img[k].width/2,
        self.img[k].height/2,
        -min(tileW, tileH)/4,
        0, 0)
        vertex(-self.img[k].width/2,
        self.img[k].height/2,
        -min(tileW, tileH)/4,
        1, 0)
        endShape()
        popMatrix()
    
        self.othersImpact = PVector(0, 0)
        self.mouseImpacted = False
