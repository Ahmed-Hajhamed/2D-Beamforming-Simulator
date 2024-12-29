import numpy as np

class Array():
    def __init__(self, name, array_type, num_elements, frequencies, steering_angle, position, meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y,
                  element_spacing = None, radius = None, arc_angle = None):
        self.name = name
        self.number_of_elements = num_elements
        self.position = position
        self.frequencies = frequencies
        self.steering_angle = np.radians(steering_angle)
        
        self.radius = radius
        self.arc_angle = np.radians(arc_angle) if arc_angle != None else arc_angle
        self.array_type = array_type
        self.wavelengths = [1.0 / x if x != 0 else 1.0 /(x+ 1e-12) for x in self.frequencies]
        
        self.elements_spacing = element_spacing * self.wavelengths[0] if element_spacing != None else element_spacing

        self.start_array(meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y)
    def start_array(self, X, Y, beam_profile_x, beam_profile_y):
        
        if self.array_type == "Linear":

            array = {
                    "type": "linear",
                    "num_elements": self.number_of_elements,
                    "element_spacing": self.elements_spacing,
                    "frequencies": self.frequencies,
                    "wavelengths": self.wavelengths,
                    "steering_angle": self.steering_angle,  # Degrees
                    "position": self.position,
                }
            
        elif self.array_type == "Curved":
            array ={
                "type": "curved",
                "num_elements": self.number_of_elements,
                "frequencies": self.frequencies,
                "wavelengths": self.wavelengths,
                "steering_angle": self.steering_angle,
                "position": self.position,
                "radius": self.radius,
                "arc_angle": self.arc_angle,  # Degrees
            }

        self.array_data = {}

        center_x, center_y = array["position"]

        if array["type"] == "linear":
            source_positions = [
                np.array([i * self.elements_spacing - (self.number_of_elements - 1) * self.elements_spacing / 2, 0])
                for i in range(self.number_of_elements)
            ]

        elif array["type"] == "curved":
            arc_angle = np.radians(array["arc_angle"])
            radius = array["radius"]
            angles = np.linspace(-arc_angle / 2, arc_angle / 2, self.number_of_elements)
            source_positions = [
                np.array([radius * np.sin(angle), radius * np.cos(angle)]) for angle in angles
            ]
        source_positions = [pos + np.array([center_x, center_y]) for pos in source_positions]
        distances = [
            np.sqrt((X - pos[0])**2 + (Y - pos[1])**2) for pos in source_positions
        ]
        beam_distances = [
            np.sqrt((beam_profile_x - pos[0])**2 + (beam_profile_y - pos[1])**2)
            for pos in source_positions
        ]
        self.phase_shifts = [
            [
                2 * np.pi / wavelength * pos[0] * np.sin(self.steering_angle)
                + 2 * np.pi / wavelength * pos[1] * np.cos(self.steering_angle)
                for wavelength in self.wavelengths
            ]
            for pos in source_positions
        ]
        self.array_data = {
            "positions": np.array(source_positions),
            "distances": distances,
            "beam_distances": beam_distances,
            "phase_shifts": self.phase_shifts,
            "frequencies": self.frequencies,
            "wavelengths": self.wavelengths,
            "steering_angle": self.steering_angle,
        }


    def update_steerign_angle(self):
        element_spacing = self.elements_spacing * self.wavelengths[0]
        source_positions = [
            np.array([i * element_spacing - (self.number_of_elements - 1) * element_spacing / 2, 0])
            for i in range(self.number_of_elements)
        ]

        self.phase_shifts = [
                [
                    2 * np.pi / wavelength * pos[0] * np.sin(self.steering_angle)
                    + 2 * np.pi / wavelength * pos[1] * np.cos(self.steering_angle)
                    for wavelength in self.wavelengths
                ]
                for pos in source_positions
            ]
        
    def update_array(self, name, array_type, num_elements, frequencies, steering_angle, position, meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y,
                  element_spacing = None, radius = None, arc_angle = None):
        self.name = name
        self.number_of_elements = num_elements
        self.position = position
        self.frequencies = frequencies
        self.steering_angle = np.radians(steering_angle)
        
        self.radius = radius
        self.arc_angle = np.radians(arc_angle) if arc_angle != None else arc_angle
        self.array_type = array_type
        self.wavelengths = [1.0 / x if x != 0 else 1.0 /(x+ 1e-12) for x in self.frequencies]
        
        self.elements_spacing = element_spacing * self.wavelengths[0] if element_spacing != None else element_spacing

        self.start_array(meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y)