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
    global policy_year
    global io_ref
    
    io_ref = 0.5
    policy_year = 1900
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
def ifpc_control(t, world3, k):
    # ifpc control with feedback value     
    
    
    if not hasattr(ifpc_control, 'pid'):
        ifpc_control.pid = Pid_controller(world3.dt, 0.5, 0.1, 10)

    #fpc_ref.update(pop_ref, (world3.pop[k]/6e9),(230/400),(460/400))

    ifpc_control.pid.update(fpc_ref, (world3.fpc[k]/400),0.01)
    
    if t<=policy_year:
        return 1
    
    values = np.append(world3.ifpc_control_values[(k-2):k], ifpc_control.pid.val)
    val = np.mean(values)
    return val


def isopc_control(t, world3, k):
    # isopc control with feedback value     
    
    
    if not hasattr(isopc_control, 'pid'):
        isopc_control.pid = Pid_controller(world3.dt, 0.5, 0.005, 0.5)

    #sopc_ref.update(pop_ref, (world3.pop[k]/6e9),(100/400), (780/400))         
    
    isopc_control.pid.update(sopc_ref, (world3.sopc[k]/400), 0.01)

    if t<=policy_year:
        return 1
    
    values = np.append(world3.isopc_control_values[(k-2):k], isopc_control.pid.val)
    val = np.mean(values)

    return val


def fioac_control(t, world3, k):
    # fioac control with feedback value being fioai
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 0.5, 0.005, 1)

    #iopc_ref.update(pop_ref, (world3.pop[k]/6e9),(50/400),(216/400))
    
    fioai_ref.update(iopc_ref, (world3.iopc[k]/400))

    val = fioac_control.pid.update(world3.fioai[k], fioai_ref.val, 0.01, 1)

    if t<=policy_year:
        return 0.43

    #k_py = (policy_year-1900)/world3.dt
    #values = np.append(world3.fioac_control_values[(int(k_py)-5):k], fioac_control.pid.val)
    #val = np.mean(values)
    return val



def example6():
    # Controlling IO with FIOAI as outer loop and FIOAA, FIOAS and FIOAC as inner loop.
    global fioai_ref
    global iopc_ref
    global sopc_ref
    global fpc_ref
    global policy_year
    global pop_ref
    global average_num_ele

    average_num_ele = 100
    pop_ref = 0.5
    policy_year = 1950
    world3 = pyworld3.World3(year_max=2100) 
    fioai_ref = Pid_controller(world3.dt, 1.5, 0.01, 1)
    sopc_ref = 0.5
    iopc_ref = 0.25
    fpc_ref = 0.6
    #iopc_ref = Pid_controller(world3.dt, 0.5, 0.005, 5)
    #sopc_ref = Pid_controller(world3.dt, 0.5, 0.005, 5)
    #fpc_ref = Pid_controller(world3.dt, 0.5, 0.005, 5)

    world3.set_world3_control(fioac_control=fioac_control, isopc_control=isopc_control, ifpc_control=ifpc_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()

    
    plot_world_variables(
        world3.time,
        [world3.iopc, world3.fioai, world3.fioac, world3.nrfr],
        ["IOPC", "FIOAI","FIOAC", "NRFR"],
        [[0, 400], [0, 1], [0, 1], [0,1]],
        figsize=(7, 5),
        #img_background="./img/standard_run.jpg",
        grid=1,
        title="Taking away switching at policy year",
    )
    plt.show()

    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.fpc, world3.pop, world3.ppolx],
        ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
        [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
        figsize=(7, 5),
        img_background="./img/standard_run.jpg",
        grid=1,
        title="World3 standard run",
    )
    plt.show()
    """
    """
    plot_world_variables(
        world3.time,
        [(world3.iopc), (world3.io/1e12), (world3.nrfr), world3.pop, world3.sopc],
        ["IOPC", "IO", "NRFR", "POP", "SOPC"],
        [[0, 1.1*max(world3.iopc)], [0, 2], [0, 1.1], [0, 16e9], [0, 1.1*max(world3.sopc)]],
        figsize=(7, 5),
        #img_background="./img/fig7-7.png",
        grid=1,
        title='Cascade control for POP')
    plt.show()
    """
    """
    iopc_values = np.linspace(0,2000)
    plt.plot(iopc_values, world3.hsapc_f(iopc_values), 'r')
    plt.hlines(100, 0, 2000, 'b')
    plt.hlines(50, 0, 2000, 'g')
    plt.show()
    ehspc_values = np.linspace(0,230)
    plt.plot(ehspc_values, world3.lmhs1_f(ehspc_values), 'r')
    plt.plot(ehspc_values, world3.lmhs2_f(ehspc_values), 'b')
    plt.show()
    """
    
    """
    x_values = np.linspace(0, 1600)
    plt.plot(x_values, world3.pcrum_f(x_values), 'r')
    #plt.hlines(1, 0, 1600)
    plt.show()
    plt.plot(x_values, world3.cmi_f(x_values), 'b')
    plt.show()
    print(f"CMI för IOPC=100: {world3.cmi_f(100)}")
    print(f"CMI för IOPC=216: {world3.cmi_f(216)}")
    """
    

    
    



if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    example6()


