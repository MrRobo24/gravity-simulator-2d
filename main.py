import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Gravity Simulator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define circle properties
circle_pos = (400, 300)  # (x, y) position
circle_radius = 30

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with background color
    screen.fill(BLACK)
    
    # Draw the solid circle
    pygame.draw.circle(screen, WHITE, circle_pos, circle_radius)
    
    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
