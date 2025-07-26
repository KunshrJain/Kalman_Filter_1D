import numpy as np
import matplotlib.pyplot as plt

# Time step (seconds)
dt = 0.1

# Define system model
A = np.array([[1, dt],
              [0, 1]])      # State transition matrix
B = np.array([[0.5 * dt**2],
              [dt]])        # Control input matrix (for acceleration)
H = np.array([[1, 0]])      # Measurement matrix (barometer only sees altitude)

# Covariances
Q = np.array([[1e-3, 0],
              [0, 1.51e-3]])   # Process noise (trust in model)
R = np.array([[3]])         # Measurement noise (barometer noise ~3m)

# Initial state
x = np.array([[0],          # altitude (m)
              [0]])         # velocity (m/s)
P = np.eye(2)               # Initial estimate uncertainty

# Simulated true values and measurements
true_alt = 0
true_vel = 0
acc_input = 1.5             # m/s² constant acceleration (e.g., during motor burn)

# Data storage for plotting
estimates = []
measurements = []
truths = []

# Simulation loop
for t in range(100):
    # Simulate true motion
    true_alt += true_vel * dt + 0.5 * acc_input * dt**2
    true_vel += acc_input * dt

    # Simulate noisy sensor readings
    z = true_alt + np.random.normal(0, 50)    # barometer
    acc_measured = acc_input + np.random.normal(0, 0.2)  # IMU noise

    # === Kalman Prediction ===
    u = np.array([[acc_measured]])            # control input
    x = A @ x + B @ u                         # predicted state
    P = A @ P @ A.T + Q                       # predicted covariance

    # === Kalman Update ===
    y = z - (H @ x)                           # innovation
    S = H @ P @ H.T + R                       # innovation covariance
    K = P @ H.T @ np.linalg.inv(S)            # Kalman Gain
    x = x + K @ y                             # update estimate
    P = (np.eye(2) - K @ H) @ P               # update covariance

    # Store for plotting
    estimates.append(x[0, 0])
    measurements.append(z)
    truths.append(true_alt)

# === Plot results ===
plt.figure(figsize=(10, 5))
plt.plot(truths, label='True Altitude')
plt.plot(measurements, label='Barometer (Noisy)', linestyle='dotted')
plt.plot(estimates, label='Kalman Filter Estimate')
plt.xlabel('Time step')
plt.ylabel('Altitude (m)')
plt.title('Kalman Filter for Rocket Altitude Estimation')
plt.legend()
plt.grid()
plt.show()
