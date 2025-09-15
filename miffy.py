import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("animal")
clock = pygame.time.Clock()
xpos = 0
ypos = 0
mousePos = (xpos, ypos)


def miffy():
    xpos = random.randrange(50, 750)
    ypos = random.randrange(100, 700)
    #size = random.randrange(20, 50)
    #outline ears
    pygame.draw.ellipse(screen, (0, 0, 0), (xpos-44, ypos-104, 40, 88))
    pygame.draw.ellipse(screen, (0, 0, 0), (xpos+6, ypos-104, 40, 88))
    #head
    pygame.draw.circle(screen, (0, 0,0), (xpos, ypos), 54)
    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 50)
    #ears (left, right)
    pygame.draw.ellipse(screen, (255, 255, 255), (xpos-40, ypos-100, 32, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (xpos+10, ypos-100, 32, 80))
    #eyes
    pygame.draw.circle(screen, (0, 0, 0), (xpos-25, ypos+6), 5)
    pygame.draw.circle(screen, (0, 0, 0), (xpos+25, ypos+6), 5)
    #mouth
    pygame.draw.line(screen, (0, 0, 0), (xpos-8, ypos+20), (xpos+8, ypos+30), 4)
    pygame.draw.line(screen, (0, 0, 0), (xpos-8, ypos+30), (xpos+8, ypos+20), 4)

# running = True
# while running:
#     print(mousePos[0], mousePos[1])
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             
#         if event.type == pygame.MOUSEMOTION:
#             mousePos = event.pos
            
            
            
screen.fill((116, 196, 252))
for i in range(4):
    miffy()
pygame.display.flip()
pygame.time.wait(100000)
pygame.quit()


