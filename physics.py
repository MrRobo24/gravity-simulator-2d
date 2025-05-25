from body import Body

class Physics:
    def __init__(self):
        self.acc_due_to_grav = 9.81  # Acceleration due to gravity in m/s^2
        self.universal_grav_const = 6.67430e-11  # Universal gravitational constant in m^3 kg^-1 s^-2
    
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
            new_x = body.position[0] + body.velocity[0] * time
            new_y = body.position[1] + body.velocity[1] * time
            body.position = (new_x, new_y)
            body.locus.append(body.position)
            
    def calc_new_velocity(self, body: Body, time: float) -> None:
        if time <= 0.0:
            raise ValueError("Time must be greater than zero.")
        else:
            # Calculate new velocity using the formula: v = u + at
            v_x = body.velocity[0] + body.acceleration[0] * time
            v_y = body.velocity[1] + body.acceleration[1] * time
            body.velocity = (v_x, v_y)
    
    def calc_new_velocity_and_pos(self, body: Body, time: float) -> None:
        if (body.force != (0, 0)):
            self.calc_accelaration_by_force(body)
            
        self.calc_new_velocity(body, time)
        self.calc_new_position(body, time)
        
        
    def calc_force_of_gravity(self, body1: Body, body2: Body) -> None:
        if body1.mass <= 0.0 or body2.mass <= 0.0:
            raise ValueError("Mass must be greater than zero.")
        else:
            # Calculate the distance between the two bodies
            dist_x = body1.position[0] - body2.position[0]
            dist_y = body1.position[1] - body2.position[1]
            distance = (dist_x**2 + dist_y**2)**0.5
            
            # Calculate the gravitational force using formula F = G * (m1 * m2) / r^2
            force_magnitude = (self.universal_grav_const * body1.mass * body2.mass) / (distance**2)
            
            # Calculate the force vector
            force_x = force_magnitude * (dist_x / distance)
            force_y = force_magnitude * (dist_y / distance)
            
            # Update the forces on both bodies
            body1.force = (-force_x, -force_y)
            body2.force = (force_x, force_y)