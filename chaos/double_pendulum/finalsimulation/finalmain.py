import matplotlib
matplotlib.use("QtAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class DoublePendulum:
    """
    Double Pendulum Simulator
    -------------------------
    This class stores all the physical parameters of
    the pendulum in one place.
    """

    def __init__(self):


        self.g = 9.81


        self.m1 = 1.0
        self.m2 = 1.0

        self.L1 = 2.0
        self.L2 = 2.0

        self.theta1 = np.radians(120)
        self.theta2 = np.radians(-20)


        self.omega1 = 0.0
        self.omega2 = 0.0


        self.dt = 0.01

    def derivatives(self,state):


        """
        Returns the derivatives of the current state.
        """
        theta1, theta2, omega1, omega2 = state
        dtheta1 = omega1
        dtheta2 = omega2

        # Alpha 1

        numerator1 = (
            -self.g * (2 * self.m1 + self.m2)
            * np.sin(theta1)
        )

        numerator2 = (
            -self.m2 * self.g
            * np.sin(theta1 - 2 * theta2)
        )

        numerator3 = (
            -2
            * np.sin(theta1 - theta2)
            * self.m2
        )

        numerator4 = (
            omega2**2
            * self.L2
            +
            omega1**2
            * self.L1
            * np.cos(theta1 - theta2)
        )

        denominator1 = (
            self.L1
            *
            (
                2 * self.m1
                + self.m2
                - self.m2
                * np.cos(
                    2 * theta1
                    - 2 * theta2
                )
            )
        )

        domega1 = (
            numerator1
            + numerator2
            + numerator3 * numerator4
        ) / denominator1

        # Alpha 2

        numerator5 = (
            2
            * np.sin(theta1 - theta2)
        )

        numerator6 = (
            omega1**2
            * self.L1
            * (self.m1 + self.m2)

            +

            self.g
            * (self.m1 + self.m2)
            * np.cos(theta1)

            +

            self.omega2**2
            * self.L2
            * self.m2
            * np.cos(theta1 - theta2)
        )

        denominator2 = (
            self.L2
            *
            (
                2 * self.m1
                + self.m2
                - self.m2
                * np.cos(
                    2 * theta1
                    - 2 * theta2
                )
            )
        )

        domega2 = (
            numerator5 * numerator6
        ) / denominator2

        return (
            dtheta1,
            dtheta2,
            domega1,
            domega2
        )



    def rk4_step(self):

        print("\n========== RK4 Step ==========")
        theta1 = self.theta1
        theta2 = self.theta2
        omega1 = self.omega1
        omega2 = self.omega2

        # Save current state
        state = (
            theta1,
            theta2,
            omega1,
            omega2
        )

        print("\nCurrent State")
        print("----------------")
        print(f"Theta1 : {np.degrees(theta1):.2f}°")
        print(f"Theta2 : {np.degrees(theta2):.2f}°")
        print(f"Omega1 : {omega1:.4f}")
        print(f"Omega2 : {omega2:.4f}")

        k1 = self.derivatives(state)
        temp_state = (
        state[0] + k1[0] * self.dt / 2,
        state[1] + k1[1] * self.dt / 2,
        state[2] + k1[2] * self.dt / 2,
        state[3] + k1[3] * self.dt / 2
        )

        print("\nFirst RK4 Slope (k1)")
        print("--------------------")
        print(f"dTheta1 : {k1[0]:.6f}")
        print(f"dTheta2 : {k1[1]:.6f}")
        print(f"dOmega1 : {k1[2]:.6f}")
        print(f"dOmega2 : {k1[3]:.6f}")


        temp_state = (
        state[0] + k1[0] * self.dt / 2,
        state[1] + k1[1] * self.dt / 2,
        state[2] + k1[2] * self.dt / 2,
        state[3] + k1[3] * self.dt / 2
        )

        print("\nTemporary State (for k2)")
        print("-------------------------")
        print(f"Theta1 : {np.degrees(temp_state[0]):.4f}°")
        print(f"Theta2 : {np.degrees(temp_state[1]):.4f}°")
        print(f"Omega1 : {temp_state[2]:.6f}")
        print(f"Omega2 : {temp_state[3]:.6f}")

        k2 = self.derivatives(temp_state)
        temp_state = (
        state[0] + k2[0] * self.dt / 2,
        state[1] + k2[1] * self.dt / 2,
        state[2] + k2[2] * self.dt / 2,
        state[3] + k2[3] * self.dt / 2
         )

        print("\nSecond RK4 Slope (k2)")
        print("----------------------")
        print(f"dTheta1 : {k2[0]:.6f}")
        print(f"dTheta2 : {k2[1]:.6f}")
        print(f"dOmega1 : {k2[2]:.6f}")
        print(f"dOmega2 : {k2[3]:.6f}")


        k3 = self.derivatives(temp_state)

        print("\nThird RK4 Slope (k3)")
        print("--------------------")
        print(f"dTheta1 : {k3[0]:.6f}")
        print(f"dTheta2 : {k3[1]:.6f}")
        print(f"dOmega1 : {k3[2]:.6f}")
        print(f"dOmega2 : {k3[3]:.6f}")



        temp_state = (
            state[0] + k3[0] * self.dt,
            state[1] + k3[1] * self.dt,
            state[2] + k3[2] * self.dt,
            state[3] + k3[3] * self.dt
        )

        print("\nTemporary State (for k4)")
        print("-------------------------")
        print(f"Theta1 : {np.degrees(temp_state[0]):.4f}°")
        print(f"Theta2 : {np.degrees(temp_state[1]):.4f}°")
        print(f"Omega1 : {temp_state[2]:.6f}")
        print(f"Omega2 : {temp_state[3]:.6f}")

        k4 = self.derivatives(temp_state)

        print("\nFourth RK4 Slope (k4)")
        print("---------------------")
        print(f"dTheta1 : {k4[0]:.6f}")
        print(f"dTheta2 : {k4[1]:.6f}")
        print(f"dOmega1 : {k4[2]:.6f}")
        print(f"dOmega2 : {k4[3]:.6f}")

        # =====================================================
        # RK4 Weighted Average
        # =====================================================

        new_theta1 = state[0] + (
            self.dt / 6
        ) * (
            k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]
        )

        new_theta2 = state[1] + (
            self.dt / 6
        ) * (
            k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]
        )

        new_omega1 = state[2] + (
            self.dt / 6
        ) * (
            k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2]
        )

        new_omega2 = state[3] + (
            self.dt / 6
        ) * (
            k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3]
        )

        print("\nNew State (After One RK4 Step)")
        print("------------------------------")
        print(f"Theta1 : {np.degrees(new_theta1):.4f}°")
        print(f"Theta2 : {np.degrees(new_theta2):.4f}°")
        print(f"Omega1 : {new_omega1:.6f}")
        print(f"Omega2 : {new_omega2:.6f}")

        self.theta1 = new_theta1
        self.theta2 = new_theta2

        self.omega1 = new_omega1
        self.omega2 = new_omega2
        
    # Calculate Bob Positions
    def get_positions(self):

        # Bob 1
        x1 = self.L1 * np.sin(self.theta1)
        y1 = -self.L1 * np.cos(self.theta1)

        # Bob 2
        x2 = x1 + self.L2 * np.sin(self.theta2)
        y2 = y1 - self.L2 * np.cos(self.theta2)

        return (
            x1,
            y1,
            x2,
            y2
        )



pendulum = DoublePendulum()

x1, y1, x2, y2 = pendulum.get_positions()

print(f"Bob 1 : ({x1:.2f}, {y1:.2f})")
print(f"Bob 2 : ({x2:.2f}, {y2:.2f})")


