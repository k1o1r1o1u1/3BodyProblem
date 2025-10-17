# 🌌 3D Gravitational Simulation

A Python-based **3D N-body simulation** that visualizes gravitational interactions between multiple planets.  
This simulation models Newtonian gravity in real-time using `matplotlib`’s 3D animation tools.

---

## 📘 Overview

This project demonstrates how celestial bodies move under mutual gravitational forces.  
Each planet is defined by its mass, position, and velocity, and all interactions are calculated using Newton's Law of Universal Gravitation.

The simulation is **interactive**, allowing you to pause, step through frames, or reset the system to its initial state.

---

## ⚙️ Features

✅ Real-time 3D visualization with smooth animation  
✅ Dynamic orbit trails for each planet  
✅ Adjustable gravitational constant (G) and time step (dt)  
✅ Interactive keyboard controls  
✅ Velocity vectors and labeled planet markers  
✅ Easy customization — add or remove planets, change initial conditions, and visualize their motion

---

## 🎮 Controls

| Key | Action |
|-----|---------|
| **Spacebar** | Pause / Resume simulation |
| **→ (Right Arrow)** | Advance one frame (when paused) |
| **R** | Reset all planets to initial positions |

---

## 🧠 Physics Background

The motion is governed by **Newton’s Law of Universal Gravitation**:

\[
F = G \frac{m_1 m_2}{r^2}
\]

Each planet experiences the sum of forces from all others.  
Acceleration and velocity are updated using **Euler Integration**:

```python
# Update velocity
ax, ay, az = Fx/p.mass, Fy/p.mass, Fz/p.mass
p.vx += ax * dt
p.vy += ay * dt
p.vz += az * dt

# Update position
p.x += p.vx * dt
p.y += p.vy * dt
p.z += p.vz * dt
```

A small `epsilon` is added to prevent singularities when planets get too close.

---

## 🧩 Code Structure

```
📁 3D-Gravitational-Simulation
│
├── main.py           # Main simulation and visualization script
├── README.md         # Documentation (this file)
└── requirements.txt  # Python dependencies (optional)
```

---

## 🧱 Planet Class

```python
class Planet:
    def __init__(self, x, y, z, radius, color, mass, vx=0, vy=0, vz=0):
        self.x, self.y, self.z = x, y, z
        self.vx, self.vy, self.vz = vx, vy, vz
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = [(x, y, z)]
```

Each `Planet` instance stores position, velocity, mass, and orbit history.

---

## ⚡ Simulation Logic

### 1️⃣ Compute gravitational force between all pairs
```python
def gravitational_force(p1, p2, G=0.1, epsilon=0.01):
    dx, dy, dz = p2.x-p1.x, p2.y-p1.y, p2.z-p1.z
    dist_sq = dx*dx + dy*dy + dz*dz + epsilon*epsilon
    dist = math.sqrt(dist_sq)
    F = G * p1.mass * p2.mass / dist_sq
    return (F*dx/dist, F*dy/dist, F*dz/dist)
```

### 2️⃣ Update velocities and positions
```python
def simulate(planets, dt, G=0.1, max_trail=300):
    for p in planets:
        fx = fy = fz = 0.0
        for q in planets:
            if p is not q:
                dfx, dfy, dfz = gravitational_force(p, q, G)
                fx += dfx; fy += dfy; fz += dfz
        update_velocity(p, (fx, fy, fz), dt)
    
    for p in planets:
        update_position(p, dt)
        p.orbit.append((p.x, p.y, p.z))
        if len(p.orbit) > max_trail:
            p.orbit.pop(0)
```

---

## 🎨 Visualization

- Uses `matplotlib`’s 3D plotting (`Axes3D`) and `FuncAnimation`
- Each planet is drawn as a colored scatter point
- Trails represent recent orbital paths
- Velocity vectors are visualized using `ax.quiver`

```python
ax.scatter(p.x, p.y, p.z, color=p.color, s=80)
ax.plot(xs, ys, zs, color=p.color, alpha=0.6, linewidth=2)
ax.quiver(p.x, p.y, p.z, p.vx, p.vy, p.vz, length=2.0, normalize=True, color=p.color)
```

---

## 🧰 Requirements

Install Python dependencies:

```bash
pip install matplotlib
```

---

## ▶️ How to Run

```bash
git clone https://github.com/<your-username>/3D-Gravitational-Simulation.git
cd 3D-Gravitational-Simulation
python main.py
```

You should see a 3D space with three colored planets orbiting dynamically.  
Use keyboard controls to pause, step, or reset.

---

## 📸 Example Output

```
[ Red planet moving diagonally across the screen ]
[ Green and Blue planets orbiting and interacting gravitationally ]
```

*(Add screenshots or GIFs once you upload your animation)*

---

## 🧩 Customization

You can add or modify planets in the initialization block:

```python
orig = [
    Planet(0, 0, 0, 0.1, 'red', 40, 1.0, 0.5, 0.5),
    Planet(3, 0, 0, 0.1, 'green', 40, 0.0, -0.5, 0.3),
    Planet(0, 4, 2, 0.1, 'blue', 40, -1.0, -0.3, 0.0),
]
```

---

## 🧭 Future Enhancements

- Replace Euler integration with **Runge–Kutta 4 (RK4)** for higher accuracy  
- Add **collision detection** and planet merging  
- Implement **energy conservation visualization**  
- Add GUI controls for adjusting parameters like `G`, `dt`, and `planet count`  
- Option to export simulation data to CSV or JSON  




---

