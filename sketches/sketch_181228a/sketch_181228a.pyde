"""
Formation Control 
by Anna Lukina
based on
Flocking and Circle Packing
by Daniel Shiffman.    

An implementation of Craig Reynold's Boid to simulate
the flocking behavior of birds going into a Word Formation. Each boid steers itself based on 
rules of avoidance, alignment, and coherence for flocking and clear view, velocity matching.

Click the mouse to add a boid.
"""

from boid import Boid
from flock import Flock

flock = Flock()

palette =  []

def setup():
    global img_element, palette, columns, rows, cellsize, img, explode, frame, word, spots, start_pack, pack, treeGrowth, root, back
    img = loadImage("Head_Hearts.gif")  # Load the image
    back = loadImage("Projektor_1.jpg") # background image
    cellsize = 2  # Dimensions of each cell in the grid
    columns = img.width / cellsize  # Calculate # of columns
    rows = img.height / cellsize  # Calculate # of rows
    frame = 0
    treeGrowth = height / 10 * 0.66
    root = 5
    pack = 1000 # number of elements needed to pack into letters
    start_pack = 500 # frame number from which to start packing
    #frameRate(100)
    
    palette.append('#FFDF0D')
    palette.append('#FF19B7')
    palette.append('#17B200')
    palette.append('#21FF00')
    
    size(1856, 1158, P3D)
    
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
            flock.addBoid(Boid(boid_x, boid_y, img_element[k], palette), word)
    
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
    global img_element, palette, columns, rows, cellsize, img, explode, frame, word, spots, start_pack, pack, treeGrowth, root, back
    background(0)
    #rotateX(PI/9)
    
    # spawn a given word which will join the flock
    if frame > start_pack and frame < pack + start_pack:
        # spawn elements in white pixels of word image
        word = 1
        # pick a random element
        k = int(random(0, len(img_element)))
        # pack an element into a random pixel
        r = int(random(0, len(spots)))
        spot = spots[r]
        # spawn a new boid for formation of letters
        flock.addBoid(Boid(spot.x, spot.y, img_element[k], palette), word)

        # make the word to be stable for a few frames
        flock.run(word)
        
    if frame >= pack + start_pack:
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
                #else:
                    #noLoop()
    
    if frame < pack * 3:
        frame += 1
        word = 0
        flock.run(word)
    if frame >= pack * 3:
        #noLoop()
        gravity = PVector(0, 0.02)
        for b in flock.boids:
            b.applyForce(gravity)
            b.update()
            b.render()
    if frame >= pack * 4:
        noLoop()
        
    # grow a tree
    #if frame <= start_pack:
    #    stroke(255)
    #    strokeWeight(5)
    #    treeGrowth = max(2, treeGrowth * 0.66)
    #    if treeGrowth == 10:
    #        root = min(11, root + 1)
    #        treeGrowth = height / 10 * 0.66
        # Let's pick an angle 0 to 90 degrees based on the mouse position
        #a = (100 / float(width)) * 90
    #    a = 45
        # Convert it to radians
        # Start the tree from the bottom of the screen
    #    translate(root * width / 10, root * height / 10)
        # Draw a line 120 pixels
    #    line(0, 0, 0, -height / 10)
        # Move to the end of that line
    #    translate(0, - height / 10)
        # Start the recursive branching!
    #    branch(height / 10, radians(a))
    #    translate(0, height / 10)
        
        # Draw a line 120 pixels
    #    rotate(PI/2)
    #    line(0, 0, 0, -height / 10)
        # Move to the end of that line
    #    translate(0, - height / 10)
        # Start the recursive branching!
    #    branch(height / 10, radians(a))
    #    translate(0, height / 10)
        
        # Draw a line 120 pixels
    #    rotate(PI/2)
    #    line(0, 0, 0, -height / 10)
        # Move to the end of that line
    #    translate(0, - height / 10)
        # Start the recursive branching!
    #    branch(height / 10, radians(a))
    #    translate(0, height / 10)
        
        # Draw a line 120 pixels
    #    rotate(PI/2)
    #    line(0, 0, 0, -height / 10)
        # Move to the end of that line
    #    translate(0, -height / 10)
        # Start the recursive branching!
    #    branch(height / 10, radians(a))
    #    translate(0, height / 10)
        #rotate(-3*PI/2)
        #translate(- root * width / 10, - root * height / 10)
        noStroke()
    
    #saveFrame("frame_flock-######.png")

# Add a boid into the System
def mousePressed():
    global img_element, word, palette
    flock.addBoid(Boid(mouseX, mouseY, img_element[int(random(0,len(img_element)))], palette), word)
    
def keyPressed():
  if (key == 'q'):
    videoExport.endMovie()
    exit()

def branch(h, theta):
    global treeGrowth
    # Each branch will be 2/3rds the size of the previous one
    h *= 0.66
    # All recursive functions must have an exit condition!!!!
    # Here, ours is when the length of the branch is 2 pixels or less
    if h > treeGrowth:
        # Save the current state of transformation (i.e. where are we now)
        pushMatrix()
        rotate(theta)  # Rotate by theta
        line(0, 0, 0, -h)  # Draw the branch
        translate(0, -h)  # Move to the end of the branch
        branch(h, theta)  # Ok, now call myself to draw two branches!!
        # Whenever we get back here, we "pop" in order to restore the previous
        # matrix state
        popMatrix()
        # Repeat the same thing, only branch off to the "left" this time!
        with pushMatrix():
            rotate(-theta)
            line(0, 0, 0, -h)
            translate(0, -h)
            branch(h, theta)
