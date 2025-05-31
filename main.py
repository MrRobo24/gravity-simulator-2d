import pygame
from physics import Physics
from solar_system import SolarSystem
from constants import AU, WIDTH, HEIGHT, CENTRE, BLACK

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Gravity Simulator")

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

if __name__ == "__main__":
    solar_system = SolarSystem()
    solar_system.add_all_bodies()

    bodies = solar_system.get_bodies()

    for idx, body in enumerate(bodies):
        print(f"IDX: {idx} - {body.name}")
        
    SCALE = 800 / AU # Default scale for the bodies
    CENTRAL_BODY_IDX = int(input("Enter the body index to focus the camera on: "))
    SCALE = bodies[CENTRAL_BODY_IDX].scale / AU  # Scale based on the central body

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
        
        solar_system.update_bodies(physics)
        
        pygame.time.delay(10)

    # Quit pygame
    pygame.quit()
