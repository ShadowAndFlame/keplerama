G = 6.67430e-11 # m^3/kgs^2

def magnitude(c: complex) -> float:
    return abs(c)

def direction(c: complex) -> complex:
    return c / magnitude(c)

def g(m: float, x: complex) -> complex:
    return (G*m / magnitude(x)**2) * direction(x) # m / s^2

def step(x0: complex, v0: complex, a0: complex, dt: float, m: float) -> tuple[complex, complex, complex]:
    x1: complex = x0 + v0*dt # m
    v1: complex = v0 + a0*dt # m/s
    a1: complex = g(m, x0) # m/s^2
    return x1, v1, a1
