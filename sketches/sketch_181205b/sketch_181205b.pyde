"""
Staircase 
by Anna Lukina

An implementation of shapes moving down a staircase
Nucleus turning around the dancing couples

"""

traceOrbit = 100
traceOrbit2 = 50
traceOrbit3 = 50
rDancer = 70.0

palette = []
palette1 = []
#palette = ['#FFDF0D', '#FF19B7', '#17B200', '#21FF00']
#palette1 = ['#0C7F05', '#FFDF0D', '#030075', '#13CC07']
xgrid = 0.0
b = random(2.0)

symbolSize = 16
streams = []
fadeInterval = 1.6

xspacing = 0 # How far apart should each horizontal location be spaced
w = 0 # Width of entire wave

theta = PI # Start angle at 0
amplitude = 0.0 # Height of wave
period = 1000.0 # How many pixels before the wave repeats
dx = 0.0 # Value for incrementing Y, a function of period and yspacing
yvalues = [] # Using an array to store height values for the wave

from dancers import Dancers
from electron import Electron
from staircase import Staircase

def setup():
    global frame, back, next_frame, projector, gravity, img_dancers, img_hearts, img_logics, steps, dancers, coolStreams, currentX, electrons, delta, move_x, move_y, move_z, grid, gridDensity, theta, yvalues, amplitude, dx, xspacing
    
    # grid colors
    palette.append('#FFDF0D')
    palette.append('#FF19B7')
    palette.append('#17B200')
    palette.append('#21FF00')
    palette1.append('#0C7F05')
    palette1.append('#FFDF0D')
    palette1.append('#030075')
    palette1.append('#13CC07')
    
    # load all the images
    img_dancers = []
    img_hearts = []
    img_logics = []
    
    img_dancers.append(loadImage("Men_Dancers_PURE.gif"))
    img_dancers.append(loadImage("Red_dancer_PURE.gif"))
    img_dancers.append(loadImage("Lavanda_Dancer_PURE.gif"))
    img_dancers.append(loadImage("Grey_Dancer_PURE.gif"))
    img_dancers.append(loadImage("PINK_Dancer_PURE.gif"))
    img_hearts.append(loadImage("Heart Red.gif"))
    img_hearts.append(loadImage("Heart Gold.gif"))
    img_hearts.append(loadImage("Heart Green.gif"))
    img_logics.append(loadImage("Logic_A.gif"))
    img_logics.append(loadImage("Logic_U.gif"))
    img_logics.append(loadImage("Logic_V.gif"))
    img_logics.append(loadImage("Logic_L.gif"))
    
    for img in img_dancers:
            resize_perc = rDancer / max(img.width, img.height)
            img.resize(int(img.width * resize_perc), int(img.height * resize_perc))
    
    back = loadImage("stone-floor-texture.jpg")
    projector = loadImage("Projektor_1.jpg")
    next_frame = loadImage("frame_cubes-000001.png")
    holo = loadImage("9.jpg")
    size(1856,1158,P3D)
    smooth()
    lights()
    noStroke()
    
    # create the staircase
    steps = Staircase(height, 1000)
    stairs = Staircase(height, 13)
    
    # create nucleus
    electrons = []
    for i in range(3):
        electrons.append(Electron())
        electrons[i].s = 0.0005
        electrons[i].r = 3
    
    # create dancers
    dancers = []
    for i in range(len(img_dancers)):
        core = img_dancers[i]
        dancers.append(Dancers(core))
        
    move_x = -width / 2
    move_y = -height / 2
    move_z = 10
    frame = 0
    
    grid = 2
    gridDensity = 4
    
    xmatrix = 0
    for i in range(0, width / symbolSize):
        stream = Stream()
        stream.generateSymbols(xmatrix, random(-height / 2, 0))
        streams.append(stream)
        xmatrix += symbolSize
  
    textSize(symbolSize)
    
    theFont = createFont("Arial Unicode MS", 20)
    textFont(theFont)
    textAlign(CENTER, TOP)
    coolStreams = []
    for x in range(10, width, 20): # add streams across the width of the screen with text size intervals
        coolStreams.append(CoolStream(x+1.0)) 
    
    # wave parameters
    w = 1640
    xspacing = w / 10
    dx = (TWO_PI / period) * xspacing
    yvalues = [0.0 for y in range(0, w / xspacing)]
    rectMode(CENTER)
    
    gravity = 0.0
        
