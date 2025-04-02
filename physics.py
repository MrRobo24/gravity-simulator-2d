from body import Body

class Physics:
    def __init__(self):
        self.acc_due_to_grav = 9.81  # Acceleration due to gravity in m/s^2
        self.universal_grav_const = 6.67430e-11  # Universal gravitational constant in m^3 kg^-1 s^-2
        self.meter_to_pixel = 100  # Conversion factor from meters to pixels 1 m = 100 pixels
    
    def calc_accelaration_by_force(self, body: Body) -> None:
        if body.mass <= 0.0:
            raise ValueError("Mass must be greater than zero.")
        else:
            body.acceleration = (body.force[0] / body.mass, body.force[1] / body.mass)
        
    def calc_new_position(self, body: Body, time: float) -> None:
        if time <= 0.0:
            raise ValueError("Time must be greater than zero.")
        else:
            # Calculate new postion using the formula: s = ut + 1/2 at^2
            new_x = body.position[0] + body.velocity[0] * time + 0.5 * body.acceleration[0] * time**2
            new_y = body.position[1] + body.velocity[1] * time + 0.5 * body.acceleration[1] * time**2
            body.position = (new_x, new_y)