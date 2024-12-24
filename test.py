
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_elements = 16       # Number of transmitters in a linear array
element_spacing = 0.5    # Element spacing (wavelengths)
wavelength = 1.0         # Wavelength of the signal
frequency = 1.0          # Frequency (arbitrary units)
grid_size = 300         # Resolution of the heatmap
steering_angle = 30     # Beam steering angle (degrees)
time_step = 0.1          # Time step for phase animation

# Create a 2D grid for the heatmap
x = np.linspace(-10, 10, grid_size)  # X-axis
y = np.linspace(-10, 10, grid_size)  # Y-axis
X, Y = np.meshgrid(x, y)             # 2D grid

# Angular positions for polar beam profile
theta = np.linspace(0, 2 * np.pi, grid_size)

# Function to compute wave interference pattern
def compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle):
    k = 2 * np.pi / wavelength  # Wavenumber
    omega = 2 * np.pi * frequency  # Angular frequency
    steering_radians = np.deg2rad(steering_angle)
    
    # Transmitter positions (linear array)
    element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2
    
    # Total field summation
    field = np.zeros_like(X, dtype=np.float64)
    for pos in element_positions:
        # Distance-based delay and phase steering
        distance = np.sqrt((X - pos)**2 + Y**2)
        phase_delay = k * (pos * np.sin(steering_radians))
        field += np.sin(k * distance - omega * t + phase_delay)
    
    return field

# Function to compute the polar beam profile (array factor)
def compute_polar_pattern(num_elements, element_spacing, wavelength, steering_angle):
    k = 2 * np.pi / wavelength  # Wavenumber
    steering_radians = np.deg2rad(steering_angle)
    
    # Element positions
    element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2
    
    # Array factor calculation
    array_factor = np.zeros_like(theta, dtype=np.complex128)
    for pos in element_positions:
        phase_shift = k * (pos * np.sin(theta)) - k * (pos * np.sin(steering_radians))
        array_factor += np.exp(1j * phase_shift)
    
    return np.abs(array_factor) / num_elements  # Normalize the array factor

# Set up the figure with two subplots
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121)  # Heatmap subplot
ax2 = fig.add_subplot(122, projection='polar')  # Polar plot for beam profile

# Heatmap axis
heatmap = ax1.imshow(np.zeros_like(X), extent=[-10, 10, -10, 10], origin='lower',
                     cmap='RdBu', vmin=-1, vmax=1, interpolation='bilinear')
ax1.set_title("Real-Time Beamforming Heatmap")
ax1.set_xlabel("X Position (wavelengths)")
ax1.set_ylabel("Y Position (wavelengths)")

# Polar beam profile axis
polar_line, = ax2.plot([], [], color='red', linewidth=2)
ax2.set_title("Polar Beam Profile")

# Function to initialize the polar beam profile
def init():
    polar_line.set_data([], [])
    return heatmap, polar_line

# Animation function
def update(frame):
    t = frame * time_step  # Update time
    
    # Update heatmap
    field = compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle)
    heatmap.set_data(field)
    ax1.set_title(f"Real-Time Heatmap - Frame {frame}")
    
    # Update polar beam profile
    polar_pattern = compute_polar_pattern(num_elements, element_spacing, wavelength, steering_angle)
    polar_line.set_data(theta, polar_pattern)
    
    return heatmap, polar_line

# Real-Time Animation
ani = FuncAnimation(fig, update, init_func=init, frames=200, interval=50, blit=True)
plt.tight_layout()
plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # # Phased Array Parameters
# # num_elements = 16        # Number of transmitters in a linear array
# # element_spacing = 0.5    # Element spacing (in wavelengths)
# # wavelength = 1.0         # Wavelength of the signal
# # frequency = 1e9          # Frequency (e.g., 1 GHz)
# # steering_angle = 30       # Beam steering angle (degrees)
# # grid_size = 400          # Grid resolution for the heatmap

# # # Create a 2D grid for visualization
# # x = np.linspace(-10, 10, grid_size)  # x-axis
# # y = np.linspace(-10, 10, grid_size)  # y-axis
# # X, Y = np.meshgrid(x, y)             # 2D grid

# # # Calculate the phase difference across the array elements
# # def compute_interference(X, Y, num_elements, element_spacing, wavelength, steering_angle):
# #     k = 2 * np.pi / wavelength  # Wavenumber
# #     steering_radians = np.deg2rad(steering_angle)

# #     # Array positions along x-axis (linear array)
# #     element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2

