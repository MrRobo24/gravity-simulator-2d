import pygame
from .constants import WIDTH, HEIGHT, BLACK
from .solar_system import SolarSystem

class Graphics:
    """
    A class to handle the graphical rendering of the SolarSystem simulation using Pygame.
    Responsible for setting up the window, handling the main simulation loop,
    and drawing celestial bodies on the screen.
    """

    def __init__(self):
        """
        Initializes the Pygame library and sets up the display window with predefined width and height.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def render_solar_system(self):
        """
        Renders the solar system simulation using Pygame.
        This method handles the main game loop, processes events,
        updates body positions, and draws them onto the screen.
        """
        pygame.display.set_caption("2D Gravity Simulator")

        # Create and initialize the solar system with predefined bodies
        solar_system = SolarSystem()
        solar_system.add_all_bodies()
        solar_system.set_scale()

        # Main simulation loop
        running = True
        while running:
            # Handle Pygame events (e.g., closing the window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen with the background color
            self.screen.fill(BLACK)

            # Draw all celestial bodies and their trajectories
            solar_system.draw_bodies(pygame, self.screen)

            # Update the display with new frame
            pygame.display.flip()

            # Update the physics for all bodies
            solar_system.update_bodies()

            # Brief pause to control the frame rate
            pygame.time.delay(10)

        # Clean up and close the Pygame window
        pygame.quit()
