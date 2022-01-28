
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

#app = pg.mkQApp("Plotting Example")
# mw = QtGui.QMainWindow()
# mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(600,400)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))

if __name__ == '__main__':
    pg.exec()
