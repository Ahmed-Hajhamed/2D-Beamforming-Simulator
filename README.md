# 2D Beamforming Simulator

## Overview
Beamforming is a crucial technology in modern wireless communications, 5G, radar, sonar, and biomedical applications such as ultrasound imaging and tumor ablation. It relies on delays/phase-shifts and constructive/destructive interference to direct signals efficiently.

This simulator provides an interactive platform to explore beamforming concepts by allowing users to customize system parameters and visualize the resulting beam profiles in real time.

## Features
### 1. **Customizable Beamforming Parameters**
- Adjust the number of transmitters and receivers.
- Apply different delays and phase shifts.
- Select multiple operating frequencies and their values in real time.
- Choose between linear and curved phased array geometries with customizable curvature parameters.

### 2. **Real-time Visualization**
- View constructive and destructive interference maps.
- Display synchronized beam profiles in multiple visualization panels.

### 3. **Multiple Phased Array Units**
- Add and configure multiple phased arrays within the system.
- Customize the location and parameters of each unit independently.

### 4. **Predefined Scenarios**
- Load and modify at least three parameter setting files inspired by:
  - **5G Beam Steering**: Explore directional signal transmission for improved wireless communication.
  - **Ultrasound Imaging**: Simulate medical imaging techniques used in diagnostics.
  - **Tumor Ablation**: Model focused energy delivery for non-invasive treatments.

## Getting Started
### Prerequisites
- Python with relevant scientific computing libraries such as PyQt5, NumPy, and Matplotlib.

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/2D-beamforming-simulator.git
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

