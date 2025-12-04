# Q6a: LDE Solution
n = np.arange(0, 50)
theta = np.zeros(len(n))
theta[0] = 0.1  # w[0]
theta[1] = -2   # w[1]

for i in range(2, len(n)):
    theta[i] = 0.5*theta[i-1] + 0.3*theta[i-2]

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.stem(n, theta)
plt.title('Q6: LDE Step Response')
plt.xlabel('n')
plt.ylabel('θ[n]')
plt.grid(True)

# Q6c: Z-transform simulation
Hz_Q6 = cnt.TransferFunction([1], [1, -0.5, -0.3], dt=1.0)
t_z, y_z = cnt.step_response(Hz_Q6, n)

plt.subplot(1, 2, 2)
plt.stem(t_z, y_z[0])
plt.title('Q6: Z-transform Step Response')
plt.xlabel('n')
plt.ylabel('θ[n]')
plt.grid(True)

plt.tight_layout()
plt.show()

print("Q6 Discrete Transfer Function:")
print(Hz_Q6)