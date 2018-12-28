"""
V Formation 
by Anna Lukina
based on
Flocking
by Daniel Shiffman.    

An implementation of Craig Reynold's Boid to simulate
the flocking behavior of birds going into a V Formation. Each boid steers itself based on 
rules of avoidance, alignment, and coherence for flocking and clear view, velocity matching, and upwash benefit for V Formation.

Click the mouse to add a boid.
"""

from boid import Boid
from flock import Flock

flock = Flock()

def setup():
    global img_element, columns, rows, cellsize, img, explode
    img = loadImage("Head_Hearts.gif")  # Load the image
    cellsize = 2  # Dimensions of each cell in the grid
    columns = img.width / cellsize  # Calculate # of columns
    rows = img.height / cellsize  # Calculate # of rows
    explode = 0
    
    size(1000, 2000, P3D)
    
    img_element = []
    img_element.append(loadImage("Heart Red.gif"))
    img_element.append(loadImage("Heart Gold.gif"))
    img_element.append(loadImage("Heart Green.gif"))
    img_element.append(loadImage("Logic_A.gif"))
    img_element.append(loadImage("Logic_L.gif"))
    img_element.append(loadImage("Logic_U.gif"))
    img_element.append(loadImage("Logic_V.gif"))
    textureMode(NORMAL)
    
    # spawn flocks in random places of the image
    for k in range(0, len(img_element)):
        # Add an initial set of boids into the system
        boid_x = random(-img.width / 4, img.width / 4)
        boid_y = random(-img.height / 4, img.height / 4)
        
        for i in range(5):
            flock.addBoid(Boid(boid_x, boid_y, img_element[k]))
   
def draw():
    global img_element, columns, rows, cellsize, img, explode
    background(0)
    explode += 50
    # Begin loop for columns
    #for i in range(columns):
        # Begin loop for rows
     #   for j in range(rows):
     #       x = i * cellsize + cellsize / 2  # x position
     #       y = j * cellsize + cellsize / 2  # y position
     #       loc = x + y * img.width  # Pixel array location
     #       c = img.pixels[loc]  # Grab the color
            # Calculate a z position as a function of mouseX and pixel
            # brightness
     #       z = (explode / float(width)) * brightness(img.pixels[loc]) - 20.0
            # Translate to the location, set fill and stroke, and draw the rect
     #       with pushMatrix():
     #           translate(x + 200, y + 100, z)
     #           fill(c, 204)
     #           noStroke()
     #           rectMode(CENTER)
     #           rect(0, 0, cellsize, cellsize)
                
    # Set up some different colored lights
    #pointLight(51, 102, 126, 35, 40, 36)
    #pointLight(200, 40, 60, -65, -60, -150)
    
    # Raise overall light in scene
    #ambientLight(70, 70, 10)
    flock.run()

# Add a boid into the System
def mousePressed():
    global img_element
    flock.addBoid(Boid(mouseX, mouseY, img_element[int(random(0,len(img_element)))]))
