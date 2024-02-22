import numpy as np
import matplotlib.pyplot as plt
t_values = np.linspace(0,10, 1000)
func = np.exp(-0.01 * t_values)
plt.plot(t_values, func)
plt.show()
