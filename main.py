import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3


def simulation(world3,title_name):
    """function that makes a plot of a given simulation with the title of the figure as input"""

    plot_world_variables(
            world3.time,
            [world3.ppolx, world3.al, world3.pop, world3.fioaa, world3.aiph, world3.pcrum],
            ["PPOLX", "AL", "POP", "FIOAA", "AIPH", "PCRUM"],
            [[0.9*min(world3.ppolx), 1.1*max(world3.ppolx)], [0.9*min(world3.al), 1.1*max(world3.al)],
            [0.9*min(world3.pop), 1.1*max(world3.pop)],[0.9*min(world3.fioaa), 1.1*max(world3.fioaa)], 
            [0.9*min(world3.aiph), 1.1*max(world3.aiph)], [0.9*min(world3.pcrum), 1.1*max(world3.pcrum)]],
            figsize=(7, 5),
            grid=1,
            title=title_name,
        )
    plt.show()

def example1():
    # Business as usual
    pyworld3.hello_world3()


def ppgf_control(t, world3, k):
    #if world3.ppolx[k] <= 1.5:
    #    return 1
    #else: 
    #    return 0.1
    ref = 3
    K = 0.5
    if abs((ref-world3.ppolx[k])*K)<=1:
        if (ref-world3.ppolx[k])*K<0:
            return 0
        return (ref-world3.ppolx[k])*K
    else:
        return 1

def al_control(t, world3, k):
    ref=1.632e8
    P=0.5
    if abs((ref-world3.ppol[k])*P)<=0.9e9:
        if ((ref-world3.ppol[k])*P)<0:
            return 0.1
        else:
            return (ref-world3.ppol[k])*P
    else:
        return 0.9e9


def example2():
    # Tuning the simulation
    world3 = pyworld3.World3()           # choose the time limits and step.
    world3.set_world3_control(al_control=al_control)          # choose your controls
    world3.init_world3_constants()       # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()       # initialize all variables.
    world3.set_world3_delay_functions()  # initialize delay functions.
    world3.set_world3_table_functions()  # get tables from a json file.
    world3.run_world3()
    #iopc = np.linspace(1,1600)
    #plt.plot(iopc, world3.pcrum_f(iopc))
    #plt.show()
    print(max(world3.io)/max(world3.ppol))
    print(world3.pop[-1])
    simulation(world3, "Tuning the pollution sector")


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



