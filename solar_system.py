from bodies import bodies
from constants import TIMESTEP

class SolarSystem:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def get_bodies(self):
        return self.bodies

    def __str__(self):
        return f"Solar System with {len(self.bodies)} bodies."
    
    def add_bodies(self, new_bodies):
        for body in new_bodies:
            self.add_body(body)
            
    def add_all_bodies(self):
        self.add_bodies(bodies)
        
    def update_bodies(self, physics):
        for body in self.bodies:
            body.force = (0, 0)  # Reset force for each body
            
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                first_body = self.bodies[i]
                second_body = self.bodies[j]
                
                # Calculate the force of gravity between the two bodies
                physics.calc_force_of_gravity(first_body, second_body)
        
        for body in self.bodies:
            physics.calc_new_velocity_and_pos(body, TIMESTEP)
            
