# 🔥 1D Heat Stimulation in Steel — IIT Bombay Project

This project simulates **1D heat conduction** in a steel billet using the **Finite Difference Method (FDM)** and the **Tridiagonal Matrix Algorithm (TDMA)**. It is developed as part of an academic project inspired by IIT Bombay.

---

## 📌 Features

- 1D transient heat conduction simulation
- TDMA (Thomas Algorithm) for solving matrix equations
- Temperature variation with respect to time and position
- Modular and reusable Python code
- Outputs results in CSV format at regular time intervals

---

## 📁 Project Structure

1_D_Heat_Stimulations/
├── Billet.py # Main driver script to run the simulation
├── HeatEquations1d.py # Logic for heat equation and time stepping
├── InitialConditions.py # Defines geometry, time step, initial temperature
├── SteelProperties.py # Provides material properties (ρ, Cp, k, etc.)
├── TridagSolver.py # Implements TDMA (Thomas Algorithm)
├── Writes.py # Writes output CSVs
├── Path.py # Defines input/output folder structure
├── input/
│ └── input.csv # Optional input CSV for simulation parameters
├── output/
│ ├── results1.csv
│ ├── results2.csv
│ └── ... # Outputs for each time step (every nwrite)
├── pycache/ # Auto-generated cache by Python
└── README.md # Project documentation (this file)


## ⚙️ Simulation Parameters

- **Material**: Steel
- **Length of billet**: 1000 mm
- **Initial Temperature**: 20°C
- **Heat Transfer Coefficients**: hl = hr = 1000 W/m²°C
- **Air Temperature (both sides)**: 20°C
- **Density (ρ)**: 7800 kg/m³
- **Thermal Conductivity (k)**: Based on % Carbon
- **Specific Heat (Cp)**: Based on % Carbon
- **Number of Nodes**: 100
- **Time Step (Δt)**: 1 second
- **Total Simulation Time**: 1000 seconds
- **Output Interval (`nwrite`)**: User-defined (e.g., every 100 steps)

---

## 🚀 How to Run the Simulation

### 1. Clone the Repository

```bash
git clone https://github.com/santosh-patil-hub/1D_Heat_Stimulations.git
cd 1D_Heat_Stimulations
2. Run the Simulation
# output file 
[results7.csv](https://github.com/user-attachments/files/20905141/results7.csv)

python Billet.py
