from newton import *
from plot import *
from PyQt6.QtWidgets import QApplication # ty: ignore

planet_mass = 5.9722e24 # kg
planet_diameter = 1.2756e7 # m
planet_radius = planet_diameter/2 # m

satellite_altitude = 4e5 # m
satellite_position = (satellite_altitude + planet_radius)*1j # m
satellite_velocity = 0.75*7.67e3 # m/s

start_time = 0 # s
timestep = 1 # s
max_time = 60*60*24*7 # s
step_count = int(max_time / timestep)

def main():
    app = QApplication([])
    # t, x, v, a = newton_loop(start_time, satellite_position, satellite_velocity, timestep, step_count, planet_mass)
    # plot_complex(x, planet_diameter)
    timer = plot_complex_live(newton_generator(start_time, satellite_position, satellite_velocity, timestep, planet_mass), planet_diameter)
    timer.start()
    app.exec()
    
if __name__ == "__main__":
    main()
