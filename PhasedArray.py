import numpy as np
class PhasedArray():
    def __init__(self, name, type, number_of_elements, position, frequencies, meshgrid, phase_shifts = None,
                  elements_spacing = None, steering_angle = None, raduis = None, arc_angle = None):
        self.name = name
        self.type = type
        self.number_of_elements = number_of_elements
        self.elements_spacing = elements_spacing
        self.frequencies = np.array(frequencies)
        self.wavelengths = 1 / (self.frequencies + 1e-9)
        self.wavelengths = list(self.wavelengths)
        self.steering_angle = steering_angle  #degrees
        self.position = position
        self.radius = raduis
        self.arc_angle= arc_angle
        self.mesh_grid = meshgrid
        self.distances = None
        self.source_positions = None
        self.phase_shifts = phase_shifts
        self.beam_distances = None
        self.update_array()

    def update_array(self):
        if self.type == "Linear":
            self.elements_spacing = self.elements_spacing * self.wavelengths[0]
            source_positions = [
                np.array([i * self.elements_spacing - (self.number_of_elements - 1) * self.elements_spacing / 2, 0])
                for i in range(self.number_of_elements)
            ]
        if self.type == "Curved":
            self.arc_angle = np.radians(self.arc_angle)
            angles = np.linspace(-self.arc_angle / 2, self.arc_angle / 2, self.number_of_elements)
            self.source_positions = [
                np.array([self.radius * np.sin(angle), self.radius * np.cos(angle)]) for angle in angles
            ]

        self.source_positions = np.array([pos + np.array([self.position[0], self.position[1]]) for pos in source_positions])

        self.distances = [ 
            np.sqrt((self.mesh_grid[0] - pos[0])**2 + (self.mesh_grid[1] - pos[1])**2) for pos in source_positions
                                                                      ]
        
        if self.steering_angle is not None:
            
            self.steering_angle = np.radians(self.steering_angle)
            self.phase_shifts = [
                [
                    2 * np.pi / wavelength * pos[0] * np.sin(self.steering_angle)
                    + 2 * np.pi / wavelength * pos[1] * np.cos(self.steering_angle)
                    for wavelength in self.wavelengths
                ]
                for pos in source_positions
            ]

    def calculate_beam_distances(self, beam_profile_x, beam_profile_y):
        self.beam_distances = [
        np.sqrt((beam_profile_x - self.position[0])**2 + (beam_profile_y - self.position[1])**2)
                                ]
