G = 6.67430e-11 # m^3/kgs^2

def magnitude(c: complex) -> float:
    return abs(c)

def direction(c: complex) -> complex:
    return c / magnitude(c)

def g(m: float, x: complex) -> complex:
    return (G*m / magnitude(x)**2) * -direction(x) # m / s^2

def step(t1: float, x1: complex, v1: complex, a1: complex, dt: float, m: float) -> tuple[float, complex, complex, complex]:
    t2: float = t1 + dt
    a2: complex = g(m, x1) # m/s^2
    v2: complex = v1 + a2*dt # m/s
    x2: complex = x1 + v2*dt # m
    return t2, x2, v2, a2

def loop(t0: float, x0: complex, v0: complex, dt: float, t_count: int, m: float) -> tuple[list[float], list[complex], list[complex], list[complex]]:
    t: list[float] = [t0]
    x: list[complex] = [x0]
    v: list[complex] = [v0]
    a: list[complex] = [g(m, x0)]
    for _ in range(t_count):
        t1: float = t[-1]
        x1: complex = x[-1]
        v1: complex = v[-1]
        a1: complex = a[-1]
        t2, x2, v2, a2 = step(t1, x1, v1, a1, dt, m)
        t.append(t2)
        x.append(x2)
        v.append(v2)
        a.append(a2)
    return t, x, v, a
