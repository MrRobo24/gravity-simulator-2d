from .body import Body

class Physics:
    """
    A class that handles physics calculations for celestial bodies in a gravity simulation.
    Includes methods for calculating gravitational forces, acceleration, velocity,
    and position updates over time.
    """

    def __init__(self):
        """
        Initializes physical constants.
        """
        self.universal_grav_const = 6.67430e-11  # Universal gravitational constant in m^3 kg^-1 s^-2

    def calc_accelaration_by_force(self, body: Body) -> None:
        """
        Calculates and sets the acceleration of a body based on the net force acting on it.

        Args:
            body (Body): The celestial body whose acceleration is to be calculated.

        Raises:
            ValueError: If the body's mass is zero or negative.
        """
        if body.mass <= 0.0:
            raise ValueError("Mass must be greater than zero.")
        else:
            body.acceleration = (body.force[0] / body.mass, body.force[1] / body.mass)

    def calc_new_position(self, body: Body, time: float) -> None:
        """
        Updates the position of the body based on its velocity and time.

        Args:
            body (Body): The celestial body to update.
            time (float): The timestep in seconds.

        Raises:
            ValueError: If time is zero or negative.
        """
        if time <= 0.0:
            raise ValueError("Time must be greater than zero.")
        else:
            # Update position using s = ut (approximation without acceleration)
            new_x = body.position[0] + body.velocity[0] * time
            new_y = body.position[1] + body.velocity[1] * time
            body.position = (new_x, new_y)
            body.locus.append(body.position)  # Track position for drawing trajectory

    def calc_new_velocity(self, body: Body, time: float) -> None:
        """
        Updates the velocity of the body based on its acceleration and time.

        Args:
            body (Body): The celestial body to update.
            time (float): The timestep in seconds.

        Raises:
            ValueError: If time is zero or negative.
        """
        if time <= 0.0:
            raise ValueError("Time must be greater than zero.")
        else:
            # Update velocity using v = u + at
            v_x = body.velocity[0] + body.acceleration[0] * time
            v_y = body.velocity[1] + body.acceleration[1] * time
            body.velocity = (v_x, v_y)

    def calc_new_velocity_and_pos(self, body: Body, time: float) -> None:
        """
        Convenience method to calculate both velocity and position updates.

        Args:
            body (Body): The celestial body to update.
            time (float): The timestep in seconds.
        """
        if (body.force != (0, 0)):
            self.calc_accelaration_by_force(body)

        self.calc_new_velocity(body, time)
        self.calc_new_position(body, time)

    def calc_force_of_gravity(self, body1: Body, body2: Body) -> None:
        """
        Calculates and applies the gravitational force between two bodies.

        Args:
            body1 (Body): The first body.
            body2 (Body): The second body.

        Raises:
            ValueError: If either body's mass is zero or negative.
        """
        if body1.mass <= 0.0 or body2.mass <= 0.0:
            raise ValueError("Mass must be greater than zero.")
        else:
            # Compute the distance vector between the two bodies
            dist_x = body1.position[0] - body2.position[0]
            dist_y = body1.position[1] - body2.position[1]
            distance = (dist_x**2 + dist_y**2)**0.5

            # Compute the magnitude of the gravitational force: F = G * m1 * m2 / r^2
            force_magnitude = (self.universal_grav_const * body1.mass * body2.mass) / (distance**2)

            # Decompose force vector into x and y components
            force_x = force_magnitude * (dist_x / distance)
            force_y = force_magnitude * (dist_y / distance)

            # Apply equal and opposite forces to the two bodies
            body1.force = (body1.force[0] - force_x, body1.force[1] - force_y)
            body2.force = (body2.force[0] + force_x, body2.force[1] + force_y)
