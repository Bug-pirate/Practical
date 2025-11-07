# -------------------------------------------------------------
# Experiment 6: Fuzzy Inference System for Fan Speed Control
# Corrected version (works across skfuzzy versions)
# -------------------------------------------------------------

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Step 1: Define input and output variables
# -------------------------------------------------------------
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')  # 0°C to 50°C
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')     # 0% to 100%

# -------------------------------------------------------------
# Step 2: Define membership functions
# -------------------------------------------------------------
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot']  = fuzz.trimf(temperature.universe, [30, 50, 50])

fan_speed['low']    = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high']   = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# -------------------------------------------------------------
# Step 3: Define fuzzy rules
# -------------------------------------------------------------
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'],  fan_speed['high'])

# -------------------------------------------------------------
# Step 4: Create control system
# -------------------------------------------------------------
fan_ctrl_system = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl_system)

# -------------------------------------------------------------
# Step 5: Provide input and compute output
# -------------------------------------------------------------
# Set the input value in a variable so we can print it reliably later
temperature_value = 30  # Example input (change as needed)

# Assign and compute
fan_sim.input['temperature'] = temperature_value
fan_sim.compute()

# -------------------------------------------------------------
# Step 6: Display result (version-independent)
# -------------------------------------------------------------
print("-------------------------------------------------------------")
print("Fuzzy Inference System: Fan Speed Control")
print("-------------------------------------------------------------")
print(f"Input Temperature: {temperature_value} °C")
# fan_sim.output is a dict-like mapping of consequent name -> crisp value
print(f"Defuzzified Fan Speed: {fan_sim.output['fan_speed']:.2f} %")
print("-------------------------------------------------------------")

# -------------------------------------------------------------
# Optional: Evaluate multiple sample inputs and print table
# -------------------------------------------------------------
# Uncomment the block below to test multiple temperature values automatically.
# (This will recompute the simulation for each value.)

# print("\nSample evaluations:")
# print("Temperature (°C) -> Fan Speed (%)")
# for t in [0, 10, 20, 25, 30, 35, 40, 50]:
#     fan_sim.input['temperature'] = t
#     fan_sim.compute()
#     print(f"{t:>3} -> {fan_sim.output['fan_speed']:.2f}")

# -------------------------------------------------------------
# Step 7: Visualize results
# -------------------------------------------------------------
# Membership functions
temperature.view()
fan_speed.view()

# Show result on the output membership plot
# (this highlights the defuzzified value)
try:
    fan_speed.view(sim=fan_sim)
except Exception:
    # In some environments view(sim=...) may raise; ignore if plotting fails
    pass

plt.show()