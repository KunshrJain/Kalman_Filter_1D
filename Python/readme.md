Built for testing and prototype building
## 🧠 Project Overview

- **Kalman Filter**: Implements a basic 1D filter in Python.
- **Dummy Data**: Test the Kalman filter using dummy data.




## 🔧 Folder Structure

kalman-project:

├── kalman.py # Python file Kalman logic

├── rocket_dummy_flight.csv # Header file

├── readme.md


## 🔧 Kalman Logic And theory
The Kalman Filter models the system as:
🔹 State Prediction
xₖ = Fₖ·xₖ₋₁ + Bₖ·uₖ + wₖ
Where:
- `xₖ` → State vector at time k (position, velocity, etc.)
- `Fₖ` → State transition matrix (how state evolves)
- `Bₖ` → Control input matrix (how input affects state)
- `uₖ` → Control vector (acceleration, input forces, etc.)
- `wₖ` → Process noise (assumed Gaussian with covariance `Q`)
- 
🔹 Measurement Update
zₖ = Hₖ·xₖ + vₖ

Where:
- `zₖ` → Measurement vector at time k (sensor data)
- `Hₖ` → Observation matrix (how states map to measurements)
- `vₖ` → Measurement noise (Gaussian with covariance `R`)

🔧 Update Equations

🔹Prediction Step
x̂ₖ⁻ = F·x̂ₖ₋₁ + B·u
Pₖ⁻ = F·Pₖ₋₁·Fᵀ + Q

🔹Update Step

Kₖ = Pₖ⁻·Hᵀ·(H·Pₖ⁻·Hᵀ + R)⁻¹

x̂ₖ = x̂ₖ⁻ + Kₖ·(zₖ - H·x̂ₖ⁻)

Pₖ = (I - Kₖ·H)·Pₖ⁻
---

## 🛠 Installation

### 1. Dependencies

| Tool               | Purpose                                         |
|--------------------|-------------------------------------------------|
| **MatPlot Library**| To plot the Graphs of filtered data             |
| **NumPy**          | To Perform the calculation of Matrices involved |

2. Install VSC:
   ```bash
   https://code.visualstudio.com/
   ```
3. Install Matplot Library:
   ```bash
   pip install matplotlib
   ```
3. Install NumPy Library:
   ```bash
   pip install numpy
   ```

---

### License:
This project is licensed under the MIT License - see the LICENSE.md file for details.

---
### Contributors:
| Name                                         | GitHub Profile            |
| ---------------------------------------------| ------------------------- |
| [Pranjal Giri](https://github.com/oslowtech) | Contributor and Developer |
| [Kunsh Jain](https://github.com/kunshrjain)  | Contributor and Developer |
