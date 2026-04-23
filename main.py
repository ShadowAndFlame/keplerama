from cmath import pi
from newton import *
from plot import *
from PyQt6.QtWidgets import QApplication # ty: ignore
from PyQt6.QtGui import QColor # ty: ignore

planet_mass = 5.9722e24 # kg
planet_diameter = 1.2756e7 # m
planet_radius = planet_diameter/2 # m
planet_position: TimePosition = stationary()
planet: Body = (planet_mass, planet_diameter, planet_position, 'blue')

moon_mass = 7.348e22 # kg
moon_diameter = 3.4748e6 # m
moon_radius = planet_diameter/2 # m
moon_orbit_radius = 3.84784e8 # m
moon_orbit_period = 2.360592e6 # s
moon_position: TimePosition = circular(moon_orbit_radius, moon_orbit_period, -pi/8)
moon: Body = (moon_mass, moon_diameter, moon_position, 'grey')

bodies: list[Body] = [
    planet,
    moon,
]

satellite_altitude: float = 4e5 # m
satellite_position: complex = (satellite_altitude + planet_radius)*1j # m
satellite_velocity: float = 7.67e3 # m/s ~spherical
# satellite_velocity: float = satellite_velocity * 1.25 # elliptical
satellite_velocity: float = satellite_velocity * 1.402 # moon encounter
# satellite_velocity: float = satellite_velocity * 1.45 # hyperbolic
# satellite_velocity: float = satellite_velocity * 0.982 # crash

start_time = 0 # s
timestep = 1 # s
max_time = 60*60*24*7 # s
step_count = int(max_time / timestep)

def main():
    app = QApplication([])
    # t, x, v, a = newton_loop(start_time, satellite_position, satellite_velocity, timestep, step_count, planet_mass)
    # plot_complex(x, planet_diameter)
    timer = plot_complex_live(newton_generator(start_time, satellite_position, satellite_velocity, timestep, bodies), bodies)
    timer.start()
    app.exec()
    
if __name__ == "__main__":
    main()
