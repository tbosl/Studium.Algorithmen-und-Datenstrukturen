import matplotlib.pyplot as plt
import numpy as np

n_values = np.arange(1, 20)

f_8n = 8 * n_values
f_4nlogn = 4 * n_values * np.log2(n_values)
f_2n2 = 2 * n_values ** 2
f_n3 = n_values ** 3
f_2n = 2 ** n_values

log_f_8n = np.log2(f_8n)
log_f_4nlogn = np.where(f_4nlogn > 0, np.log2(f_4nlogn), 0)
log_f_2n2 = np.log2(f_2n2)
log_f_n3 = np.log2(f_n3)
log_f_2n = n_values

# Plot the points
plt.figure(figsize=(10, 6))
plt.plot(np.log2(n_values), log_f_8n, label='8n')
plt.plot(np.log2(n_values), log_f_4nlogn, label='4nlogn')
plt.plot(np.log2(n_values), log_f_2n2, label='2n^2')
plt.plot(np.log2(n_values), log_f_n3, label='n^3')
plt.plot(np.log2(n_values), log_f_2n, label='2^n')

# Add labels and title
plt.xlabel('log(n)')
plt.ylabel('log(f(n))')
plt.title('Functions on Logarithmic Scale')
plt.legend()

# Show plot
plt.grid(True)
plt.show()