# #     # Total field summation
# #     field = np.zeros_like(X, dtype=np.complex128)
# #     for pos in element_positions:
# #         phase_shift = k * (pos * np.sin(steering_radians))  # Phase shift for steering
# #         distance = np.sqrt((X - pos)**2 + Y**2)  # Distance to grid point
# #         field += np.exp(1j * (k * distance + phase_shift)) / (distance + 1e-6)  # Avoid divide-by-zero

# #     return np.abs(field)  # Return magnitude of the resulting field

# # # Compute the field intensity (constructive/destructive interference map)
# # field_intensity = compute_interference(X, Y, num_elements, element_spacing, wavelength, steering_angle)

# # # Normalize for visualization
# # field_intensity /= np.max(field_intensity)

# # # Extract the beam profile along the centerline (Y = 0)
# # centerline_index = grid_size // 2
# # beam_profile = field_intensity[centerline_index, :]

# # # Plot the heatmap
# # plt.figure(figsize=(12, 6))

# # # Heatmap (2D interference map)
# # plt.subplot(1, 2, 1)
# # plt.imshow(field_intensity, extent=[-10, 10, -10, 10], origin='lower', cmap='RdBu', aspect='auto')
# # plt.colorbar(label='Normalized Intensity')
# # plt.title(f"Beamforming Heatmap (Steering Angle = {steering_angle}°)")
# # plt.xlabel("X Position (wavelengths)")
# # plt.ylabel("Y Position (wavelengths)")

# # # Beam Profile (centerline intensity)
# # plt.subplot(1, 2, 2)
# # plt.plot(x, beam_profile, color='red', linewidth=2)
# # plt.title("Beam Profile Along Centerline (Y = 0)")
# # plt.xlabel("X Position (wavelengths)")
# # plt.ylabel("Normalized Intensity")
# # plt.grid()

# # plt.tight_layout()
# # plt.show()

# # # Phased Array Parameters
# # num_elements = 16        # Number of transmitters in a linear array
# # element_spacing = 0.5    # Element spacing (in wavelengths)
# # wavelength = 1.0         # Wavelength of the signal
# # steering_angle = 0       # Initial beam steering angle (degrees)
# # grid_size = 400          # Grid resolution for the heatmap

# # # Polar Grid
# # theta = np.linspace(0, 2 * np.pi, grid_size)  # Angular positions
# # r = np.linspace(0, 1, 1)  # Normalized radius (polar plot uses direction)

# # def compute_polar_pattern(num_elements, element_spacing, wavelength, steering_angle):
# #     k = 2 * np.pi / wavelength  # Wavenumber
# #     steering_radians = np.deg2rad(steering_angle)

# #     # Array positions
# #     element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2

# #     # Compute array factor in polar coordinates
# #     array_factor = np.zeros_like(theta, dtype=np.complex128)
# #     for pos in element_positions:
# #         phase_shift = k * (pos * np.sin(theta)) - k * (pos * np.sin(steering_radians))
# #         array_factor += np.exp(1j * phase_shift)

# #     return np.abs(array_factor) / num_elements  # Normalize the array factor

# # # Real-Time Polar Visualization
# # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
# # line, = ax.plot([], [], color='red', linewidth=2)
# # ax.set_title("Real-Time Beam Profile (Polar)")

# # def update(frame):
# #     global steering_angle
# #     steering_angle = (steering_angle + 1) % 360  # Increment angle (0 to 360 degrees)
# #     pattern = compute_polar_pattern(num_elements, element_spacing, wavelength, steering_angle)
# #     ax.clear()
# #     ax.plot(theta, pattern, color='red', linewidth=2)
# #     ax.set_title(f"Beam Profile (Polar) - Steering Angle: {steering_angle}°")

# # ani = FuncAnimation(fig, update, interval=100)  # Update every 100 ms
# # plt.show()

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # # Parameters
# # num_elements = 1      # Number of transmitters in a linear array
# # element_spacing = 0.5    # Element spacing (wavelengths)
# # wavelength = 1.0         # Wavelength of the signal
# # frequency = 1.0          # Frequency (arbitrary units)
# # grid_size = 300          # Resolution of the heatmap
# # steering_angle = 0     # Beam steering angle (degrees)
# # time_step = 0.1          # Time step for phase animation

# # # Create a 2D grid for the heatmap
# # x = np.linspace(-10, 10, grid_size)
# # y = np.linspace(-10, 10, grid_size)
# # X, Y = np.meshgrid(x, y)

# # # Function to compute wave interference pattern
# # def compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle):
# #     k = 2 * np.pi / wavelength  # Wavenumber
# #     omega = 2 * np.pi * frequency  # Angular frequency
# #     steering_radians = np.deg2rad(steering_angle)
    
