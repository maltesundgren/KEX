import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt


def simulation(world3,title_name):
    """function that makes a plot of a given simulation with the title of the figure as input"""

    plot_world_variables(
            world3.time,
            [world3.nrfr, world3.iopc, world3.fpc, world3.pop, world3.ppolx],
            ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
            [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
            figsize=(7, 5),
            grid=1,
            title=title_name,
        )
    plt.show()

def example1():
    # Business as usual
    pyworld3.hello_world3()


def example2():
    # Tuning the simulation
    world3 = pyworld3.World3(2000, 2500, 0.1)           # choose the time limits and step.
    world3.set_world3_control()          # choose your controls
    world3.init_world3_constants()       # choose the model constants.
    world3.init_world3_variables()       # initialize all variables.
    world3.set_world3_table_functions()  # get tables from a json file.
    world3.set_world3_delay_functions()  # initialize delay functions.
    world3.run_world3()
    simulation(world3, "Tuning the simulation")


def example3():
    # Open loop simulation
    import numpy as np
    icor_control = lambda t: min(3 * np.exp(-(t - 2023) / 50), 3) # This is the open loop control function

    world3 = pyworld3.World3(year_max=2100)
    world3.set_world3_control(icor_control=icor_control)
    world3.init_world3_constants()
    world3.init_world3_variables()
    world3.set_world3_table_functions()
    world3.set_world3_delay_functions()
    world3.run_world3(fast=False)
    simulation(world3, "Open loop")


def example4():
    # Closed loop simulation
    icor_control = lambda t, world, k: world.fioac[k] # This is the feedback control function

    world3 = pyworld3.World3(year_max=2100)
    world3.set_world3_control(icor_control=icor_control)
    world3.init_world3_constants()
    world3.init_world3_variables()
    world3.set_world3_table_functions()
    world3.set_world3_delay_functions()
    world3.run_world3(fast=False)
    simulation(world3, "Closed loop")


if __name__ == "__main__":
    #example1()
    example2()
    #example3()
    #example4()

