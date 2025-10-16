3D Planetary System Simulation
A real-time 3D gravitational simulation of multiple planets interacting through Newtonian gravity, built with Python and Matplotlib.

https://via.placeholder.com/800x400/000000/FFFFFF?text=3D+Planetary+Simulation

Features
3D Visualization: Real-time 3D rendering of planetary motion

Physics Simulation: Accurate gravitational forces between all bodies

Interactive Controls: Pause, step-through, and reset functionality

Visual Effects:

Color-coded planets with orbit trails

Velocity vector visualization

Planet labeling

Customizable Parameters: Adjustable masses, velocities, and initial positions

Requirements
bash
python >= 3.6
matplotlib >= 3.0
numpy
Installation
Clone or download the script

Install required packages:

bash
pip install matplotlib numpy
Usage
Run the simulation:

bash
python planetary_simulation.py
Controls
Spacebar: Pause/Resume simulation

Right Arrow: Single step forward (when paused)

R: Reset simulation to initial state

Code Structure
Planet Class
Stores position, velocity, mass, and visual properties

Maintains orbit history for trail effects

State management for reset functionality

Physics Engine
Gravitational Force: Newtonian gravity with softening parameter

Numerical Integration: Basic Euler integration for motion

Collision Handling: Softened potential prevents numerical instability

Visualization
3D scatter plots for planets

Line plots for orbit trails

Quiver plots for velocity vectors

Real-time animation with Matplotlib

Customization
Adding Planets
Modify the orig list in the initialization section:

python
Planet(x, y, z, radius, color, mass, vx, vy, vz)
Adjusting Physics
G: Gravitational constant (default: 0.1)

dt: Time step (default: 0.1)

epsilon: Softening parameter to prevent numerical issues

Visual Settings
MAX_TRAIL: Length of orbit history (default: 300)

Colors, sizes, and labels can be modified in the Planet initialization

Example Configuration
The default simulation includes three planets:

Red Planet: Mass 40, initial velocity (1.0, 0.5, 0.5)

Green Planet: Mass 40, initial velocity (0.0, -0.5, 0.3)

Blue Planet: Mass 40, initial velocity (-1.0, -0.3, 0.0)

Educational Applications
This simulation demonstrates:

Newton's Law of Universal Gravitation

N-body problem dynamics

Numerical integration methods

Conservation laws in orbital mechanics

3D vector mathematics

Limitations
Uses basic Euler integration (consider Verlet or RK4 for better accuracy)

No relativistic effects

Simplified collision handling

Performance may decrease with many bodies

Extensions
Potential enhancements:

Add user interface for real-time parameter adjustment

Implement different numerical integrators

Add collision detection and response

Include energy conservation monitoring

Export trajectory data for analysis

License
Open source - feel free to modify and distribute for educational purposes.

