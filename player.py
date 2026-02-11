import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x,pos_y,constants.PLAYER_RADIUS)

        self.rotation = 0


        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),constants.LINE_WIDTH)

