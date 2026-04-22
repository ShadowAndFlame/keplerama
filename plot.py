from newton import magnitude, direction, Body
from typing import Generator
import pyqtgraph as pg # ty: ignore
from PyQt6.QtWidgets import QGraphicsEllipseItem # ty: ignore
from PyQt6.QtCore import QTimer # ty: ignore
from numpy import append # ty: ignore

def complex_to_xy(z: list[complex]) -> tuple[list[float], list[float]]:
    x = [zz.real for zz in z]
    y = [zz.imag for zz in z]
    return x, y

def plot_complex(z: list[complex], d: float = 0):
    plot = pg.plot()
    plot.setAspectLocked(True)
    plot.showGrid(x=True, y=True)

    planet = QGraphicsEllipseItem(-d/2, -d/2, d, d)  # x, y, width, height
    planet.setPen(pg.mkPen((0, 0, 0, 100)))
    planet.setBrush(pg.mkBrush((0, 0, 255)))
    plot.addItem(planet)

    plot.plot(*complex_to_xy(z))

def plot_complex_live(gen: Generator[complex, None, None], bodies: list[Body]) -> QTimer:
    plot = pg.plot()
    plot.setAspectLocked(True)
    plot.showGrid(x=True, y=True)

    planets = []
    for body in bodies:
        planet = QGraphicsEllipseItem(-d/2, -d/2, d, d)  # x, y, width, height
        planet.setPen(pg.mkPen((0, 0, 0, 100)))
        planet.setBrush(pg.mkBrush((0, 0, 255)))
        plot.addItem(planet)
        planets.append(planet)

    z0 = next(gen)
    x0 = z0.real
    y0 = z0.imag
    line = plot.plot([x0], [y0])

    timer = QTimer()

    def next_point():
        z = next(gen)
        if magnitude(z) <= d/2:
            crash_z = d/2*direction(z)
            plot.plot([crash_z.real], [crash_z.imag], line=None, symbol='x', symbolPen=pg.mkPen((255, 0, 0, 100)), symbolBrush=pg.mkBrush((255, 0, 0)))
            timer.stop()
            return
        x = append(line.xData, z.real)
        y = append(line.yData, z.imag)
        line.setData(x, y)
    
    timer.timeout.connect(next_point)
    return timer
