import copy
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ----- Planet Class -----
class Planet:
    def __init__(self, x, y, z, radius, color, mass, vx=0, vy=0, vz=0):
        self.x, self.y, self.z = x, y, z
        self.radius = radius
        self.color = color
        self.mass = mass
        self.vx, self.vy, self.vz = vx, vy, vz
        self.orbit = [(x, y, z)]
    def state(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz, list(self.orbit))
    def load_state(self, st):
        self.x, self.y, self.z, self.vx, self.vy, self.vz, self.orbit = st

# ----- Physics Functions -----
def update_position(p, dt):
    p.x += p.vx * dt
    p.y += p.vy * dt
    p.z += p.vz * dt

def update_velocity(p, force, dt):
    ax, ay, az = force[0]/p.mass, force[1]/p.mass, force[2]/p.mass
    p.vx += ax * dt
    p.vy += ay * dt
    p.vz += az * dt

def gravitational_force(p1, p2, G=0.1, epsilon=0.01):
    dx, dy, dz = p2.x-p1.x, p2.y-p1.y, p2.z-p1.z
    dist_sq = dx*dx + dy*dy + dz*dz + epsilon*epsilon
    dist = math.sqrt(dist_sq)
    F = G * p1.mass * p2.mass / dist_sq
    return (F*dx/dist, F*dy/dist, F*dz/dist)

def simulate(planets, dt, G=0.1, max_trail=300):
    # update velocities
    for p in planets:
        fx = fy = fz = 0.0
        for q in planets:
            if p is not q:
                dfx, dfy, dfz = gravitational_force(p, q, G)
                fx += dfx; fy += dfy; fz += dfz
        update_velocity(p, (fx, fy, fz), dt)
    # update positions & orbits
    for p in planets:
        update_position(p, dt)
        p.orbit.append((p.x, p.y, p.z))
        if len(p.orbit) > max_trail:
            p.orbit.pop(0)

# ----- Initialization -----
dt = 0.1
MAX_TRAIL = 300

orig = [
    Planet( 0,0,0, 0.1,'red',   40,  1.0,  0.5,  0.5),
    Planet( 3,0,0, 0.1,'green', 40,  0.0, -0.5,  0.3),
    Planet( 0,4,2, 0.1,'blue',  40, -1.0, -0.3,  0.0),
]
planets = copy.deepcopy(orig)
initial_states = [p.state() for p in planets]

# ----- Plot Setup -----
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

running = True
step_once = False

# Keyboard controls
def on_key(event):
    global running, step_once
    if event.key == ' ':
        running = not running
    elif event.key == 'right' and not running:
        step_once = True
    elif event.key == 'r':
        for p, st in zip(planets, initial_states):
            p.load_state(st)
        ax.clear()

fig.canvas.mpl_connect('key_press_event', on_key)

# ----- Animation -----
def animate(frame):
    global step_once
    if running or step_once:
        simulate(planets, dt, G=0.1, max_trail=MAX_TRAIL)
        step_once = False

    ax.clear()
    ax.set_xlim(-10,10); ax.set_ylim(-10,10); ax.set_zlim(-10,10)
    ax.set_title("Space=Pause ▶ Right=Step ▶ R=Reset", color='white')
    ax.set_xlabel("X", color='white'); ax.set_ylabel("Y", color='white'); ax.set_zlabel("Z", color='white')
    ax.tick_params(colors='white')

    for p in planets:
        # Draw orbit trail
        xs, ys, zs = zip(*p.orbit)
        ax.plot(xs, ys, zs, color=p.color, alpha=0.6, linewidth=2)
        # Draw planet
        ax.scatter(p.x, p.y, p.z, color=p.color, s=80)
        # Draw velocity vector (longer for visibility)
        ax.quiver(p.x, p.y, p.z,
                  p.vx, p.vy, p.vz,
                  length=2.0, normalize=True, color=p.color, alpha=0.9)
        # Label at planet
        ax.text(p.x, p.y, p.z, f"{p.color}", color='white', fontsize=8)

ani = FuncAnimation(fig, animate, interval=50)
plt.show()
