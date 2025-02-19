import numpy as np

class Array():
    def __init__(self, name, array_type, num_elements, frequencies, steering_angle, position, meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y,
                  element_spacing = None, radius = None, arc_angle = None):
        self.start_array(name, array_type, num_elements, frequencies, steering_angle, position, meshgird_x, meshgrid_y, beam_profile_x, beam_profile_y,
                          element_spacing, radius, arc_angle)

    def start_array(self, name,  array_type, number_of_elements, frequencies, steering_angle, position, X, Y, beam_profile_x, beam_profile_y,
                     element_spacing = None, radius = None, arc_angle = None):
        self.name = name
        self.number_of_elements = number_of_elements
        self.position = position
        self.frequencies = frequencies
        self.steering_angle = steering_angle
        self.elements_spacing = element_spacing
        self.radius = radius
        self.arc_angle = arc_angle
        self.array_type = array_type
        self.wavelengths = [1.0 / x if x != 0 else 1.0 /(x+ 1e-12) for x in self.frequencies]
        if array_type == "Linear":
            phased_array = [
                {
                    "type": "linear",
                    "num_elements": self.number_of_elements,
                    "element_spacing": element_spacing,
                    "frequencies": self.frequencies,
                    "wavelengths": self.wavelengths,
                    "steering_angle": self.steering_angle,  # Degrees
                    "position": self.position,
                }]
        elif array_type == "Curved":
            phased_array = [
            {
                "type": "curved",
                "num_elements": self.number_of_elements,
                "frequencies": self.frequencies,
                "wavelengths": self.wavelengths,
                "steering_angle": self.steering_angle,
                "position": self.position,
                "radius": radius,
                "arc_angle": arc_angle,  # Degrees
            }
                ]

        self.array_data = {}
        for array in phased_array:
            self.number_of_elements = array["num_elements"]
            self.wavelengths = array["wavelengths"]
            self.frequencies = array["frequencies"]
            self.steering_angle = np.radians(array["steering_angle"])
            center_x, center_y = array["position"]

            if array["type"] == "linear":
                element_spacing = array["element_spacing"] * self.wavelengths[0]
                source_positions = [
                    np.array([i * element_spacing - (self.number_of_elements - 1) * element_spacing / 2, 0])
                    for i in range(self.number_of_elements)
                ]
                self.unit_placements = [
                    np.array([i * element_spacing - (self.number_of_elements - 1) * element_spacing / 2, 0])
                    for i in range(self.number_of_elements)
                ]
            elif array["type"] == "curved":
                arc_angle = np.radians(array["arc_angle"])
                radius = array["radius"]
                angles = np.linspace(-arc_angle / 2, arc_angle / 2, self.number_of_elements)
                source_positions = [
                    np.array([radius * np.sin(angle), radius * np.cos(angle)]) for angle in angles
                ]
                self.unit_placements = [
                    np.array([i * 0.5 * self.wavelengths[0] - (self.number_of_elements - 1) * 0.5* self.wavelengths[0] / 2, 0])
                    for i in range(self.number_of_elements)
                ]

            source_positions = [pos + np.array([center_x, center_y]) for pos in source_positions]
            self.unit_placements = [pos + np.array([center_x, center_y]) for pos in self.unit_placements]
            distances = [
                np.sqrt((X - pos[0])**2 + (Y - pos[1])**2) for pos in self.unit_placements
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
                for pos in self.unit_placements
            ]
            self.array_data = {
                "positions": np.array(source_positions),
                "distances": distances,
                "beam_distances": beam_distances,
                "phase_shifts": self.phase_shifts,
                "frequencies": self.frequencies,
                "wavelengths": self.wavelengths,
                "steering_angle": self.steering_angle,
                "unit_placements": np.array(self.unit_placements)
            }
    def update_steering_angle(self):
        # source_positions = self.array_data["positions"]
        self.phase_shifts = [
                [
                    2 * np.pi / wavelength * pos[0] * np.sin(self.steering_angle)
                    + 2 * np.pi / wavelength * pos[1] * np.cos(self.steering_angle)
                    for wavelength in self.wavelengths
                ]
                for pos in self.unit_placements
            ]
        self.array_data["phase_shifts"] = self.phase_shifts
        self.array_data["steering_angle"] = self.steering_angle
