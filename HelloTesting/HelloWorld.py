import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 1, 50)
y = 2*x + 1
plt.figure()
plt.plot(y,labels='predictions')
plt.show()