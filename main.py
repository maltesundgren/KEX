import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3
from Pid_controller import Pid_controller

def clip_func(x, x1,x2):
    """function that saturates the output to be y1 if less than x1 and y2 if more than x2"""
    if x<x1:
        return x1
    elif x>x2:
        return x2
    else:
        return x
    
def fioai_control(t, world3, k):
    """Control function for fioai using the PID_controller class"""
    if not hasattr(fioai_control, 'pid_controller'):
        fioai_control.pid_controller = Pid_controller(world3.dt, 0.5, 0.001, 0)
        
    val = fioai_control.pid_controller.update(1, (world3.io[k]/1e12))
    clipped_val = clip_func(val, 0.001, 1)
    return clipped_val

    
def ifpc_control(t, world3, k):
    """Control function for ifpc using the PID_controller class"""
    if t < 2000:
        return world3.ifpc[k]
    
    if not hasattr(ifpc_control, 'pid'):
        ifpc_control.pid = Pid_controller(world3.dt, 0.0001, 0.001, 1)
    val = ifpc_control.pid.update(200, world3.ifpc[k])
    clipped_val = clip_func(val, 0.01, 500)

    return clipped_val


def fioaa_control(t, world3, k):
    """Control function for fioai using the PID_controller class"""
    if t < 1930:
         return 1
    
    if not hasattr(fioaa_control, 'pid_controller'):
        fioaa_control.pid_controller = Pid_controller(world3.dt, 0.6, 0, 0.5)
        
    val = fioaa_control.pid_controller.update((world3.io[k]/1e12), .5)
    clipped_val = clip_func(val, 0.001, 1)
    return clipped_val


def fioas_control(t, world3, k):
    """Control function for fioai using the PID_controller class"""
    if t < 1930:
         return 1
    if not hasattr(fioas_control, 'pid_controller'):
        fioas_control.pid_controller = Pid_controller(world3.dt, 0.6, 0, 0.5)
        
    val = fioas_control.pid_controller.update((world3.io[k]/1e12), .5)
    clipped_val = clip_func(val, 0.001, 1)
    return clipped_val


def fioac_control(t, world3, k):
    """Control function for fioai using the PID_controller class"""
    if t < 1930:
         return 1
    if not hasattr(fioac_control, 'pid_controller'):
        fioac_control.pid_controller = Pid_controller(world3.dt, 0.5, 0.00, 0)
        
    val = fioac_control.pid_controller.update((world3.io[k]/1e12), .5)
    clipped_val = clip_func(val, 0.001, 1)
    return clipped_val


def example1():
    # Business as usual
    pyworld3.hello_world3()
    

def example2():
    """fioai_control där fioai har ersats av en kontrollfunktion. KOD BEHÖVER ÄNDRAS FÖR DETTA I CAP-SEKTORN"""
    # Tuning the simulation
    world3 = pyworld3.World3(year_max=2500)                                      # choose the time limits and step.
    world3.set_world3_control(fioai_control = fioai_control)                                     # choose your controls
    world3.init_world3_constants()                                  # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()                                  # initialize all variables.
    world3.set_world3_table_functions()                             # get tables from a json file.
    world3.set_world3_delay_functions()                             # initialize delay functions.
    world3.run_world3()
    
    
    plot_world_variables(
        world3.time,
        [world3.fioai, world3.pop, world3.io/(1e12), world3.fpc, world3.ifpc],
        ["FIOAI", "POP", "IO", "FPC", "IFPC"],
        [[-0.1, 1.1], [0, 10e9], [0, 5], [0, 1.1*max(world3.fpc)],[0, 1.1*max(world3.ifpc)] ],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FIOAI CONTROL')
    plt.show()


def example3():
    """PLOT FIOAI, FIOAA, FIOAS AND FIOAC"""
    # Tuning the simulation
    world3 = pyworld3.World3(year_max=2100)                                      # choose the time limits and step.
    world3.set_world3_control(fioaa_control=fioaa_control, fioas_control=fioas_control, fioac_control=fioac_control)                                     # choose your controls
    world3.init_world3_constants()                                  # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()                                  # initialize all variables.
    world3.set_world3_table_functions()                             # get tables from a json file.
    world3.set_world3_delay_functions()                             # initialize delay functions.
    world3.run_world3()
    
    plot_world_variables(
        world3.time,
        [world3.io/1e12, world3.nrfr, world3.fioai, world3.fioaa, world3.fioas, world3.fioac],
        ["IO", "NRFR","FIOAI", "FIOAA", "FIOAS", "FIOAC"],
        [[0, 7], [0, 1], [0, 1], [0, .5], [0, .5], [0, 1] ],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FIO SIGNALS')
    plt.show()
    
    print(max(world3.io))


if __name__ == "__main__":
    #example1()
    example2()
    #example3()



