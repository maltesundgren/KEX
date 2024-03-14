import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3
from Pid_controller import Pid_controller


def simulation(world3,title_name):
    """function that makes a plot of a given simulation with the title of the figure as input"""

    plot_world_variables(
        world3.time,
        #[world3.nrfr, world3.iopc, world3.fpc, world3.pop, world3.ppolx, world3.fioai],
        #["NRFR", "IOPC", "FPC", "POP", "PPOLX", "FIOAI"],
        #[[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32], [-0.1, 1.1]],
        [world3.fioaa, world3.io, world3.pop, world3.pcrum],
        ["FIOAA", "IO", "POP", "PCRUM"],
        [[-0.1, 1.1], [0, 1.1*max(world3.io)], [0, 16e9], [0, 1.1*max(world3.pcrum)]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title=title_name)
    plt.show()


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


def clip_func(x, x1,x2):
    """function that saturates the output to be y1 if less than x1 and y2 if more than x2"""
    if x<x1:
        return x1
    elif x>x2:
        return x2
    else:
        return x
    
PID_f = None
PID_i = None

def fioai_control(t, world3, k):
    """control function for fioai using the PID_controller class"""
    if t <= 1950:
        return 1 - world3.fioaa[k] - world3.fioas[k] - world3.fioac[k]

    global PID
    if PID == None: 
        PID = Pid_controller(world3.dt, 0.2, 0.4, 0.066)
        
    val = PID.update(0.2, world3.fioai[k], world3.fioai[k-1])
    clipped_val = clip_func(val, 0.01,1)
    return clipped_val


def nruf_control(t, world3, k):
    """control function for fcaor using the PID_controller class"""
    global PID
    if PID == None:
        PID = Pid_controller(world3.dt, 0.2, 0.4, 0.066)
    
    val = PID.update(1, world3.nrfr[k])
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def fioaa_control(t, world3, k):
    """control function for fcaor using the PID_controller class"""
    global PID_f
    if PID_f == None:
        PID_f = Pid_controller(world3.dt, 0.2, 0.4, 0.066)
    
    val = PID_f.update(0.6, world3.fioai[k])
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val


def ifpc_control(t, world3, k):
    """control function for fcaor using the PID_controller class"""
    global PID_i
    if PID_i == None:
        PID_i = Pid_controller(world3.dt, 0.2, 0.4, 0.066)
    
    val = PID_i.update(0.6, world3.fioai[k])
    clipped_val = clip_func(val, 0.01, 1)
    return clipped_val

# Ku = 1
# Tu = 1 year

# Classic PID
# Kp = 0.6 * Ku         = 0.6
# Ki = 1.2 * Ku/Tu      = 1.2
# Kd = 0.075 * Ku * Tu  = 0.075

def example1():
    # Business as usual
    pyworld3.hello_world3()
    

def example2():
    # Tuning the simulation
    world3 = pyworld3.World3()                                      # choose the time limits and step.
    world3.set_world3_control(fioaa_control=fioaa_control,ifpc_control=ifpc_control)                                     # choose your controls
    world3.init_world3_constants()                                  # choose the model constants. pet=1950 caps value of population
    world3.init_world3_variables()                                  # initialize all variables.
    world3.set_world3_table_functions()                             # get tables from a json file.
    world3.set_world3_delay_functions()                             # initialize delay functions.
    world3.run_world3()
    
    #iopc = np.linspace(1,1600)
    #plt.plot(iopc, world3.pcrum_f(iopc))
    #plt.show()
    print(max(world3.io))
    simulation(world3, "Tuning the pollution sector")



if __name__ == "__main__":
    #example1()
    example2()
    #example3()