def draw():
    global frame, projector, img_dancers, img_hearts, img_logics, steps, dancers, coolStreams, currentX, electrons, move_x, move_y, move_z, xgrid, grid, gridDensity, theta, yvalues, amplitude, dx, xspacing
    #background(projector)
    background(0)
    lights()
    #rotateX(map(mouseY, 0, height, -PI, PI))
    #rotateY(map(mouseX, 0, width, -PI, PI))
    #noStroke()
    #noFill()
    translate(width / 2, height / 2, 0)
        
    # wave the steps
    if frameCount < 1400:
        yvalues = calcWave()
    renderWave()
        
    if frameCount < 1400:
        # positions of dancers on the grid
        for d in range(len(dancers) - 4):
            dancers[d].z = -xspacing * 4 + move_x
            dancers[d].y = height / 2 + yvalues[4] - height / 3 #0
            dancers[d].x = -width / 2
            
            dancers[d+1].z = -xspacing * 8 + move_x
            dancers[d+1].y = height / 2 + yvalues[8] - height / 3 #-height/4
            dancers[d+1].x = -width / 2
            
            dancers[d+2].z = 0 - move_x
            dancers[d+2].y = height / 2 + yvalues[0] - height / 3 #height/4
            dancers[d+2].x = width / 2
            
            dancers[d+3].z = -xspacing * 2 - move_x
            dancers[d+3].y = height / 2 + yvalues[2] - height / 3 #height/4
            dancers[d+3].x = width / 2
            
            dancers[d+4].z = -xspacing * 6 - move_x
            dancers[d+4].y = height / 2 + yvalues[6] - height / 3 #height/4
            dancers[d+4].x = width / 2
        
        move_x += 2*dx
        move_y += .01
        
        # dancers on the steps
        for dancer in dancers:
        # draw a nusleus with a dancer inside
        #dancers[0].render(steps.x, -height / 2 + steps.y, steps.y)
            electronsB = []
            electronsT = []
            nucleus = createShape(GROUP)
            angle = [radians(-75), radians(75), radians(0)]
            el_orbit = []
            for i in range(3):
                el_orbit.append(createShape(GROUP))
            
            for electron in electrons:
                electron.setCoords(millis(), traceOrbit, traceOrbit2, traceOrbit3)
                if (electron.overLapping()):
                    electronsB.append(electron)
                else:
                    electronsT.append(electron)
                    
            for i in range(3):
                el = electrons[i].display()
                orbit = printTrace()
                el_orbit[i].addChild(el)
                el_orbit[i].addChild(orbit)
                el_orbit[i].rotate(angle[i])
                nucleus.addChild(el_orbit[i])
                nucleus.rotate(move_y)
            nucleus.translate(dancer.x, dancer.y, dancer.z)
            shape(nucleus)
            
            dance = dancer.display()
            #dance.rotate(move_x)
            shape(dance)
            
            # draw a step
            #steps.update()
            #steps.render()
            #for i in range(13):
            #    stairs.update()
                #stairs.render()
            #saveFrame("frame-######.png")
            
    # start matrix rain
    translate(-width/2, -height/2, -height / 2 + frameCount/10)
    rotateX(PI/7)
    if frameCount >= 300:
        for stream in streams:
            stream.render()
        #for stream in coolStreams:
        #    stream.update(2, 0.001)
        #del coolStreams
        #coolStreams = []
        #for x in range(10, width, 20):
        #    coolStreams.append(CoolStream(x*1.0))
        
    if frameCount > 2000:
        noLoop()
    #saveFrame("frame_matrix-######.png")

class Symbol:
    
    def __init__(self, x, y, speed, first, opacity):
        self.x = x
        self.y = y
        self.value = ''
        
        self.speed = speed
        self.first = first
        self.opacity = opacity

        self.swichInterval = round(random(2, 25))

    def setToRandomSymbol(self):
        charType = round(random(0, 10))
        if (frameCount % self.swichInterval == 0):
            if (charType > 9):
                # set it Katakana but I want to set flip version of Katakana later
                self.value = "LogiCS"#u"".join(map(unichr, (0x30a0, round(random(0, 96)))))
            else:
                self.value = int(random(0, 2))
                
    def rain(self):
        if (self.y < 2*height):
            self.y += self.speed
        #else:
            #self.y = -height / 2
            
class Char:

    def __init__(self, tempX, tempY):
        # CONSTRUCTOR to make an instance
        self.x = tempX
        self.y = tempY
        charType = round(random(1)) # return decimal return 0 or 1 with the round
        if (charType == 0):
            rndChar = int(random(48, 90)) # 0 to Z is 48 to 90
            # char built in func only takes base10
            # character map is in hexadecimal, need to convert
            self.theChar = rndChar
        else: 
            if (charType == 1):
                rndChar = int(random(12449, 12615)) # Katakana 12449-12615
                self.theChar = rndChar
        
    def show(self):
        text(self.theChar, self.x, self.y)

    def getRandomChar(self):
        charType = round(random(1)) # return decimal return 0 or 1 with the round
        if (charType == 0):
            rndChar = int(random(48, 90)) # 0 to Z is 48 to 90
            # char built in func only takes base10
            # character map is in hexadecimal, need to convert
            self.theChar = rndChar
        else: 
            if (charType == 1):
                rndChar = int(random(12449, 12615)) # Katakana 12449-12615
                self.theChar = rndChar
                
