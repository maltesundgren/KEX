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
  
""" FOR EXAMPLE"
def fioaa_control(t, world3, k):
    #Control function for fioai using the PID_controller class
    if not hasattr(fioaa_control, 'pid'):
        fioaa_control.pid = Pid_controller(world3.dt, 1, 0, 0)
        
    val = fioaa_control.pid.update((world3.io[k]/1e12),1)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val

def fioas_control(t, world3, k):
    #Control function for fioai using the PID_controller class
    if not hasattr(fioas_control, 'pid'):
        fioas_control.pid = Pid_controller(world3.dt, 1, 0, 0)
        
    val = fioas_control.pid.update((world3.io[k]/1e12),1)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val

def fioac_control(t, world3, k):
    #Control function for fioai using the PID_controller class
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 0.5, 0, 0)
        
    val = fioac_control.pid.update((world3.io[k]/1e12),1)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val
"""



def example1():
    # Business as usual
    pyworld3.hello_world3()
    

def example2():
    """fioaa, fioas control"""
    # Tuning the simulation
    world3 = pyworld3.World3(year_max=2500)                                      # choose the time limits and step.
    world3.set_world3_control(fioaa_control = fioaa_control, fioas_control=fioas_control, fioac_control=fioac_control)                                     # choose your controls
    world3.init_world3_constants()                                  # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()                                  # initialize all variables.
    world3.set_world3_table_functions()                             # get tables from a json file.
    world3.set_world3_delay_functions()                             # initialize delay functions.
    world3.run_world3()
    
    
    plot_world_variables(
        world3.time,
        [world3.fioaa, world3.fioai, world3.fioas, world3.fioac, world3.io/(1e12)],
        ["FIOAA", "FIOAI", "FIOAS", "FIOAC", "IO"],
        [[-0.1, 1.1], [-0.1, 1.1], [-0.1,1.1], [-0.1,1.1], [0,5]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FIOAA, FIOAC FIOAS CONTROL')
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
        [world3.fioai, world3.fioaa, world3.fioas, world3.fioac],
        ["FIOAI", "FIOAA", "FIOAS", "FIOAC"],
        [[-0.1, 1.1], [-0.1, 1.1], [-0.1, 1.1], [-0.1, 1.1] ],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FIO SIGNALS')
    plt.show()

def fcaor_control(t, world3, k):
    """FCAOR control function"""
    if not hasattr(fcaor_control, 'pid'):
        fcaor_control.pid = Pid_controller(world3.dt, 0.45, 0.01, 0.5)
        
    val = fcaor_control.pid.update((world3.io[k]/1e12),1)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def example4():
    """FCAOR control"""
      # Tuning the simulation
    world3 = pyworld3.World3(year_max=2500)                                      # choose the time limits and step.
    world3.set_world3_control(fcaor_control=fcaor_control)                                     # choose your controls
    world3.init_world3_constants()                                  # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()                                  # initialize all variables.
    world3.set_world3_table_functions()                             # get tables from a json file.
    world3.set_world3_delay_functions()                             # initialize delay functions.
    world3.run_world3()

    plot_world_variables(
        world3.time,
        [world3.fcaor, world3.io/1e12],
        ["FCAOR", "IO"],
        [[-0.1, 1.1], [0, 5]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FCAOR control')
    plt.show()

"""
def fioaa_control(t, world3, k):
    # fioaa control with feeback value being fioai
    if not hasattr(fioaa_control, 'pid'):
        fioaa_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)
        
    #fioai_ref.update(2, (world3.io[k]/1e12)) 
    val = fioaa_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def fioac_control(t, world3, k):
    # fioac control with feedback value being fioai
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)

    fioai_ref.update(0.5, (world3.io[k]/1e12))   
    val = fioac_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def fioas_control(t, world3, k):
    # fioac control with feedback value being fioai
    if not hasattr(fioas_control, 'pid'):
        fioas_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)

    #fioai_ref.update(2, (world3.io[k]/1e12))   
    val = fioas_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val
"""

def example5():
    # Trying to control fioai by fioaa, fioas and fioac.
    global fioai_ref
    #fioai_ref = 0.2
    world3 = pyworld3.World3(year_max=2500) 
    fioai_ref = Pid_controller(world3.dt, 1, 0.01, 0)
    #fioai_ref = lambda k: (0.5 if k <= 1 else fioai_ref_control(world3.time[k], world3, k - 1))                                    
    world3.set_world3_control(fioac_control=fioac_control, fioaa_control=fioaa_control, fioas_control=fioas_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()

    plot_world_variables(
        world3.time,
        [world3.fioai, (world3.io/1e12), world3.pop],
        ["FIOAI", "IO", "POP"],
        [[-0.1, 1.1], [0, 2], [0, 16e9]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='Cascade control for IO')
    plt.show()



# EXAMPLE 6
def fioac_control(t, world3, k):
    # fioac control with feedback value being fioai
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)

    if t<=policy_year:
        return 0.43

    io_ref.update(fpc_ref, (world3.fpc[k]/100))
    fioai_ref.update(io_ref.val, (world3.io[k]/1e12))   
    val = fioac_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def fioas_control(t, world3, k):
    # fioac control with feedback value being fioai
    if not hasattr(fioas_control, 'pid'):
        fioas_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)
   
    if t<=policy_year:
        return 1

    val = fioas_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def fioaa_control(t, world3, k):
    # fioaa control with feeback value being fioai
    if not hasattr(fioaa_control, 'pid'):
        fioaa_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 0)

    if t<=policy_year:
        return 1
    val = fioaa_control.pid.update(world3.fioai[k], fioai_ref.val)
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val



def example6():
    # Trying to control fioai by fioaa, fioas and fioac.
    global fioai_ref
    global io_ref
    global policy_year
    global fpc_ref

    policy_year = 1950
    fpc_ref = 400
    world3 = pyworld3.World3(year_max=2100) 
    fioai_ref = Pid_controller(world3.dt, 0.5, 0.01, 0)
    io_ref = Pid_controller(world3.dt, 1, 0.01, 0)

    world3.set_world3_control(fioac_control=fioac_control, fioaa_control=fioaa_control, fioas_control=fioas_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()

    plot_world_variables(
        world3.time,
        [world3.fioai, (world3.iopc), (world3.pop), world3.fpc, world3.ppolx, world3.nrfr],
        ["FIOAI", "IOPC", "POP", "FPC", "PPOLX", "NRFR"],
        [[-0.1, 1.1], [0, 1000], [0, 16e9], [0, 1000], [0,32], [0, 1]],
        figsize=(7, 5),
        img_background="./img/fig7-7.png",
        grid=1,
        title='Cascade control for POP by having FPC as reference value')
    plt.show()


if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    example6()


