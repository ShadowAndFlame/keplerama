from turtle import title
import pyqtgraph as pg
from PyQt6.QtWidgets import QGraphicsEllipseItem

def plot_complex(z: list[complex], d: float = 0):
    plot = pg.plot()
    plot.setAspectLocked(True)
    plot.showGrid(x=True, y=True)

    reals = [zz.real for zz in z]
    imags = [zz.imag for zz in z]
    plot.plot(reals, imags)

    planet = QGraphicsEllipseItem(-d/2, -d/2, d, d)  # x, y, width, height
    planet.setPen(pg.mkPen((0, 0, 0, 100)))
    planet.setBrush(pg.mkBrush((0, 0, 255)))
    plot.addItem(planet)
