# Kalman Filter Demo – Native C Backend + Python GUI

This project demonstrates a simple but powerful **Kalman Filter** implementation written in **native C**, and wrapped using **Python ctypes** to interface with a **PyQt5 GUI**. The goal is to show how high-performance C logic can be combined with a modern, flexible frontend in Python.

> 🚀 Ideal for real-time sensor fusion, noise filtering, or predictive applications in embedded systems, robotics, and more.

---

## 🧠 Project Overview

- **Kalman Filter**: Implements a basic 1D filter in C (custom struct + init/update methods).
- **Python GUI**: PyQt5 interface to enter values and visualize results.
- **ctypes Bridge**: Python loads the compiled C `.dll`/`.so` directly for max performance.
- **Cross-Platform**: Works on Windows/Linux with minor tweaks.
- **Highly Modular**: C logic and Python UI are fully decoupled.

---

## 🔧 Folder Structure

kalman-project:

├── kalman.c # Native C Kalman logic

├── kalman.h # Header file

├── build.bat / Makefile # Compile C into DLL/SO

├── main.c # Calling for test

├── main.exe #Execution file for post prototyping

├── README.md 

├── License


---
---

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

| Tool        | Purpose                          |
|-------------|----------------------------------|
| **G++**| To run GUI and ctypes wrapper    |
| **gcc/clang** | To compile the C code into DLL/SO |
| **Python**   | testing                    |

2. Install VSC:
   ```bash
   https://code.visualstudio.com/
   ```
3. Install Gcc/G++:
   ```bash
   https://code.visualstudio.com/docs/cpp/config-mingw
   ```

---

### License:
This project is licensed under the MIT License - see the LICENSE.md file for details.

---
### Contributors:
| Name                                       | GitHub Profile            |
| ------------------------------------------ | ------------------------- |
| [Kunsh Jain](https://github.com/kunshrjain) | Contributor and Developer |
| [Pranjal Giri](https://github.com/oslowtech) | Contributor and Developer and gay |



