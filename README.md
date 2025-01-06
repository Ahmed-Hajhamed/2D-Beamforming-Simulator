# 2D Beamforming Simulator

## Overview
Beamforming is a crucial technology in modern wireless communications, 5G, radar, sonar, and biomedical applications such as ultrasound imaging and tumor ablation. It relies on delays/phase-shifts and constructive/destructive interference to direct signals efficiently.

This simulator provides an interactive platform to explore beamforming concepts by allowing users to customize system parameters and visualize the resulting beam profiles in real time.
![Screen Shot 2025-01-06 at 1 49 39 PM](https://github.com/user-attachments/assets/569142ce-cc10-4cd6-a668-73f22956ba57)


## Features
### 1. **Customizable Beamforming Parameters**
- Adjust the number of transmitters and receivers.
- Apply different delays and phase shifts.
- Select multiple operating frequencies and their values in real time.
- Choose between linear and curved phased array geometries with customizable curvature parameters.
  
![Screen Shot 2025-01-06 at 1 50 01 PM](https://github.com/user-attachments/assets/2ae5013c-d704-4f07-b72e-11efba6da980)

### 2. **Real-time Visualization**
- View constructive and destructive interference maps.
- Display synchronized beam profiles in multiple visualization panels.
  
![Screen Shot 2025-01-06 at 1 50 15 PM](https://github.com/user-attachments/assets/abd8df3a-7d4b-4879-b7cb-a3ade13c71f7)

### 3. **Multiple Phased Array Units**
- Add and configure multiple phased arrays within the system.
- Customize the location and parameters of each unit independently.
  
![Screen Shot 2025-01-06 at 1 51 40 PM](https://github.com/user-attachments/assets/9f7cc29c-b3fd-4629-91e0-41e5f33df9ab)

### 4. **Predefined Scenarios**
- Load and modify at least three parameter setting files inspired by:
  - **5G Beam Steering**: Explore directional signal transmission for improved wireless communication.
  - **Ultrasound Imaging**: Simulate medical imaging techniques used in diagnostics.
  - **Tumor Ablation**: Model focused energy delivery for non-invasive treatments.
    
![Screen Shot 2025-01-06 at 1 54 16 PM](https://github.com/user-attachments/assets/dabf456f-4378-44a1-98f2-a2b660e2746f)

## Getting Started
### Prerequisites
- Python with relevant scientific computing libraries such as PyQt5, NumPy, and Matplotlib.

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Ahmed-Hajhamed/2D-Beamforming-Simulator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the simulator:
   ```sh
   python main.py
   ```

## Usage
- Open the simulator interface.
- Adjust the beamforming parameters as needed.
- Load predefined scenarios or create new ones.
- Observe the real-time beam steering and interference visualization.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## References
- [Beamforming Concepts](https://en.wikipedia.org/wiki/Beamforming)

