class Electron:
    
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.r = 0.0
        self.s = 0.0
        
    def setCoords(self, millis, rOrbit, rOrbit2, rOrbit3):
        self.x = sin(millis * self.s) * rOrbit/2
        self.y = cos(millis * self.s) * rOrbit2/2
        self.z = cos(millis * self.s) * rOrbit3/2
        
    def display(self):
        fill(255)
        #strokeWeight(5)
        stroke(255)
        #electron = createShape(ELLIPSE, self.x, self.y, self.r, self.r)
        electron = createShape(SPHERE, self.r)
        electron.translate(self.x, self.y, self.z)
        return electron
        #ellipse(self.x, self.y, self.r, self.r)
        
    def overLapping(self):
        if (self.y < 0):
            return True
        else:
            return False
