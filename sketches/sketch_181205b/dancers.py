# Class of a shape inside a nucleus
class Dancers:
    
    def __init__(self, core):
        self.core = core
        self.theta = 0
        
    def render(self, x, y, z):
        nucleus = createShape(GROUP)
        orbid_atom = []
        for i in range(3):  
            orbid_atom.append(createShape(GROUP))
        atom = []
        orbid = []
        radius = []
        self.theta += radians(1)
        with pushMatrix():
            stroke(255)
            strokeWeight(1)
            noFill()
            orbid.append(createShape(ELLIPSE, 0, 0, 100, 50))
            orbid[0].rotateX(PI/2)
            fill(255)
            atom.append(createShape(SPHERE, 5))
            noFill()
            noStroke()
            radius.append(createShape(SPHERE, 1))
            atom[0].translate(-50, 0)
            orbid_atom[0].addChild(radius[0])
            orbid_atom[0].addChild(atom[0])
            orbid_atom[0].rotateY(self.theta)
            #shape(orbid_atom[0])
            noTint()
            dancer = createShape(SPHERE, 40)
            dancer.setTexture(self.core)
            dancer.rotateY(self.theta)
            #shape(dancer)
            #shape(orbid[0])
            
            stroke(255)
            strokeWeight(1)
            noFill()
            orbid.append(createShape(ELLIPSE, 0, 0, 50, 100))
            orbid[1].rotateY(PI/2)
            orbid[1].rotateZ(PI/4)
            fill(255)
            atom.append(createShape(SPHERE, 5))
            noFill()
            noStroke()
            radius.append(createShape(SPHERE, 1))
            atom[1].translate(50*cos(self.theta), -50*sin(PI/3))
            orbid_atom[1].addChild(radius[1])
            orbid_atom[1].addChild(atom[1])
            orbid_atom[1].rotateX(self.theta)
            #shape(orbid_atom[1])
            #shape(orbid[1])
            
            stroke(255)
            strokeWeight(1)
            noFill()
            orbid.append(createShape(ELLIPSE, 0, 0, 50, 100))
            orbid[2].rotateY(-PI/2)
            orbid[2].rotateZ(-PI/4)
            fill(255)
            atom.append(createShape(SPHERE, 5))
            noFill()
            noStroke()
            radius.append(createShape(SPHERE, 1))
            atom[2].translate(-50*cos(self.theta), -50*sin(PI/3))
            orbid_atom[2].addChild(radius[2])
            orbid_atom[2].addChild(atom[2])
            orbid_atom[2].rotateX(-self.theta)
            #shape(orbid_atom[2])
            #shape(orbid[2])
            
            # a step
            stroke(255)
            rectMode(CENTER)
            step = createShape(RECT, 0, 100, x, 1)
            
            for o in orbid_atom:
                nucleus.addChild(o)
            #rotate(1)
            nucleus.addChild(dancer)
            #nucleus.addChild(step)
            nucleus.translate(0, y, z)
            shape(nucleus)
        
