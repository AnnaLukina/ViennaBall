"""
Staircase 
by Anna Lukina

An implementation of shapes moving down a staircase

"""

from dancers import Dancers
from staircase import Staircase

def setup():
  global frame, img_dancers, img_hearts, img_logics, steps, dancers, stairs
  
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
      scale(0.5)
  for img in img_hearts:
      scale(0.2) 
  for img in img_logics:
      scale(0.2)
  
  back = loadImage("stairs_11.jpg")
  holo = loadImage("9.jpg")
  size(1500,1000,P3D)
  smooth()
  lights()
  noStroke()
  
  # create the staircase
  steps = Staircase(height, 1000)
  stairs = Staircase(height, 13)
  
  dancers = []
  # create dancing couples
  for i in range(len(img_dancers)):
      core = img_dancers[int(random(0, len(img_dancers)))]
      dancers.append(Dancers(core))

def draw():
  global frame, img_dancers, img_hearts, img_logics, steps, dancers, stairs
  background(0)
  translate(width / 2, height / 2, 0)
  #rotateX(map(mouseY, 0, height, -PI, PI))
  #rotateY(map(mouseX, 0, width, -PI, PI))
  #noStroke()
  #noFill()
  
  # dancers on the steps
  if frame < 100:
    # draw a random dancing couple
    dancers[0].render(steps.x, -height / 2 + steps.y, steps.y)
    # draw a step
    steps.update()
    #steps.render()
    for i in range(13):
        stairs.update()
        stairs.render()
    saveFrame("frame-######.png")
  else:
    noLoop()
