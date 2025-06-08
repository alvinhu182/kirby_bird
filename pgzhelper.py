
import math
import pygame

# Adiciona métodos extras aos objetos Actor
def update_actor_methods():
    def rotate_to(self, angle):
        self.angle = angle

    def move_forward(self, distance):
        angle_rad = math.radians(-self.angle)
        self.x += distance * math.cos(angle_rad)
        self.y += distance * math.sin(angle_rad)

    def point_towards(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        self.angle = -math.degrees(math.atan2(dy, dx))

    def overlaps(self, other):
        return self.colliderect(other)

    def animate(self, images, loop=True):
        if not hasattr(self, '_animation_frames'):
            self._animation_frames = images
            self._animation_index = 0
            self._animation_loop = loop
            self._animation_speed = 0.2
        else:
            self._animation_index += self._animation_speed
            if self._animation_index >= len(self._animation_frames):
                if self._animation_loop:
                    self._animation_index = 0
                else:
                    self._animation_index = len(self._animation_frames) - 1
            self.image = self._animation_frames[int(self._animation_index)]

    pygame.actor.Actor.rotate_to = rotate_to
    pygame.actor.Actor.move_forward = move_forward
    pygame.actor.Actor.point_towards = point_towards
    pygame.actor.Actor.overlaps = overlaps
    pygame.actor.Actor.animate = animate

try:
    update_actor_methods()
except:
    pass
