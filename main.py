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

def check_bounds_and_collision():
    if (abs(first_body.position[0] - second_body.position[0]) < first_body.radius + second_body.radius and
        abs(first_body.position[1] - second_body.position[1]) < first_body.radius + second_body.radius):
        print("Collision detected!")
        return False
    
    if (first_body.position[0] < 0 or first_body.position[0] > WIDTH or
        first_body.position[1] < 0 or first_body.position[1] > HEIGHT):
        print("Out of bounds!")
        return False
    
    if (second_body.position[0] < 0 or second_body.position[0] > WIDTH or
        second_body.position[1] < 0 or second_body.position[1] > HEIGHT):
        print("Out of bounds!")
        return False
    
    return True


# Define circle properties

first_body = Body(
    name = "Earth",
    mass = 100,  # Mass in kg
    radius = 10,  # Radius in pixels
    color = WHITE,  # Color in RGB
    velocity = (0, 0),  # Initial velocity
    position = (500, 500),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0)  # Initial force
)

second_body = Body(
    name = "Moon",
    mass = 1,  # Mass in kg
    radius = 5,  # Radius in pixels
    color = WHITE,  # Color in RGB
    velocity = (1**0.5, 0),  # Initial velocity
    position = (500, 600),  # Initial position
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
    pygame.draw.circle(screen, first_body.color, first_body.position, first_body.radius)
    pygame.draw.circle(screen, second_body.color, second_body.position, second_body.radius)
    
    if not check_bounds_and_collision():
        break
    
    # Update display
    pygame.display.flip()
    
    # print(second_body.position, second_body.velocity)
    
    physics.calc_force_of_gravity(first_body, second_body)
    
    # physics.calc_accelaration_by_force(first_body)
    physics.calc_new_position_and_velocity(first_body, 0.01)
    physics.calc_new_position_and_velocity(second_body, 0.01)
    
    pygame.time.delay(10)

# Quit pygame
pygame.quit()
