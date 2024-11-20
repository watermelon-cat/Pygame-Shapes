import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pattern Generator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 252, 87)
ORANGE = (255, 164, 66)
GREY = (186, 170, 153)

# Starting settings
current_color = RED
current_shape = "triangle"
SHAPE_SIZE = 40

# List of shapes (each shape is: [x, y, size, color, type])
shapeList = [] #this is going to be a LIST of LISTS!

# Initialize font for instructions
font = pygame.font.Font(None, 36)

# Main game loop-------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            
            #numbers select what shape to draw
            if event.key == pygame.K_1:
                current_shape = "ellipse"  # Select ellipse
            elif event.key == pygame.K_2:
                current_shape = "hexagon"  # Select hexagon
            elif event.key == pygame.K_3:
                current_shape = "triangle"  # Select triangle
            elif event.key == pygame.K_4:
                current_shape = "square"  # Select triangle
            elif event.key == pygame.K_5:
                current_shape = "circle"  # Select triangle
                
            #letters select what color to draw with
            if event.key == pygame.K_r:
                current_color = RED  # Change to red
            elif event.key == pygame.K_g:
                current_color = GREEN  # Change to green
            elif event.key == pygame.K_b:
                current_color = BROWN  # Change to brown
            elif event.key == pygame.K_o:
                current_color = ORANGE  # Change to green
            elif event.key == pygame.K_y:
                current_color = YELLOW  # Change to brown
            elif event.key == pygame.K_l:
                current_color = BLACK  # Change to green
            elif event.key == pygame.K_w:
                current_color = WHITE  # Change to brown
            
            #SIZE CHANGE
            if event.key == pygame.K_p:
                SHAPE_SIZE += 10
            elif event.key == pygame.K_m:
                SHAPE_SIZE -= 10

        # Check for mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_shape = [mouse_x, mouse_y, SHAPE_SIZE, current_color, current_shape]
            shapeList.append(new_shape)  # Add new shape to the list

    # Clear the screen
    screen.fill(GREY)

    # Draw all shapes directly in the loop
    for i in range(len(shapeList)):
        x = shapeList[i][0]
        y = shapeList[i][1]
        size = shapeList[i][2]
        color = shapeList[i][3]
        kind = shapeList[i][4]

        if kind == "ellipse":
            pygame.draw.ellipse(screen, color, (x - size, y - size // 2, size * 2, size))  # Ellipse dimensions
        elif kind == "square":
            pygame.draw.rect(screen,color, (x -size, y- size // 2, size, size))
        elif kind == "circle":
            pygame.draw.circle(screen,color, (x -size, y- size), size, size)
        elif kind == "hexagon":
            points = [
                (x, y - size),  # Top
                (x + size, y - size // 2),  # Top-right
                (x + size, y + size // 2),  # Bottom-right
                (x, y + size),  # Bottom
                (x - size, y + size // 2),  # Bottom-left
                (x - size, y - size // 2)   # Top-left
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "triangle":
            points = [
                (x, y - size),           # Top point
                (x - size, y + size),    # Bottom-left point
                (x + size, y + size)     # Bottom-right point
            ]
            pygame.draw.polygon(screen, color, points)

    # Display instructions at the top
    instructions = font.render("1: Ellipse | 2: Hexagon | 3: Triangle | 4: Square | 5: Circle |", True, BLACK)
    screen.blit(instructions, (10, 10))
    colorlist = font.render("L: Black | W: White | R: Red | G: Green | B: Brown | O: Orange | Y: Yellow |", True, BLACK)
    screen.blit(colorlist, (10, 40))
    size_show = font.render("P : Plus | M: Minus |", True, BLACK)
    screen.blit(size_show, (10, 70))
    #size_show = font.render(SHAPE_SIZE, True, BLACK)
    #screen.blit(SHAPE_SIZE, (10, 70))
    print(SHAPE_SIZE)

    # Update the screen
    pygame.display.flip()

pygame.quit()