# #     # Transmitter positions (linear array)
# #     element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2
    
# #     # Total field summation
# #     field = np.zeros_like(X, dtype=np.float64)
# #     for pos in element_positions:
# #         # Distance-based delay and phase steering
# #         distance = np.sqrt((X - pos)**2 + Y**2)
# #         phase_delay = k * (pos * np.sin(steering_radians))
# #         field += np.sin(k * distance - omega * t + phase_delay)
    
# #     return field

# # # Set up the figure and axis for animation
# # fig, ax = plt.subplots(figsize=(8, 8))
# # heatmap = ax.imshow(np.zeros_like(X), extent=[-10, 10, -10, 10], origin='lower',
# #                     cmap='RdBu', vmin=-1, vmax=1, interpolation='bilinear')
# # ax.set_title("Real-Time Beamforming Heatmap")
# # ax.set_xlabel("X Position (wavelengths)")
# # ax.set_ylabel("Y Position (wavelengths)")

# # # Animation function
# # def update(frame):
# #     t = frame * time_step  # Update time
# #     field = compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle)
# #     heatmap.set_data(field)
# #     ax.set_title(f"Real-Time Beamforming Heatmap - Frame {frame}")
# #     return heatmap,

# # # Real-Time Animation
# # ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
# # plt.show()

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # # Parameters
# # num_elements = 16        # Number of transmitters in a linear array
# # element_spacing = 0.5    # Element spacing (wavelengths)
# # wavelength = 1.0         # Wavelength of the signal
# # frequency = 1.0          # Frequency (arbitrary units)
# # grid_size = 300          # Resolution of the heatmap
# # steering_angle = 30      # Beam steering angle (degrees)
# # time_step = 0.1          # Time step for phase animation

# # # Create a 2D grid for the heatmap
# # x = np.linspace(-10, 10, grid_size)  # X-axis
# # y = np.linspace(-10, 10, grid_size)  # Y-axis
# # X, Y = np.meshgrid(x, y)             # 2D grid

# # # Function to compute wave interference pattern
# # def compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle):
# #     k = 2 * np.pi / wavelength  # Wavenumber
# #     omega = 2 * np.pi * frequency  # Angular frequency
# #     steering_radians = np.deg2rad(steering_angle)
    
# #     # Transmitter positions (linear array)
# #     element_positions = np.arange(num_elements) * element_spacing - (num_elements - 1) * element_spacing / 2
    
# #     # Total field summation
# #     field = np.zeros_like(X, dtype=np.float64)
# #     for pos in element_positions:
# #         # Distance-based delay and phase steering
# #         distance = np.sqrt((X - pos)**2 + Y**2)
# #         phase_delay = k * (pos * np.sin(steering_radians))
# #         field += np.sin(k * distance - omega * t + phase_delay)
    
# #     return field

# # # Set up the figure with two subplots
# # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# # # Heatmap axis
# # heatmap = ax1.imshow(np.zeros_like(X), extent=[-10, 10, -10, 10], origin='lower',
# #                      cmap='RdBu', vmin=-1, vmax=1, interpolation='bilinear')
# # ax1.set_title("Real-Time Beamforming Heatmap")
# # ax1.set_xlabel("X Position (wavelengths)")
# # ax1.set_ylabel("Y Position (wavelengths)")

# # # Beam profile axis
# # line, = ax2.plot([], [], color='red', linewidth=2)
# # ax2.set_xlim(-10, 10)
# # ax2.set_ylim(-1, 1)
# # ax2.set_title("Beam Profile (Y = 0)")
# # ax2.set_xlabel("X Position (wavelengths)")
# # ax2.set_ylabel("Normalized Intensity")
# # ax2.grid()

# # # Function to initialize beam profile
# # def init():
# #     line.set_data([], [])
# #     return line,

# # # Animation function
# # def update(frame):
# #     t = frame * time_step  # Update time
    
# #     # Compute the field for the heatmap
# #     field = compute_wave_pattern(X, Y, t, num_elements, element_spacing, wavelength, steering_angle)
# #     heatmap.set_data(field)  # Update heatmap
    
# #     # Compute the beam profile (centerline at Y = 0)
# #     centerline_index = grid_size // 2
# #     beam_profile = field[centerline_index, :]  # Intensity along Y = 0
# #     line.set_data(x, beam_profile)  # Update beam profile

# #     ax1.set_title(f"Real-Time Heatmap - Frame {frame}")
# #     return heatmap, line

# # # Real-Time Animation
# # ani = FuncAnimation(fig, update, init_func=init, frames=200, interval=50, blit=True)
# # plt.tight_layout()
# # plt.show()

