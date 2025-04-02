import pygame
from body import Body
from physics import Physics

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Gravity Simulator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define circle properties
circle_pos = (100, 100)  # (x, y) position
circle_radius = 50

first_body = Body(
    name = "Earth",
    mass = 10,  # Mass in kg
    radius = circle_radius,  # Radius in pixels
    color = WHITE,  # Color in RGB
    velocity = (0, 0),  # Initial velocity
    position = circle_pos,  # Initial position
    acceleration = (0, 10),  # Initial acceleration
    force = (0, 0)  # Initial force
)

# Create a Physics instance
physics = Physics()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with background color
    screen.fill(BLACK)
    
    # Draw the solid circle
    pygame.draw.circle(screen, first_body.color, first_body.position, first_body.radius)
    
    # Update display
    pygame.display.flip()
    
    # physics.calc_accelaration_by_force(first_body)
    physics.calc_new_position_and_velocity(first_body, 0.01)  # Update position with a time step of 0.01 seconds
    
    pygame.time.delay(10)

# Quit pygame
pygame.quit()
