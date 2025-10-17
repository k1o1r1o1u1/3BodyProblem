# 🌍 3D Gravitational Simulation

This project visualizes the **gravitational interaction** between multiple bodies in **3D space** using Python and Matplotlib.  
Each planet moves under Newton’s law of universal gravitation, showing dynamic orbits, trails, and real-time motion vectors.

---

## 🚀 Features

- Real-time 3D simulation of multiple celestial bodies  
- Adjustable **gravity constant (G)** and **time step (dt)**  
- Smooth **orbit trails** with fading motion history  
- **Interactive keyboard controls**:
  - **Spacebar** → Pause / Resume  
  - **Right Arrow** → Step forward one frame (when paused)  
  - **R** → Reset simulation to initial state  
- Simple, clean visualization with color-coded planets and labeled velocity vectors  

---

## 🧠 Physics Overview

The simulation uses Newton’s law of gravitation:

\[
F = G \frac{m_1 m_2}{r^2}
\]

Each planet’s position and velocity are updated iteratively using basic **Euler integration**:
```python
p.vx += (Fx / p.mass) * dt
p.x += p.vx * dt
