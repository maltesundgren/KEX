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
  


# EXAMPLE 6
def fioac_control(t, world3, k):
    if t<=policy_year:
        return 0.43

    fioai_ref.update(io_ref, (world3.io[k]/1e12))
    
    clipped_val = clip_func(fioai_ref.val, 0.01, 1)
    
    return (1 - clipped_val)/3


def fioas_control(t, world3, k):
    # fioac control with feedback value being fioai
    if t<=policy_year:
        return 1

    fioai_ref.update(io_ref, (world3.io[k]/1e12))
    
    clipped_val = clip_func(fioai_ref.val, 0.01, (1/0.3))
    
    return (1 - clipped_val)/3


def fioaa_control(t, world3, k):
    # fioaa control with feeback value being fioai
    if t<=policy_year:
        return 1

    fioai_ref.update(io_ref, (world3.io[k]/1e12))
    
    clipped_val = clip_func(fioai_ref.val, 0.01, (1/0.4))
    
    return (1 - clipped_val)/3


def example6():
    # Controlling IO with FIOAI as outer loop and FIOAA, FIOAS and FIOAC as inner loop.
    global fioai_ref
    global io_ref
    global policy_year

    policy_year = 1900
    world3 = pyworld3.World3(year_max=2100) 
    fioai_ref = Pid_controller(world3.dt, 4, 0.1, 0)
    io_ref = 0.5

    world3.set_world3_control(fioac_control=fioac_control, fioaa_control=fioaa_control, fioas_control=fioas_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()


    print(world3.io[-1])

    plot_world_variables(
        world3.time,
        [world3.fioai, world3.fioaa, world3.fioas, world3.fioac, world3.io/1e12, world3.sopc/world3.isopc, world3.fpc/world3.ifpc],
        ["FIOAI", "FIOAA", "FIOAS", "FIOAC", "IO", "SOPC/ISOPC", "FPC/IFPC"],
        [[-0.1, 1.1], [-0.1, 1.1], [-0.1, 1.1], [-0.1, 1.1], [0,5], [0, 2.1], [0, 2.6]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='FIO SIGNALS')
    plt.show()


    

if __name__ == "__main__":
    example6()


