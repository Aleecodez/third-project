import numpy as np
import control as cnt
from matplotlib import pyplot as plt

# Set up the system
s = cnt.tf('s')

# Part c: Arbitrary parameter values
R1, R2, C1, C2, L1 = 10, 20, 30, 40, 50
Hs = R1/(s+R2) + (0.1*C1)/(C2*s**2 + 0.1+L1)

print("Transfer Function Hs:")
print(Hs)

# Part d: Convert to Z-transform
Ts = 0.1
Hz = cnt.sample_system(Hs, Ts, method='zoh')
print("\nDiscrete Transfer Function Hz:")
print(Hz)

# Part e & f: Impulse and Step responses
plt.figure(figsize=(15, 5))

# Impulse response
plt.subplot(1, 3, 1)
t_impulse, y_impulse = cnt.impulse_response(Hs)
plt.plot(t_impulse, y_impulse)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Step response
plt.subplot(1, 3, 2)
t_step, y_step = cnt.step_response(Hs)
plt.plot(t_step, y_step)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Part g: Modified parameters for less oscillations
R1_mod, R2_mod, C1_mod, C2_mod, L1_mod = 2, 25, 10, 60, 80
Hs_mod = R1_mod/(s+R2_mod) + (0.1*C1_mod)/(C2_mod*s**2 + 0.1+L1_mod)

plt.subplot(1, 3, 3)
t1, y1 = cnt.step_response(Hs)
t2, y2 = cnt.step_response(Hs_mod)
plt.plot(t1, y1, 'b-', label='Original')
plt.plot(t2, y2, 'r-', label='Modified')
plt.title('Step Response Comparison')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# System analysis
print("\nSystem Analysis:")
print(f"Original system damping ratio: {cnt.damping(Hs)[0]}")
print(f"Modified system damping ratio: {cnt.damping(Hs_mod)[0]}")