import pygame
from body import Body
from locus_properties import LocusProperties
from physics import Physics

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1680, 1050
CENTRE = (WIDTH // 2, HEIGHT // 2)
TIMESTEP = 60 * 60  # One hour in seconds
AU = 1.496e11  # Astronomical Unit in meters
SCALE = 800 / AU  # 1 AU = 250 pixels
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

sun = Body(
    name = "Sun",
    mass = 1.989e30,  # Mass in kg
    radius = 30,  # Radius in pixels
    color = YELLOW,  # Color in RGB
    velocity = (0, 0),  # Initial velocity
    position = (0, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=False, width=1, color=YELLOW),
    scale = 250  # Scale for the body
)

earth = Body(
    name = "Earth",
    mass = 5.97219e24 ,  # Mass in kg
    radius = 12,  # Radius in pixels
    color = BLUE,  # Color in RGB
    velocity = (0, 29784.8),  # Initial velocity in m/s
    position = (-AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=True, width=1, color=BLUE),
    scale = 10000  # Scale for the body
)

moon = Body(
    name = "Moon",
    mass = 7.34767309e22,  # Mass in kg
    radius = 4,  # Radius in pixels
    color = GREY,  # Color in RGB
    velocity = (0, earth.velocity[1] + 1022),  # Initial velocity in m/s
    position = (-0.00257 * AU + earth.position[0], 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=True, width=1, color=GREY),
    scale = 10000  # Scale for the body
)

venus = Body(
    name = "Venus",
    mass = 4.8675e24,  # Mass in kg
    radius = 10,  # Radius in pixels
    color = (255, 165, 0),  # Color in RGB
    velocity = (0, 35020),  # Initial velocity in m/s
    position = (-0.723 * AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=True, width=1, color=(255, 165, 0)),
    scale = 10000  # Scale for the body
)

mercury = Body(
    name = "Mercury",
    mass = 3.3011e23,  # Mass in kg
    radius = 6,  # Radius in pixels
    color = (169, 169, 169),  # Color in RGB
    velocity = (0, 47400),  # Initial velocity in m/s
    position = (-0.387 * AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=True, width=1, color=(169, 169, 169)),
    scale = 10000  # Scale for the body
)

mars = Body(
    name = "Mars",
    mass = 6.4171e23,  # Mass in kg
    radius = 7,  # Radius in pixels
    color = (255, 0, 0),  # Color in RGB
    velocity = (0, 24077),  # Initial velocity in m/s
    position = (-1.524 * AU, 0),  # Initial position
    acceleration = (0, 0),  # Initial acceleration
    force = (0, 0),  # Initial force
    locus_properties = LocusProperties(track_locus=True, width=1, color=(255, 0, 0)),
    scale = 10000  # Scale for the body
)

bodies = [sun, mercury, venus, earth, moon, mars]

for idx, body in enumerate(bodies):
    print(f"IDX: {idx} - {body.name}")
    
CENTRAL_BODY_IDX = int(input("Enter the body index to focus the camera on: "))
SCALE = bodies[CENTRAL_BODY_IDX].scale / AU  # Scale based on the central body

# Create a Physics instance
physics = Physics()

def get_scaled_pos(position: tuple, centre_on_pos = None) -> tuple:
    if centre_on_pos == None:
        centre_on_pos = bodies[CENTRAL_BODY_IDX].position
    return (
        (position[0] - centre_on_pos[0]) * SCALE + CENTRE[0],
        (position[1] - centre_on_pos[1]) * SCALE + CENTRE[1]
    )

def draw_bodies(bodies) -> None:
    for body in bodies:
        pygame.draw.circle(screen, body.color, get_scaled_pos(body.position), body.radius)
        
        curr_locus_properties = body.locus_properties
        if curr_locus_properties.track_locus:
            for pos in body.locus:
                pygame.draw.circle(screen, curr_locus_properties.color, get_scaled_pos(pos), curr_locus_properties.width)

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
