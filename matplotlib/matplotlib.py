# Initialize
import numpy as np
import matplotlib.pyplot as pl
# Prepare
x = np.linspace(0, 4*np.pi, 1000)
y = np.sin(x)
# Render
fig, ax = plt.subplot()
ax.plot(x,y)
fig.show()

