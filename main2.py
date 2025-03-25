import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Sprite Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define rectangles
player = pygame.Rect(100, 100, 50, 50)  # Movable sprite
static_rect = pygame.Rect(400, 300, 50, 50)  # Static sprite

# Set up movement variables
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Frame rate control
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    
    # Prevent player from moving out of bounds
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))
    
    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, static_rect)
    
    pygame.display.update()

# Quit Pygame
pygame.quit()
