# Class for each step
class Staircase:
    
    def __init__(self, img_H, numSteps):
        self.x = -img_H / 2
        self.y = 0
        self.filla = 0
        self.fillb = 0
        self.fillc = 0
        self.num = numSteps
        self.stepH = img_H / self.num
        
    def update(self):
        #roll down the stairs
        self.x += self.stepH
        self.y += self.stepH
        self.filla += 89/self.num
        self.fillb += 254/self.num
        self.fillc += 232/self.num
        if self.fillb >= 254:
            self.filla = 0
            self.fillb = 0
            self.fillc = 0
            self.x = -self.stepH * self.num / 2
            self.y = 0
    
    def render(self):
        with pushMatrix():
            stroke(89,254,232)
            strokeWeight(1)
            fill(self.filla, self.fillb, self.fillc)
            rectMode(CENTER)
            rect(0, self.x, self.y, self.stepH)
