from locus_properties import LocusProperties

class Body:
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
        self.name = name
        self.color = color
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.position = position
        self.acceleration = acceleration
        self.force = force
        self.locus = []
        self.locus_properties = locus_properties
        self.scale = scale

    def __repr__(self):
        return f"Body(name={self.name}, mass={self.mass}, radius={self.radius}, color={self.color})"