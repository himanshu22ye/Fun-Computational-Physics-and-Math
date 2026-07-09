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

g = 9.81

m1 = 1.0
m2 = 1.0

theta1 = np.radians(120)
theta2 = np.radians(-20)

omega1 = 0.0
omega2 = 0.0


L1 = 2
L2 = 2

# Time step
dt = 0.01


fig, ax = plt.subplots(figsize=(7, 7))


line1, = ax.plot([], [], lw=3, color="blue")
line2, = ax.plot([], [], lw=3, color="green")
trail, = ax.plot(
    [],
    [],
    color="purple",
    linewidth=1.5,
    alpha=0.7
)


ax.scatter(0, 0, s=120, color="black")


bob1 = ax.scatter([], [], s=180, color="red")
bob2 = ax.scatter([], [], s=180, color="orange")
trail_x = []
trail_y = []

# Graph settings
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 1)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Double Pendulum (Animation)")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")



# Animation Function
def update(frame):

    global theta1,theta2
    global omega1,omega2
    global trail_x,trail_y

    # Change the angles every frame
    num1 = -g * (2 * m1 + m2) * np.sin(theta1)

    num2 = -m2 * g * np.sin(theta1 - 2 * theta2)

    num3 = -2 * np.sin(theta1 - theta2) * m2

    num4 = (
       omega2**2 * L2
       + omega1**2 * L1 * np.cos(theta1 - theta2)
    )

    numerator = num1 + num2 + num3 * num4

    denominator = L1 * (
        2 * m1
        + m2
        - m2 * np.cos(2 * theta1 - 2 * theta2)
    )

    alpha1 = numerator / denominator

    #alpha 2
    num1 = 2 * np.sin(theta1 - theta2)

    num2 = (
        omega1**2 * L1 * (m1 + m2)
        + g * (m1 + m2) * np.cos(theta1)
        + omega2**2 * L2 * m2 * np.cos(theta1 - theta2)
    )

    denominator = L2 * (
        2 * m1
        + m2
        - m2 * np.cos(2 * theta1 - 2 * theta2)
    )

    alpha2 = (num1 * num2) / denominator

# Update angular velocity
    omega1 += alpha1 * dt
# Update angle
    theta1 += omega1 * dt

    omega2 += alpha2 * dt
    theta2 += omega2 * dt

    # Bob 1 position
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    # Bob 2 position
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    trail_x.append(x2)
    trail_y.append(y2)

    if len(trail_x) > 500:
        trail_x.pop(0)
        trail_y.pop(0)

    # Update rods
    line1.set_data([0, x1], [0, y1])
    line2.set_data([x1, x2], [y1, y2])

    trail.set_data(trail_x, trail_y)

    # Update Bob 1
    bob1.set_offsets([x1, y1])

    # Update Bob 2
    bob2.set_offsets([x2, y2])

    return (
        line1,
        line2,
        trail,
        bob1,
        bob2
    )   


# Create Animation
ani = FuncAnimation(
    fig,
    update,
    frames=1000,
    interval=20,
    blit=True,
    repeat=True
)

plt.show()