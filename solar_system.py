from bodies import bodies
from constants import TIMESTEP, AU, CENTRE
from physics import Physics

class SolarSystem:
    def __init__(self):
        self.bodies = []
        self.physics = Physics()
        self.CENTRAL_BODY_IDX = 0
        self.SCALE = 800 / AU  # Default scale for the solar system

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
        
    def update_bodies(self):
        for body in self.bodies:
            body.force = (0, 0)  # Reset force for each body
            
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                first_body = self.bodies[i]
                second_body = self.bodies[j]
                
                # Calculate the force of gravity between the two bodies
                self.physics.calc_force_of_gravity(first_body, second_body)
        
        for body in self.bodies:
            self.physics.calc_new_velocity_and_pos(body, TIMESTEP)
            
    def set_scale(self):
        try:
            for idx, body in enumerate(self.bodies):
                print(f"IDX: {idx} - {body.name}")
            
            self.CENTRAL_BODY_IDX = int(input("Enter the body index to focus the camera on: "))
            
            (self.SCALE, self.CENTRAL_BODY_IDX) = (self.bodies[self.CENTRAL_BODY_IDX].scale / AU, self.CENTRAL_BODY_IDX)  # Scale based on the central body
        except Exception as e:
            print(f"Invalid input: {e}. Using default scale.")
        
    def get_scaled_pos(self, position: tuple, centre_on_pos = None) -> tuple:
        if centre_on_pos == None:
            centre_on_pos = bodies[self.CENTRAL_BODY_IDX].position
        return (
            (position[0] - centre_on_pos[0]) * self.SCALE + CENTRE[0],
            (position[1] - centre_on_pos[1]) * self.SCALE + CENTRE[1]
        )
                
    def draw_bodies(self, pygame, screen) -> None:
        for body in self.bodies:
            pygame.draw.circle(screen, body.color, self.get_scaled_pos(body.position), body.radius)
            
            curr_locus_properties = body.locus_properties
            if curr_locus_properties.track_locus:
                for pos in body.locus:
                    pygame.draw.circle(screen, curr_locus_properties.color, self.get_scaled_pos(pos), curr_locus_properties.width)
