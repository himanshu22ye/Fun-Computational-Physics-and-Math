"""import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation

matplotlib.use("QtAgg")

L1=2
L2=2
theta_deg1 = 45
theta_deg2 = 30
theta1=np.radians(theta_deg1)
theta2=np.radians(theta_deg2)
x1=L1*np.sin(theta1)
y1=-L1*np.cos(theta1)
x2=x1+L2*np.sin(theta2)
y2=y1-L2*np.cos(theta2)

print(f"Bob 1 : ({x1:.2f}, {y1:.2f})")
print(f"Bob 2 : ({x2:.2f}, {y2:.2f})")


plt.figure(figsize=(9,9))
plt.plot(
    [0, x1],
    [0, y1],
    linewidth=3,
    color="blue"
)

plt.plot(
    [x1, x2],
    [y1, y2],
    linewidth=3,
    color="green"
)

plt.scatter(
    0,
    0,
    s=120,
    color="black",
    label="Pivot"
)

plt.scatter(
    x1,
    y1,
    s=180,
    color="red",
    label="Bob 1"
)


plt.scatter(
    x2,
    y2,
    s=180,
    color="orange",
    label="Bob 2"
)

plt.title("Static Double Pendulum")

plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.grid(True)

plt.axis("equal")

plt.xlim(-5, 5)
plt.ylim(-5, 1)

plt.legend()

plt.show()




# Pivot coordinates
pivot_x = 0
pivot_y = 0

# Draw rod
plt.plot(
    [0, x1],
    [0, y1],
    linewidth=2
)



plt.scatter(pivot_x, pivot_y, s=80)


plt.scatter(x, y, s=150)


plt.axis("equal")


plt.xlim(-3, 3)
plt.ylim(-5, 1)

plt.grid(True)

plt.title("Single Pendulum")

plt.show()"""

#Artifical motion
import matplotlib
matplotlib.use("QtAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


L1 = 2
L2 = 2


fig, ax = plt.subplots(figsize=(7, 7))


line1, = ax.plot([], [], lw=3, color="blue")
line2, = ax.plot([], [], lw=3, color="green")


ax.scatter(0, 0, s=120, color="black")


bob1 = ax.scatter([], [], s=180, color="red")
bob2 = ax.scatter([], [], s=180, color="orange")

# Graph settings
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 1)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Double Pendulum (Fake Animation)")

# Animation Function
def update(frame):

    # Change the angles every frame
    theta1 = np.radians(frame)
    theta2 = np.radians(frame * 2)

    # Bob 1 position
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    # Bob 2 position
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    # Update rods
    line1.set_data([0, x1], [0, y1])
    line2.set_data([x1, x2], [y1, y2])

    # Update Bob 1
    bob1.set_offsets([x1, y1])

    # Update Bob 2
    bob2.set_offsets([x2, y2])

    return line1, line2, bob1, bob2


# Create Animation
ani = FuncAnimation(
    fig,
    update,
    frames=360,
    interval=30,
    blit=True
)

plt.show()