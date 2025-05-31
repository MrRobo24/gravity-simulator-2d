from bodies import bodies
from constants import TIMESTEP, AU, CENTRE
from physics import Physics

class SolarSystem:
    """
    A class to represent a simulated solar system with multiple celestial bodies.
    Handles adding bodies, updating their positions and velocities based on gravity,
    scaling for visualization, and rendering with pygame.
    """

    def __init__(self):
        """Initializes the SolarSystem with an empty list of bodies and default scale."""
        self.bodies = []
        self.physics = Physics()
        self.CENTRAL_BODY_IDX = 0  # Index of the central body to focus the camera on
        self.SCALE = 800 / AU  # Default visualization scale (pixels per AU)

    def add_body(self, body):
        """Adds a single body to the solar system."""
        self.bodies.append(body)

    def get_bodies(self):
        """Returns the list of all bodies in the solar system."""
        return self.bodies

    def __str__(self):
        """Returns a string representation of the solar system."""
        return f"Solar System with {len(self.bodies)} bodies."

    def add_bodies(self, new_bodies):
        """Adds multiple bodies to the solar system."""
        for body in new_bodies:
            self.add_body(body)

    def add_all_bodies(self):
        """Adds all predefined bodies from the 'bodies' module."""
        self.add_bodies(bodies)

    def update_bodies(self):
        """
        Updates the positions and velocities of all bodies based on gravitational forces
        computed between every pair of bodies.
        """
        # Reset the force on each body
        for body in self.bodies:
            body.force = (0, 0)

        # Calculate pairwise gravitational forces
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                first_body = self.bodies[i]
                second_body = self.bodies[j]

                self.physics.calc_force_of_gravity(first_body, second_body)

        # Update each body's velocity and position based on accumulated forces
        for body in self.bodies:
            self.physics.calc_new_velocity_and_pos(body, TIMESTEP)

    def set_scale(self):
        """
        Sets the scale of the simulation by choosing a central body to focus on.
        This affects the zoom level of the visual representation.
        """
        try:
            for idx, body in enumerate(self.bodies):
                print(f"IDX: {idx} - {body.name}")

            self.CENTRAL_BODY_IDX = int(input("Enter the body index to focus the camera on: "))

            # Scale relative to the chosen central body
            self.SCALE = self.bodies[self.CENTRAL_BODY_IDX].scale / AU
        except Exception as e:
            print(f"Invalid input: {e}. Using default scale.")

    def get_scaled_pos(self, position: tuple, centre_on_pos=None) -> tuple:
        """
        Converts a position in simulation space to screen space coordinates.

        Args:
            position (tuple): The (x, y) position in simulation coordinates.
            centre_on_pos (tuple, optional): The position to center the view on. Defaults to central body.

        Returns:
            tuple: Scaled (x, y) position in screen coordinates.
        """
        if centre_on_pos is None:
            centre_on_pos = bodies[self.CENTRAL_BODY_IDX].position
        return (
            (position[0] - centre_on_pos[0]) * self.SCALE + CENTRE[0],
            (position[1] - centre_on_pos[1]) * self.SCALE + CENTRE[1]
        )

    def draw_bodies(self, pygame, screen) -> None:
        """
        Draws all bodies on the screen using pygame, including their trajectories if enabled.

        Args:
            pygame: The pygame module for rendering.
            screen: The pygame display surface.
        """
        for body in self.bodies:
            # Draw the body itself
            pygame.draw.circle(screen, body.color, self.get_scaled_pos(body.position), body.radius)

            # Draw the trajectory (locus) if tracking is enabled
            curr_locus_properties = body.locus_properties
            if curr_locus_properties.track_locus:
                for pos in body.locus:
                    pygame.draw.circle(
                        screen,
                        curr_locus_properties.color,
                        self.get_scaled_pos(pos),
                        curr_locus_properties.width
                    )
