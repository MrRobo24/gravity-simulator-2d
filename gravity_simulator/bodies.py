from .body import Body
from .constants import AU, YELLOW, BLUE, GREY
from .locus_properties import LocusProperties

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

bodies = [sun, earth, moon, venus, mercury, mars]