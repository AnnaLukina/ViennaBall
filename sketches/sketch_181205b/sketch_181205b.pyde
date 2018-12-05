dance = 0
danceStep = 5
danceLimit = 1024
angle = 0
angleChange = 5
angleLimit = 360

def setup():
  global img, back, img_mirror, dance, pic, danceStep, danceLimit, angle, angleChange, angleLimit, couple
  size(723,1024,P3D)
  # Make a new instance of a PImage by loading an image file
  # Declaring a variable of type PImage
  img = loadImage("couple_transparent.png")
  img_mirror = loadImage("couple_mirrored.png")
  back = loadImage("poster.jpg")
  pic = img
  smooth()
  frameRate(30)
  noStroke()

def draw():
  global img, back, img_mirror, dance, pic, danceStep, danceLimit, angle, angleChange, angleLimit, couple
  background(back)
  translate(width / 2, 0, 0)
  #rotateX(map(mouseY, 0, height, -PI, PI))
  #rotateY(map(mouseX, 0, width, -PI, PI))
  # Draw the image to the screen at coordinate (0,0,0)
  pushMatrix()
  couple = createShape(SPHERE, 200)
  couple.setTexture(pic)
  move()
  dance += danceStep
  angle += angleChange
  if (dance > danceLimit or dance < 0):
      dance = 0
      dance += danceStep
  if (angle > angleLimit or angle < 0):
      angle = 0
      angle += angleChange
  popMatrix()

def move():
    global dance, couple, angle
    pushMatrix()
    translate(0, dance, 0)
    rotateY(map(dance, 0, width, -PI, PI))
    shape(couple)
    popMatrix()
  
  
  
