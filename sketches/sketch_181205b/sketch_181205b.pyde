dance = 0
danceStep = 100
danceLimit = 4032
ang = 0.0
frame = 0

def setup():
  global frame, img, img_heart_red, img_heart_gold, img_atom, img_logic_A, back, dance, danceStep, danceLimit, couple, ang
  # Make a new instance of a PImage by loading an image file
  # Declaring a variable of type PImage
  img_MM = loadImage("Men_Dancers_PURE.gif")
  img_MM.resize(200,200)
  img = loadImage("Red_dancer_PURE.gif")
  img.resize(200,200)
  img_FM = loadImage("Lavanda_Dancer_PURE.gif")
  img_FM.resize(200,200)
  img_FF = loadImage("Grey_Dancer_PURE.gif")
  img_FF.resize(200,200)
  img_MF = loadImage("PINK_Dancer_PURE.gif")
  img_MF.resize(200,200)
  img_heart_red = loadImage("Heart Red.gif")
  img_heart_red.resize(50,50)
  img_heart_gold = loadImage("Heart Gold.gif")
  img_heart_gold.resize(50,50)
  img_heart_green = loadImage("Heart Green.gif")
  img_heart_green.resize(50,50)
  img_logic_A = loadImage("Logic_A.gif")
  img_logic_A.resize(50,50)
  img_logic_U = loadImage("Logic_U.gif")
  img_logic_U.resize(50,50)
  img_logic_V = loadImage("Logic_V.gif")
  img_logic_V.resize(50,50)
  img_logic_L = loadImage("Logic_L.gif")
  img_logic_L.resize(50,50)
  img_atom = loadImage("Atom_Shape_PURE.gif")
  img_atom.resize(200,200)
  back = loadImage("stairs_11.jpg")
  size(2016,1512,P3D)
  smooth()
  lights()
  frameRate(30)
  noStroke()

def draw():
  global frame, img, img_heart_red, img_heart_gold, img_logic_A, atom1, atom2, atom3, img_atom, back, dance, danceStep, danceLimit, couple, ang
  background(back)
  translate(width / 2, height / 2, 0)
  #rotateX(map(mouseY, 0, height, -PI, PI))
  #rotateY(map(mouseX, 0, width, -PI, PI))
  noStroke()
  noFill()
  if frame < 100:
    pushMatrix()
    # group a pyramid together
    couple = createShape(GROUP)
    couple11 = createShape()
    couple12 = createShape()
    couple13 = createShape()
    #couple = createShape(SPHERE, 100)
    #couple.setTexture(pic)
    # make a pyramid that is rotating with figures on it
    textureMode(NORMAL)
    couple11.beginShape();
    couple11.texture(img);
    couple11.vertex(-img.width/2, -img.height/2, 0, 0);
    couple11.vertex(img.width/2, -img.height/2, 1, 0);
    couple11.vertex(img.width/2, img.height/2, 1, 1);
    couple11.vertex(-img.width/2, img.height/2, 0, 1);
    couple11.endShape();
    
    #couple12.beginShape();
    #couple12.texture(img);
    #couple12.vertex(0, -img.height/2, -img.width/2, 0, 0);
    #couple12.vertex(0, -img.height/2, img.width/2, 1, 0);
    #couple12.vertex(0, img.height/2, img.width/2, 1, 1);
    #couple12.vertex(0, img.height/2, -img.width/2, 0, 1);
    #couple12.endShape();
    
    couple12.beginShape();
    couple12.texture(img_heart_gold);
    couple12.vertex(-img_heart_gold.width/2, -img_heart_gold.height/2, 0, 0);
    couple12.vertex(img_heart_gold.width/2, -img_heart_gold.height/2, 1, 0);
    couple12.vertex(img_heart_gold.width/2, img_heart_gold.height/2, 1, 1);
    couple12.vertex(-img_heart_gold.width/2, img_heart_gold.height/2, 0, 1);
    couple12.endShape();
    couple12.translate(img.width, 0, 0)
    #couple12.rotateY(PI/2)
    
    couple13.beginShape();
    couple13.texture(img_logic_A);
    couple13.vertex(0, -img_logic_A.width/2, -img_logic_A.height/2, 0, 0);
    couple13.vertex(0, -img_logic_A.width/2, img_logic_A.height/2, 1, 0);
    couple13.vertex(0, img_logic_A.width/2, img_logic_A.height/2, 1, 1);
    couple13.vertex(0, img_logic_A.width/2, -img_logic_A.height/2, 0, 1);
    couple13.endShape();
    couple13.translate(-img.width, 0, 0)
    
    #atom.beginShape();
    #atom.texture(img_atom);
    #atom.vertex(-img_atom.width/2, -img_atom.height/2, 0, 0);
    #atom.vertex(img_atom.width/2, -img_atom.height/2, 1, 0);
    #atom.vertex(img_atom.width/2, img_atom.height/2, 1, 1);
    #atom.vertex(-img_atom.width/2, img_atom.height/2, 0, 1);
    #atom.endShape();
    
    stroke(255)
    atom1 = createShape(ELLIPSE, 0, 0, img.width+10, img.height+50)
    atom2 = createShape(ELLIPSE, 0, 0, img.width+10, img.height+50)
    atom3 = createShape(ELLIPSE, 0, 0, img.width+10, img.height+50)
    noStroke()
    
    couple.addChild(couple11)
    couple.addChild(couple12)
    couple.addChild(couple13)
    
    move()
    dance += danceStep
    if (dance > danceLimit or dance < 0):
        dance = 0
        dance += danceStep
    popMatrix()
    frame += 1
  #else:
  #  noLoop()
  #saveFrame("frame-######.png");
    
def move():
    global dance, couple, atom1, atom2, atom3, ang
    pushMatrix()
    # rotate the shape around Y axis
    couple.translate(0, 50, 0)
    couple.rotateY(map(dance, 0, width, -PI, PI))
    shape(couple)
    ang += 0.1
    atom1.rotateX(ang)
    atom2.rotateY(ang)
    atom3.rotateZ(ang)
    atom = createShape(GROUP)
    atom.addChild(atom1)
    atom.addChild(atom2)
    atom.addChild(atom3)
    atom.translate(0, 50, 0)
    shape(atom)
    popMatrix()
  
  
  
