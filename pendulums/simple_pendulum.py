from math import sin, cos, pi, sqrt
from pygame.locals import QUIT
import pygame
import sys

pygame.init()
SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

class Pendulum:

    def __init__(self, width=WIDTH, mass=10, L=200, theta=pi/4, r=20):
        self.mass = mass
        self.width = width
        self.r = r
        self.L = L  # length of the pendulum
        self.origin = (width/2, 0)
        self.end_pos = (self.origin[0] + int(L*cos(theta)),
                        self.origin[1] + int(L*sin(theta)))
        self.theta = theta  # angle
        self.aVel = 0.0
        self.aAcc = 0

    def move(self, t):
        self.end_pos = (int(self.width/2 + self.L*sin(self.theta)), int(self.L*cos(self.theta)))
        self.aAcc = -0.01 * sin(self.theta)
        self.theta += self.aVel
        self.aVel += self.aAcc
        self.aVel *= 0.99

    def draw(self, surface, fps):
        surface.fill(WHITE)
        pygame.draw.line(surface, BLACK, self.origin, self.end_pos)
        pygame.draw.circle(surface, RED, self.end_pos, self.r)
        pygame.display.flip()
        fps.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Pendulum')
    fps = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()  # starter tick
    paused = False

    pendulum = Pendulum()

    while True:  # game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        pendulum.move(seconds)
        pendulum.draw(screen, fps)


"""

SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Circles')
fps = pygame.time.Clock()
paused = False

# Ball setup
ball_pos1 = [50, 50]
ball_pos2 = [50, 240]
ball_pos3 = [50, 430]

def update():
    ball_pos1[0] += 5
    ball_pos2[0] += 3
    ball_pos3[0] += 1


def render():
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, ball_pos1, CIRCLE_RADIUS, 0)
    pygame.draw.circle(screen, WHITE, ball_pos2, CIRCLE_RADIUS, 0)
    pygame.draw.circle(screen, GREEN, ball_pos3, CIRCLE_RADIUS, 0)
    pygame.display.update()
    fps.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        update()
        render()

"""
