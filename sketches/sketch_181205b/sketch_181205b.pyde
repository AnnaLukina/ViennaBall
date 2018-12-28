dance = 0
danceStep = 20
danceLimit = 4032
ang = 0.0
frame = 0

def setup():
  global frame, V, img, img_FM, img_MM, img_FF, img_heart_red, img_heart_gold, img_atom, img_logic_A, back, dance, danceStep, danceLimit, couple, ang, x, y, filla, fillb, fillc
  # Make a new instance of a PImage by loading an image file
  # Declaring a variable of type PImage
  img_MM = loadImage("Men_Dancers_PURE.gif")
  img_MM.resize(100,100)
  img = loadImage("Red_dancer_PURE.gif")
  img.resize(100,100)
  img_FM = loadImage("Lavanda_Dancer_PURE.gif")
  img_FM.resize(100,100)
  img_FF = loadImage("Grey_Dancer_PURE.gif")
  img_FF.resize(100,100)
  img_MF = loadImage("PINK_Dancer_PURE.gif")
  img_MF.resize(100,100)
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
  img_atom.resize(100,100)
  back = loadImage("stairs_11.jpg")
  holo = loadImage("9.jpg")
  size(2016,1512,P3D)
  smooth()
  lights()
  frameRate(30)
  noStroke()
  x = -back.height/2
  y = 0
  filla=0
  fillb=0
  fillc=0
  frame = 0
  V = loadShape("Heart_G.obj")
  V.rotateX(PI)

