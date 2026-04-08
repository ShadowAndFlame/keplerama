from turtle import title
import pyqtgraph as pg # ty: ignore
from PyQt6.QtWidgets import QGraphicsEllipseItem # ty: ignore

def complex_to_xy(z: list[complex]) -> tuple[list[float], list[float]]:
    x = [zz.real for zz in z]
    y = [zz.imag for zz in z]
    return x, y

def plot_complex(z: list[complex], d: float = 0):
    plot = pg.plot()
    plot.setAspectLocked(True)
    plot.showGrid(x=True, y=True)

    plot.plot(*complex_to_xy(z))

    planet = QGraphicsEllipseItem(-d/2, -d/2, d, d)  # x, y, width, height
    planet.setPen(pg.mkPen((0, 0, 0, 100)))
    planet.setBrush(pg.mkBrush((0, 0, 255)))
    plot.addItem(planet)
