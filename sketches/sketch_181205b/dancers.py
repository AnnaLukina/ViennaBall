# Class of a shape inside a nucleus
class Dancers:
    
    def __init__(self, core):
        self.core = core
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
    def display(self):
        noStroke()
        noFill()
        noTint()
        textureMode(NORMAL)
        dancer = createShape()
        dancer.beginShape()
        dancer.texture(self.core)
        # face.
        dancer.vertex(-self.core.width/2,
        -self.core.height/2,
        1,
        0, 0)
        dancer.vertex(self.core.width/2,
        -self.core.height/2,
        1,
        1, 0)
        dancer.vertex(self.core.width/2,
        self.core.height/2,
        1,
        1, 1)
        dancer.vertex(-self.core.width/2,
        self.core.height/2,
        1,
        0, 1)
        dancer.endShape()
        dancer.translate(self.x, self.y, self.z)
        return dancer
