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

# def plot_complex(z: list[complex], d: float = 0):
#     plot = pg.plot()
#     plot.setAspectLocked(True)
#     plot.showGrid(x=True, y=True)

#     planet = QGraphicsEllipseItem(-d/2, -d/2, d, d)  # x, y, width, height
#     planet.setPen(pg.mkPen((0, 0, 0, 100)))
#     planet.setBrush(pg.mkBrush((0, 0, 255)))
#     plot.addItem(planet)

#     plot.plot(*complex_to_xy(z))

def plot_complex_live(gen: Generator[tuple[float, complex], None, None], bodies: list[Body]) -> QTimer:
    plot = pg.plot()
    plot.setAspectLocked(True)
    plot.showGrid(x=True, y=True)

    t0, z0 = next(gen)
    x0 = z0.real
    y0 = z0.imag
    line = plot.plot([x0], [y0])

    body_ellipses = []
    for body in bodies:
        d = body[1]
        p = body[2](t0)
        x = p.real - d/2
        y = p.imag - d/2
        body_ellipse = QGraphicsEllipseItem(x, y, d, d)  # x, y, width, height
        body_ellipse.setPen(pg.mkPen('black'))
        body_ellipse.setBrush(pg.mkBrush(body[3]))
        plot.addItem(body_ellipse)
        body_ellipses.append(body_ellipse)

    timer = QTimer()

    def crash(t, z):
        for body in bodies:
            d = body[1]
            p = body[2](t)
            if magnitude(p - z) > d/2:
                continue
            plot.plot([z.real], [z.imag], line=None, symbol='x', symbolPen=pg.mkPen((255, 0, 0, 100)), symbolBrush=pg.mkBrush((255, 0, 0)))
            return True
        return False

    def next_point():
        t, z = next(gen)
        if crash(t, z):
            timer.stop()
            return
        if t % (15*100) == 0:
            for body, body_ellipse in zip(bodies, body_ellipses):
                d = body[1]
                p = body[2](t)
                x = p.real - d/2
                y = p.imag - d/2
                body_ellipse.setRect(x, y, d, d)
            x = append(line.xData, z.real)
            y = append(line.yData, z.imag)
            line.setData(x, y)
    
    timer.timeout.connect(next_point)
    return timer
