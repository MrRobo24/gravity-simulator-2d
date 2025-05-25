import pygame
from body import Body
from physics import Physics

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1920, 1080
CENTRE = (WIDTH // 2, HEIGHT // 2)
TIMESTEP = 60 * 60  # One hour in seconds
AU = 1.496e11  # Astronomical Unit in meters
SCALE = 20000 / AU  # 1 AU = 250 pixels
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Gravity Simulator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)


# Define circle properties
AU = 1.496e11  # Astronomical Unit in meters

first_body = Body(
    name = "Earth",
    mass = 5.97219e24 ,  # Mass in kg
    radius = 20,  # Radius in pixels
    color = BLUE,  # Color in RGB
    velocity = (0, 0),  # Initial velocity
    position = (0, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0)  # Initial force
)

second_body = Body(
    name = "Moon",
    mass = 7.34767309e22,  # Mass in kg
    radius = 5.4,  # Radius in pixels
    color = GREY,  # Color in RGB
    velocity = (0, 1022),  # Initial velocity in m/s
    position = (-0.00257 * AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
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
    pygame.draw.circle(screen,
                       first_body.color,
                       (first_body.position[0] + CENTRE[0], first_body.position[1] + CENTRE[1]),
                       first_body.radius)
    
    pygame.draw.circle(screen,
                       second_body.color,
                       (second_body.position[0] * SCALE + CENTRE[0], second_body.position[1] * SCALE + CENTRE[1]),
                       second_body.radius)
    
    # Draw the locus of the second body
    for pos in second_body.locus:
        pygame.draw.circle(screen, WHITE, (pos[0] * SCALE + CENTRE[0], pos[1] * SCALE + CENTRE[1]), 1)
    
    # Update display
    pygame.display.flip()
    
    print(second_body.position, second_body.velocity, second_body.acceleration, second_body.force)
    
    physics.calc_force_of_gravity(first_body, second_body)
    
    # physics.calc_accelaration_by_force(first_body)
    # physics.calc_new_velocity_and_pos(first_body, 0.01)
    physics.calc_new_velocity_and_pos(second_body, TIMESTEP)
    
    pygame.time.delay(10)

# Quit pygame
pygame.quit()
