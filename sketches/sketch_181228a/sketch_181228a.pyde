"""
Formation 
by Anna Lukina
based on
Flocking and Circle Packing
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
    global img_element, columns, rows, cellsize, img, explode, frame, word, spots, start_pack, pack
    img = loadImage("Head_Hearts.gif")  # Load the image
    cellsize = 2  # Dimensions of each cell in the grid
    columns = img.width / cellsize  # Calculate # of columns
    rows = img.height / cellsize  # Calculate # of rows
    frame = 0
    pack = 1000 # number of elements needed to pack into letters
    start_pack = 500 # frame number from which to start packing
    #frameRate(100)
    
    size(1500, 1000, P3D)
    
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
    word = 0
    for k in range(0, len(img_element)):
        # Add an initial set of boids into the system
        boid_x = random(-width / 2, width / 2)
        boid_y = random(-height / 2, height / 2)
        
        for i in range(int(pack / len(img_element))):
            flock.addBoid(Boid(boid_x, boid_y, img_element[k]), word)
    
    # read white pixels of the word image        
    spots = []
    img_word = loadImage("nauka_english.png")
    img_word.resize(width, int(img_word.height * width / img_word.width))
    img_word.loadPixels()
    for x in range(img_word.width):
        for y in range(img_word.height):
            index = x + y * img_word.width
            c = img_word.pixels[index]
            b = brightness(c)
            if b > 1:
                spots.append(PVector(x,y))
   
def draw():
    global img_element, columns, rows, cellsize, img, explode, frame, word, spots, start_pack, pack
    background(0)
    
    # spawn a given word which will join the flock
    if frame > start_pack and frame < pack + start_pack * 2:
        # spawn elements in white pixels of word image
        word = 1
        # pick a random element
        k = int(random(0, len(img_element)))
        # pack an element into a random pixel
        r = int(random(0, len(spots)))
        spot = spots[r]
        # spawn a new boid for formation of letters
        flock.addBoid(Boid(spot.x, spot.y, img_element[k]), word)

        # make the word to be stable for a few frames
        flock.run(word)
    if frame >= pack + start_pack * 2:
        word = 1
        flock.run(word)
    if frame >= pack + start_pack * 2 and flock.letters:
        # make the word join the flock every 100th frame
        if not frame % 100:
            word = 0
            for b in range(100):
                if flock.letters:
                    flock.addBoid(flock.letters[-1], word)
                    del flock.letters[-1]
                else:
                    noLoop()
    
    frame += 1
    word = 0
    flock.run(word)
    if frame == pack * 4:
        noLoop()
    
    #saveFrame("frame-######.png")

# Add a boid into the System
def mousePressed():
    global img_element, word
    flock.addBoid(Boid(mouseX, mouseY, img_element[int(random(0,len(img_element)))]), word)
    
def keyPressed():
  if (key == 'q'):
    videoExport.endMovie()
    exit()
