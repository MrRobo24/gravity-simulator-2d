import pygame
from constants import WIDTH, HEIGHT, BLACK
from solar_system import SolarSystem

class Graphics:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            
    def render_solar_system(self):   
        pygame.display.set_caption("2D Gravity Simulator")

        solar_system = SolarSystem()  # Create a SolarSystem instance
        solar_system.add_all_bodies()
        solar_system.set_scale()

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill screen with background color
            self.screen.fill(BLACK)
            solar_system.draw_bodies(pygame, self.screen)
            pygame.display.flip()
            solar_system.update_bodies()
            pygame.time.delay(10)

        # Quit pygame
        pygame.quit()