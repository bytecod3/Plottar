import matplotlib.pyplot as plt
import numpy as np

# creating an ndarray
# x = np.array([1,2,3])
# y = np.array([4, 5, 6])

# multidimensional array
# m= np.array([ [1, 2, 3], [4, 5, 6] ])
# print(m[1,2])

# print(x+y)
x = np.arange(0.0, 6.0, 0.01)
plt.plot(x, [xi**2 for xi in x], label="test1")
plt.plot(x+2, '-.')

# enable legend visibility
plt.legend(loc='upper left')

# show grid
plt.grid(True)

# handle axis
# show current axis limits
plt.axis(xmin=-1, xmax=8, ymin=-2, ymax=40)

# set axes labels
plt.xlabel('No. of samples')
plt.ylabel('value')

# set plot title
plt.title("Test data")

# save a plot to file
# plt.savefig('plt1.png')

plt.show()