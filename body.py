from locus_properties import LocusProperties

class Body:
    """
    Represents a celestial body with physical properties and state used in gravitational simulations.

    Attributes:
        name (str): Name of the body (e.g., Earth, Sun).
        mass (float): Mass of the body in kilograms.
        radius (float): Radius of the body (used for rendering).
        color (tuple): RGB color for visual representation.
        velocity (tuple): Velocity vector (vx, vy) in m/s.
        position (tuple): Position vector (x, y) in meters.
        acceleration (tuple): Acceleration vector (ax, ay) in m/s^2.
        force (tuple): Net force vector (Fx, Fy) in newtons.
        locus (list): List of past positions for drawing the trajectory.
        locus_properties (LocusProperties): Settings for drawing the trajectory.
        scale (float): Scale factor for visual rendering.
    """

    def __init__(self,
                 name: str,
                 mass: float,
                 radius: float,
                 color: tuple,
                 velocity: tuple = (0, 0),
                 position: tuple = (0, 0),
                 acceleration: tuple = (0, 0),
                 force: tuple = (0, 0),
                 locus_properties: LocusProperties = LocusProperties(),
                 scale: float = 800):
        """
        Initializes a new instance of the Body class.

        Args:
            name (str): Name of the celestial body.
            mass (float): Mass in kilograms.
            radius (float): Radius for rendering.
            color (tuple): RGB color.
            velocity (tuple, optional): Initial velocity vector. Defaults to (0, 0).
            position (tuple, optional): Initial position vector. Defaults to (0, 0).
            acceleration (tuple, optional): Initial acceleration vector. Defaults to (0, 0).
            force (tuple, optional): Initial force vector. Defaults to (0, 0).
            locus_properties (LocusProperties, optional): Settings for drawing the trajectory.
            scale (float, optional): Scale factor for rendering. Defaults to 800.
        """
        self.name = name
        self.color = color
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.position = position
        self.acceleration = acceleration
        self.force = force
        self.locus = []  # Stores past positions for trajectory visualization
        self.locus_properties = locus_properties
        self.scale = scale

    def __repr__(self):
        """
        Returns a string representation of the Body instance.
        """
        return f"Body(name={self.name}, mass={self.mass}, radius={self.radius}, color={self.color})"
