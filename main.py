import pygame
from body import Body
from physics import Physics

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
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
YELLOW = (255, 255, 0)

# Define circle properties
AU = 1.496e11  # Astronomical Unit in meters

earth = Body(
    name = "Earth",
    mass = 5.97219e24 ,  # Mass in kg
    radius = 9,  # Radius in pixels
    color = BLUE,  # Color in RGB
    velocity = (0, 29784.8),  # Initial velocity in m/s
    position = (-AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    track_locus = True  # Disable locus tracking for the central body
)

moon = Body(
    name = "Moon",
    mass = 7.34767309e22,  # Mass in kg
    radius = 3,  # Radius in pixels
    color = GREY,  # Color in RGB
    velocity = (0, earth.velocity[1] + 1022),  # Initial velocity in m/s
    position = (-0.00257 * AU + earth.position[0], 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    track_locus = True  # Enable locus tracking
)

sun = Body(
    name = "Sun",
    mass = 1.989e30,  # Mass in kg
    radius = 30,  # Radius in pixels
    color = YELLOW,  # Color in RGB
    velocity = (0, 0),  # Initial velocity
    position = (0, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    track_locus = False  # Disable locus tracking for the central body
)

bodies = [sun, earth, moon]

# Create a Physics instance
physics = Physics()

def get_scaled_pos(position: tuple) -> tuple:
    # # Center the camera on Earth
    # earth_pos = earth.position
    
    # Center the moon on Earth
    earth_pos = moon.position
    
    return (
        (position[0] - earth_pos[0]) * SCALE + CENTRE[0],
        (position[1] - earth_pos[1]) * SCALE + CENTRE[1]
    )

def draw_bodies(bodies) -> None:
    for body in bodies:
        pygame.draw.circle(screen, body.color, get_scaled_pos(body.position), body.radius)
        
        if body.track_locus:
            for pos in body.locus:
                pygame.draw.circle(screen, WHITE, get_scaled_pos(pos), 1)

def update_bodies(bodies):
    for body in bodies:
        body.force = (0, 0)  # Reset force for each body
        
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            first_body = bodies[i]
            second_body = bodies[j]
            
            # Calculate the force of gravity between the two bodies
            physics.calc_force_of_gravity(first_body, second_body)
    
    for body in bodies:
        physics.calc_new_velocity_and_pos(body, TIMESTEP)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with background color
    screen.fill(BLACK)
    
    draw_bodies(bodies)
    
    pygame.display.flip()
    
    update_bodies(bodies)
    
    pygame.time.delay(10)

# Quit pygame
pygame.quit()