class CoolStream:
    
    def __init__(self, tempX):
        self.chars = []
        self.numChar = int(random(10, 30))
        self.speed = random(1, 4)
        self.rndPos = random(0, height)
        self.x = tempX

        # CONSTRUCTOR
        # the y value that the for loop uses is passed through the new Char object
        # the x value comes from the streams parameter (to be used later) 
        # adding from top to bottom, bottom is last element of the array
        for y in range(0, self.numChar*20, 20):  # 20 is text size
            self.chars.append(Char(self.x, y*1.0 + self.rndPos)) # takes 2 float objects

    def update(self, speed, chance):
        # orig    
        #for c in chars:
        for i in range(0, len(self.chars)):  # for every character in the character array
            # how we pick colors
            alph = map(i, 0, len(self.chars)-1, 50, 255) # map scale from 0 to 19 to 50 to 255
            fill(0, 250, 80, alph) # alpha makes the characters fade
            if (i == len(self.chars)-1):
                fill(250, 255, 250)
            self.chars[i].show()

            # move characters
            if (frameCount % speed == 0):
                self.chars[i].y += 20.0 # 20 is size of text
                
            # character stays if size-1 new char
            if (i == len(self.chars)-1):
                self.chars[i].getRandomChar()
            else:
                self.chars[i].theChar = self.chars[i+1].theChar

            # change the characters randomly
            if (random(1) < chance): # probability of the character changing in the stream
                if random(1) < chance / 2:
                    self.chars[i].theChar = "LogiCS"
                else:
                    self.chars[i].getRandomChar() # random chance it changes

        # checks if the stream goes over the window height
        if (self.chars[0].y > height):
            for i in range(0, len(self.chars)):
                self.chars[i].y = ((len(self.chars)-1)-i) * (-20.0)

class Stream:
    
    def __init__(self):
        self.symbols = []
        self.totalSymbols = round(random(5, 200))
        self.speed = random(2, 7)

    def generateSymbols(self, x, y):
        opacity = random(40, 255)
        first = round(random(0, 4)) == 1
        for i in range(0, int(self.totalSymbols)):
            symbol = Symbol(x, y, self.speed, first, opacity)
            symbol.setToRandomSymbol()
            self.symbols.append(symbol)
            y -= symbolSize
            first = False

    def render(self):
        for symbol in self.symbols:
            if symbol.value == "LogiCS":
                fill(250, 255, 250, symbol.opacity)
            else:
                fill(0, 255, 80, symbol.opacity)
            text(symbol.value, symbol.x, symbol.y)
            symbol.rain()
            symbol.setToRandomSymbol()
    
def printTrace():
    # orbit for an electron
    noFill() 
    stroke(255)
    strokeWeight(3)
    orbit = createShape(ELLIPSE, 0, 0, traceOrbit, traceOrbit2)
    orbit.rotateX(-3*PI/4)
    return orbit
    #ellipse(0, 0, traceOrbit, traceOrbit2)
    
def calcWave():
    global theta, yvalues, amplitude, dx
    # Increment theta (try different values for 'angular velocity' here
    theta += 0.08
    if frameCount >= 300:
        amplitude = 30.0
    # For every x value, calculate a z value with sine function
    x = theta
    for i in range(len(yvalues)):
        yvalues[i] = sin(x) * amplitude
        x += dx
    return yvalues

def renderWave():
    global xspacing, yvalues, pelette, palette1, back, gravity, next
    
    pushMatrix()
    # A simple way to draw the wave with a box at each location
    if frameCount > 1400:
        #background(next_frame)
        # start droping the cubes
        gravity += frameCount/100
    translate(-width / 2 + 45, -height / 2 - 260, -1000)
    for x in range(0, len(yvalues)):
        r = random(4)
        s = random(150)
        if (s < 10):
            fill(palette[int(r)])
        else:
            fill(255)
        #translate(xspacing, 0, zvalues[x])
        if frameCount > 1400:
            translate(0, gravity, 0)
        translate(xspacing, yvalues[x], 0)
        for y in range(0, 10):
            translate(0, 120 + y*2, 80 + y*2)
            #translate(0, 0, 100)
            #translate(0, height / 10, 0)
            step = createShape(BOX, xspacing, 70, 200)
            step.setTexture(back)
            step.rotateX(-PI/7)
            shape(step)
            #box(xspacing, height / 15, height / 10)
        translate(0, -1200 - 45*2, -800 - 45*2)
        if frameCount > 1400:
            translate(0, -gravity, 0)
        #translate(0, -height, 0)
    popMatrix()
