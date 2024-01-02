from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np


root = Tk()

fig = Figure(figsize=(10, 6), dpi=100)
t = np.arange(0, 3, 0.01)
fig.add_subplot(111).plot(t, 2*np.sin(2*np.pi*t))

canvas = FigureCanvasTkAgg(fig, master=root)  # a tk drawing area
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

mainloop()