def draw():
  global frame, V, img, img_FM, img_MM, ing_FF, img_heart_red, img_heart_gold, img_logic_A, atom1, atom2, atom3, img_atom, back, dance, danceStep, danceLimit, couple, ang, filla, fillb, fillc, x, y
  background(0)
  translate(width / 2, height / 2, 0)
  #rotateX(map(mouseY, 0, height, -PI, PI))
  #rotateY(map(mouseX, 0, width, -PI, PI))
  #noStroke()
  #noFill()
  
  # dancers on the steps
  if frame < 1000:
  #  for step in range(0,14):
  #      #gradient stairs
  #      stroke(89,254,232)
  #      strokeWeight(1)
  #      fill(filla, fillb, fillc)
  #      rectMode(CENTER)
  #      rect(0, x, y, back.height/13)
  #      #roll down stairs
  #      x += back.height/13
  #      y += back.width/13
  #      filla += 89/13
  #      fillb += 254/13
  #      fillc += 232/13
  #      if fillb >= 254:
  #          filla = 0
  #          fillb = 0
  #          fillc = 0
  #          x = -back.height/2
  #          y = 0
  #  
    noStroke()
    noFill()
    
    pushMatrix()
    # group a dancing couple together
    couple = createShape(GROUP)
    couple11 = createShape()
    couple12 = createShape()
    couple13 = createShape()
    couple14 = createShape()
    couple15 = createShape()
    couple16 = createShape()
    # make rotating with figures
    textureMode(NORMAL)
    couple11.beginShape();
    couple11.texture(img);
    couple11.vertex(-img.width/2, -img.height/2, 0, 0);
    couple11.vertex(img.width/2, -img.height/2, 1, 0);
    couple11.vertex(img.width/2, img.height/2, 1, 1);
    couple11.vertex(-img.width/2, img.height/2, 0, 1);
    couple11.endShape();
    
    couple16.beginShape();
    couple16.texture(img_FF);
    couple16.vertex(-img_FF.width/2, -img_FF.height/2, 0, 0);
    couple16.vertex(img_FF.width/2, -img_FF.height/2, 1, 0);
    couple16.vertex(img_FF.width/2, img_FF.height/2, 1, 1);
    couple16.vertex(-img_FF.width/2, img_FF.height/2, 0, 1);
    couple16.endShape();
    couple16.translate(0, 0, -2*img.height)
    
    couple12.beginShape();
    couple12.texture(img_MM);
    couple12.vertex(0, -img_MM.width/2, -img_MM.height/2, 0, 0);
    couple12.vertex(0, -img_MM.width/2, img_MM.height/2, 1, 0);
    couple12.vertex(0, img_MM.width/2, img_MM.height/2, 1, 1);
    couple12.vertex(0, img_MM.width/2, -img_MM.height/2, 0, 1);
    couple12.endShape();
    couple12.translate(img.width, -img.height, -img.height)
    
    couple13.beginShape();
    couple13.texture(img_FM);
    couple13.vertex(0, -img_FM.width/2, -img_FM.height/2, 0, 0);
    couple13.vertex(0, -img_FM.width/2, img_FM.height/2, 1, 0);
    couple13.vertex(0, img_FM.width/2, img_FM.height/2, 1, 1);
    couple13.vertex(0, img_FM.width/2, -img_FM.height/2, 0, 1);
    couple13.endShape();
    couple13.translate(-img.width, -img.height, -img.height)
    
    couple14.beginShape();
    couple14.texture(img_FF);
    couple14.vertex(0, -img_FF.width/2, -img_FF.height/2, 0, 0);
    couple14.vertex(0, -img_FF.width/2, img_FF.height/2, 1, 0);
    couple14.vertex(0, img_FF.width/2, img_FF.height/2, 1, 1);
    couple14.vertex(0, img_FF.width/2, -img_FF.height/2, 0, 1);
    couple14.endShape();
    couple14.translate(img.width, img.height, -img.height)
    
    couple15.beginShape();
    couple15.texture(img_MM);
    couple15.vertex(0, -img_MM.width/2, -img_MM.height/2, 0, 0);
    couple15.vertex(0, -img_MM.width/2, img_MM.height/2, 1, 0);
    couple15.vertex(0, img_MM.width/2, img_MM.height/2, 1, 1);
    couple15.vertex(0, img_MM.width/2, -img_MM.height/2, 0, 1);
    couple15.endShape();
    couple15.translate(-img.width, img.height, -img.height)
    
    stroke(89,254,232)
    strokeWeight(2)
    atom1 = createShape(ELLIPSE, 0, 0, img.width+50, img.height+100)
    atom2 = createShape(ELLIPSE, 0, 0, img.width+50, img.height+100)
    atom3 = createShape(ELLIPSE, 0, 0, img.width+50, img.height+100)
    noStroke()
    noFill()
    
    couple.addChild(couple11)
    couple.addChild(couple12)
    couple.addChild(couple13)
    couple.addChild(couple14)
    couple.addChild(couple15)
    couple.addChild(couple16)
    
    move()
    dance += danceStep
    if (dance > danceLimit or dance < 0):
        dance = 0
        dance += danceStep
    popMatrix()
    frame += 1
  #saveFrame("frame-######.png");
    
def move():
    global dance, V, couple, atom1, atom2, atom3, ang
    pushMatrix()
    # rotate the shape around Y axis
    #couple.translate(0, 100, 500)
    #couple.rotateY(map(dance, 0, width, -PI/2, PI/2))
    #shape(couple)
    #couple.translate(0, 100, 400)
    #couple.rotateY(map(dance-50, 0, width, -PI/2, PI/2))
    #shape(couple)
    #couple.translate(0, 100, 300)
    #couple.rotateY(map(dance-100, 0, width, -PI/2, PI/2))
    #shape(couple)
    #couple.translate(0, 100, 200)
    #couple.rotateY(map(dance-150, 0, width, -PI/2, PI/2))
    #shape(couple)
    #couple.translate(0, 100, 100)
    #couple.rotateY(map(dance-200, 0, width, -PI/2, PI/2))
    #shape(couple)
    V.translate(0, 0, 0)
    V.rotateY(PI/100)
    V.rotateX(PI/100)
    V.rotateZ(PI/100)
    shape(V, 0, 0)
    # rotate the nucleus
    ang += 0.1
    atom1.rotateX(ang)
    atom2.rotateY(ang)
    atom3.rotateZ(ang)
    atom = createShape(GROUP)
    atom.addChild(atom1)
    atom.addChild(atom2)
    atom.addChild(atom3)
    atom.translate(0, 0, dance-2000)
    shape(atom)
    popMatrix()
  
  
  
