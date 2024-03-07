import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3


def simulation(world3,title_name):
    """function that makes a plot of a given simulation with the title of the figure as input"""

    plot_world_variables(
            world3.time,
            [world3.io, world3.ic, world3.fioai],
            ["IO", "IC", "FIOAI"],
            [[0.9*min(world3.ic), 1.1*max(world3.ic)], [0.9*min(world3.ic), 1.1*max(world3.ic)], [0.9*min(world3.fioai), 1.1*max(world3.fioai)]],
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
    
    
def icor_control(t, world3, k):
    return 1 - world3.fcaor[k]


def fioai_control(t, world3, k):
    ref=0.4
    P=0.95
    if (ref-world3.fioai[k])*P<0:
        return 0.1
    else:
        if (ref-world3.fioai[k])*P <=1:
            return(ref-world3.fioai[k])*P
        
        else:
            return 1


def example2():
    # Tuning the simulation
    world3 = pyworld3.World3()           # choose the time limits and step.
    world3.set_world3_control(fioai_control=fioai_control)          # choose your controls
    world3.init_world3_constants()       # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()       # initialize all variables.
    world3.set_world3_table_functions()  # get tables from a json file.
    world3.set_world3_delay_functions()  # initialize delay functions.
    world3.run_world3()
    #iopc = np.linspace(1,1600)
    #plt.plot(iopc, world3.pcrum_f(iopc))
    #plt.show()
    print(max(world3.io)/max(world3.ppol))
    print(world3.pop[-1])
    simulation(world3, "Tuning the pollution sector")




if __name__ == "__main__":
    #example1()
    example2()



