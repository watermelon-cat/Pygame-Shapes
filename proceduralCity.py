import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Procedural Cityscape")

# Function to draw a building with random features
def draw_building():
    xpos = random.randrange(-100, 800)
    ypos = random.randrange(0, 800)
    width = random.randrange(100, 200)
    color = random.randrange(50, 200)
    pygame.draw.rect(screen, (color, color, color), (xpos, ypos, width, 800)) #building
    pygame.draw.rect(screen, (0,0,0), (xpos, ypos, width, 800), 2) #black outline
    for i in range (xpos+10, xpos + width - 20, 30):
        for j in range(ypos + 10, ypos + 600, 60):
            pygame.draw.rect(screen, (200, 200, 50), (i, j, 20, 40))#windows
            
def draw_clouds():
    xpos = random.randrange(-40, 800)
    ypos = random.randrange(30, 140)
    radius = random.randrange(15, 35)
    color = random.randrange(180, 235)
    diff = random.randrange(6, 12)
    pygame.draw.circle(screen, (color, color, color), (xpos, ypos) ,radius)
    pygame.draw.circle(screen, (color, color, color), (xpos+30, ypos-5), radius+diff)
    pygame.draw.circle(screen, (color, color, color), (xpos+60, ypos), radius+2)

def draw_trees():
    xpos = random.randrange(0, 800)
    radius = random.randrange(20, 40)
    width = random.randrange(20, 35)
    height = random.randrange(80, 140)
    ypos = 600-height
    #tree color
    color1 = random.randrange(180, 230)
    color2 = random.randrange(40, 80)
    #trunk color
    color3 = random.randrange(80, 100)
    color4 = random.randrange(40, 60)
    diff = random.randrange(10, 18)
    pygame.draw.rect(screen, (color3, color3, color4), (xpos, ypos, width, height))#trunk
    pygame.draw.circle(screen, (color2, color1, color2), (xpos-30, ypos), radius)
    pygame.draw.circle(screen, (color2, color1, color2), (xpos, ypos-10), radius+diff)
    pygame.draw.circle(screen, (color2, color1, color2), (xpos+40, ypos), radius)


screen.fill((116, 196, 252))
for i in range(20):
    draw_building()
for j in range(12):
    draw_trees()
    draw_clouds()

pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()

