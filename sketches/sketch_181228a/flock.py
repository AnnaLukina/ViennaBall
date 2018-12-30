# The Flock (a list of Boid objects)
class Flock(object):

    def __init__(self):
        self.boids = []  # Initialize a list for all the boids.
        self.letters = [] # Initialize a list for boids used in wiriting words

    def run(self, word):
        if word and self.letters:
            for b in self.letters:
                # Pass the entire list of letters to each letter individually.
                b.run(self.letters, word)
        else:
            for b in self.boids:
                # Pass the entire list of boids to each boid individually.
                b.run(self.boids, word)

    def addBoid(self, b, word):
        if word:
            if self.boids:
                # borrow a ready-made boid for formation of letters
                self.letters.append(self.boids[-1])
                del self.boids[-1]
                # make the boid go to the given pixel location
                self.letters[-1].acceleration.mult(0)
                self.letters[-1].velocity = PVector.sub(b.location, self.letters[-1].location)
                self.letters[-1].velocity.normalize()
                self.letters[-1].velocity.mult(self.letters[-1].maxspeed)
                self.letters[-1].target = b.location
            else:
                # or spawn a new one at the given pixel location
                self.letters.append(b)
        else:
            self.boids.append(b)
