import serial
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep

# === Kalman Filter Initialization ===
dt = 0.1
A = np.array([[1, dt], [0, 1]])
B = np.array([[0.5 * dt ** 2], [dt]])
H = np.array([[1, 0]])
Q = np.array([[0.01, 0], [0, 0.1]])
R = np.array([[9]])
x = np.array([[0], [0]])  # [altitude, velocity]
P = np.eye(2)

# === Serial Port Setup (change COM port as needed) ===
ser = serial.Serial('COM3', 115200, timeout=1)

# === Data Lists for Plotting ===
t_vals, alt_true, alt_kf = [], [], []
start_time = time()

try:
    i=0
    while True:
        line = []
        i+=1
        if line.startswith("ALT:"):
            try:
                
                # Parse values
                parts = line.replace("ALT:", "").replace("ACC:", "").split()
                alt = float(parts[0])
                acc = float(parts[1])  # should already have gravity removed on ESP32

                # Kalman Prediction
                u = np.array([[acc]])
                x = A @ x + B @ u
                P = A @ P @ A.T + Q

                # Kalman Update
                y = np.array([[alt]]) - H @ x
                S = H @ P @ H.T + R
                K = P @ H.T @ np.linalg.inv(S)
                x = x + K @ y
                P = (np.eye(2) - K @ H) @ P

                # Store data
                t_vals.append(time() - start_time)
                alt_true.append(alt)
                alt_kf.append(x[0, 0])

                # Print estimate
                print(f"KF Altitude: {x[0,0]:.2f} m | Velocity: {x[1,0]:.2f} m/s")

                sleep(dt)

            except Exception as e:
                print("Parse error:", e)

except KeyboardInterrupt:
    ser.close()
    print("Serial closed.")

    # Plot after exit
    plt.figure(figsize=(10, 5))
    plt.plot(t_vals, alt_true, label="Barometer Altitude (Noisy)", linestyle="dotted")
    plt.plot(t_vals, alt_kf, label="Kalman Filter Altitude", linewidth=2)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Real-Time Kalman Filter from ESP32")
    plt.legend()
    plt.grid()
    plt.show()
