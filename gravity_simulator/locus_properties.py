class LocusProperties:
    """
    A class to store properties for drawing the trajectory (locus) of a celestial body.

    Attributes:
        track_locus (bool): Whether to track and draw the trajectory of the body.
        width (float): The width (radius) of the trajectory points to be drawn.
        color (tuple): RGB color of the trajectory path.
    """

    def __init__(self, track_locus: bool = False, width: float = 1, color: tuple = (255, 255, 255)):
        """
        Initializes the LocusProperties object.

        Args:
            track_locus (bool, optional): Flag to determine if the locus should be tracked. Defaults to False.
            width (float, optional): Width of the locus point to draw. Defaults to 1.
            color (tuple, optional): RGB color of the locus. Defaults to white (255, 255, 255).
        """
        self.track_locus = track_locus  # Enable or disable tracking of the body's trajectory
        self.width = width              # Width of each point drawn in the trajectory
        self.color = color              # Color of the trajectory