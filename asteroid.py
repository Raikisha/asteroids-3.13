import random
import circleshape
import constants
import pygame

from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
         super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,constants.LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rot = random.uniform(20,50)
        v1 = self.velocity.rotate(rot)
        v2 = self.velocity.rotate(-rot)

        baby_asteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        baby_asteroid_1 = Asteroid(self.position.x,self.position.y,baby_asteroid_radius)
        baby_asteroid_2 = Asteroid(self.position.x,self.position.y,baby_asteroid_radius)

        baby_asteroid_1.velocity = v1 * 1.2
        baby_asteroid_2.velocity = v2 * 1.2
        