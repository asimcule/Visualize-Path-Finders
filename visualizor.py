import pygame
from bfs import bfs

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("My First Pygame Window")
G = [
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
]


source=(0,0)
dest=(14,14)
prev=bfs(G,source,dest)
if prev is None:
    print("No valid path possible!")
row=len(G)
column=len(G[0])
rect_width=width/column
rect_height=height/row
start_x=rect_width/2
start_y=rect_height/2


for event in pygame.event.get():
    if event.type == pygame.QUIT:  # Close window if X button is pressed
        running = False

# Fill the screen with a color (RGB)
screen.fill((0, 0, 0))  # Blue background
# create a text object
font = pygame.font.Font(None, 74)
text = font.render('No Valid Path found!', True, (255, 165, 0))  # White text
text_rect = text.get_rect(center=(width/2, height/2))  # Position it at the center

# display 
for m in range(row):
    for n in range(column):
        rect_x = n * rect_width
        rect_y = m * rect_height
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

        if prev is not None and (m,n) in prev:
            if (m,n)==source:
                pygame.draw.rect(screen, (255, 0, 0), rect)  # Filled white rectangle
            elif (m,n)==dest:
                pygame.draw.rect(screen, (255, 0, 0), rect)  # Filled white rectangle
            else:
                pygame.draw.rect(screen, (0, 255,0), rect)  # Filled white rectangle

        elif G[m][n] == 1:
            pygame.draw.rect(screen, (255, 255, 255), rect)  # Filled white rectangle
        
        pygame.draw.rect(screen, (0, 0, 0), rect, 3)  # Green border with thickness 3

        if prev is None:
            screen.blit(text, text_rect)

# Update the display
pygame.display.flip()

# wait for the user to close the window
waiting=True
while waiting:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            waiting=False

# Quit Pygame
pygame.quit()
