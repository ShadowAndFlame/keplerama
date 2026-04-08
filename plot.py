import pyqtgraph as pg

def plot_complex(z: list[complex]):
    reals = [zz.real for zz in z]
    imags = [zz.imag for zz in z]
    pg.plot(reals, imags, pen=None, symbol='o')
