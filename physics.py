from body import Body

class Physics:
    def __init__(self):
        self.acc_due_to_grav = 9.81  # Acceleration due to gravity in m/s^2
        self.universal_grav_const = 1  # Universal gravitational constant in m^3 kg^-1 s^-2
        self.meter_to_pixel = 1 # Conversion factor from meters to pixels 1 m = 100 pixels
    
    def to_pixel(self, value: float) -> float:
        return value * self.meter_to_pixel
    
    def to_meter(self, value: float) -> float:
        return value / self.meter_to_pixel
    
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
            dis_x = body.velocity[0] * time + 0.5 * body.acceleration[0] * time**2
            dis_y = body.velocity[1] * time + 0.5 * body.acceleration[1] * time**2
            new_x = body.position[0] + self.to_pixel(dis_x)
            new_y = body.position[1] + self.to_pixel(dis_y)
            body.position = (new_x, new_y)
            
    def calc_new_velocity(self, body: Body, time: float) -> None:
        if time <= 0.0:
            raise ValueError("Time must be greater than zero.")
        else:
            # Calculate new velocity using the formula: v = u + at
            v_x = body.velocity[0] + body.acceleration[0] * time
            v_y = body.velocity[1] + body.acceleration[1] * time
            body.velocity = (v_x, v_y)
    
    def calc_new_position_and_velocity(self, body: Body, time: float) -> None:
        if (body.force != (0, 0)):
            self.calc_accelaration_by_force(body)
            
        self.calc_new_position(body, time)
        self.calc_new_velocity(body, time)
        
    def calc_force_of_gravity(self, body1: Body, body2: Body) -> None:
        if body1.mass <= 0.0 or body2.mass <= 0.0:
            raise ValueError("Mass must be greater than zero.")
        else:
            # Calculate the distance between the two bodies
            dist_x = self.to_meter(body2.position[0] - body1.position[0])
            dist_y = self.to_meter(body2.position[1] - body1.position[1])
            distance = (dist_x**2 + dist_y**2)**0.5
            
            # Calculate the gravitational force using formula F = G * (m1 * m2) / r^2
            force_magnitude = (self.universal_grav_const * body1.mass * body2.mass) / (distance**2)
            
            # Calculate the force vector
            force_x = force_magnitude * (dist_x / distance)
            force_y = force_magnitude * (dist_y / distance)
            
            # Update the forces on both bodies
            body1.force = (body1.force[0] + force_x, body1.force[1] + force_y)
            body2.force = (body2.force[0] - force_x, body2.force[1] - force_y)