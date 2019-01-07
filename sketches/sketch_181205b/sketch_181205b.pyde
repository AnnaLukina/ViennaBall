"""
Staircase 
by Anna Lukina

An implementation of shapes moving down a staircase
Nucleus turning around the dancing couples

"""

traceOrbit = 200
traceOrbit2 = 100
traceOrbit3 = 100
rDancer = 100.0

from dancers import Dancers
from electron import Electron
from staircase import Staircase

def setup():
    global frame, img_dancers, img_hearts, img_logics, steps, dancers, stairs, electrons, move_x, move_y, move_z
    
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
    
    back = loadImage("stairs_11.jpg")
    holo = loadImage("9.jpg")
    size(1500,1000,P3D)
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
        electrons[i].s = 0.002
        electrons[i].r = 10
    
    # create dancers
    dancers = []
    for i in range(len(img_dancers)):
        core = img_dancers[int(random(0, len(img_dancers)))]
        dancers.append(Dancers(core))
        
    move_x = -width / 2
    move_y = -height / 2
    move_z = -100
        
def draw():
    global frame, img_dancers, img_hearts, img_logics, steps, dancers, stairs, electrons, move_x, move_y, move_z
    background(0)
    translate(width / 2, height / 2, 0)
    #rotateX(map(mouseY, 0, height, -PI, PI))
    #rotateY(map(mouseX, 0, width, -PI, PI))
    #noStroke()
    #noFill()
    electronsB = []
    electronsT = []
    nucleus = createShape(GROUP)
    angle = [radians(-75), radians(75), radians(0)]
    el_orbit = []
    for i in range(3):
        el_orbit.append(createShape(GROUP))
    move_x += electrons[0].s
    
    # dancers on the steps
    #for dancer in dancers:
    # draw a nusleus with a dancer inside
    #dancers[0].render(steps.x, -height / 2 + steps.y, steps.y)
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
        nucleus.rotate(move_x)
    shape(nucleus)
    
    dance = dancers[0].display(0, 0, 1)
    dance.rotate(move_x)
    shape(dance)
        
        # draw a step
        #steps.update()
        #steps.render()
        #for i in range(13):
        #    stairs.update()
            #stairs.render()
        #saveFrame("frame-######.png")
    
def printTrace():
    # orbit for an electron
    noFill() 
    stroke(255)
    strokeWeight(5)
    orbit = createShape(ELLIPSE, 0, 0, traceOrbit, traceOrbit2)
    orbit.rotateX(3*PI/4)
    return orbit
    #ellipse(0, 0, traceOrbit, traceOrbit2)
