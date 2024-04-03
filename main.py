import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3
from Pid_controller import Pid_controller


def ifpc_control(t, world3, k):
    # ifpc control with feedback value     
    if t<=policy_year_f:
        return 1
    
    if not hasattr(ifpc_control, 'pid'):
        ifpc_control.pid = Pid_controller(world3.dt, 15, 0.08, 0)

    ifpc_control.pid.update(fpc_ref, (world3.fpc[k]/400),0.01)
    
    values = np.append(world3.ifpc_control_values[(k-10):k], ifpc_control.pid.val)
    val = np.mean(values)
    return val


def isopc_control(t, world3, k):
    # isopc control with feedback value     
    
    if t<=policy_year_so:
        return 1

    if not hasattr(isopc_control, 'pid'):
        isopc_control.pid = Pid_controller(world3.dt, 50, 0.02, 2)        
    
    isopc_control.pid.update(sopc_ref, (world3.sopc[k]/400), 0.01)
    
    values = np.append(world3.isopc_control_values[(k-10):k], isopc_control.pid.val)
    val = np.mean(values)

    return val


def fioac_control(t, world3, k):
    # fioac control with feedback value being fioai
    if t<=policy_year_io:
        return 0.43
    
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 20, 0.01, 2)

    val = fioac_control.pid.update((world3.iopc[k]/400), iopc_ref, 0.01, 1)

    values = np.append(world3.fioac_control_values[(k-10):k], fioac_control.pid.val)
    val = np.mean(values)
    return val



def example6():
    # Controlling IO with FIOAI as outer loop and FIOAA, FIOAS and FIOAC as inner loop.
    global fioai_ref
    global iopc_ref
    global sopc_ref
    global fpc_ref
    global policy_year_io
    global policy_year_f
    global policy_year_so

    policy_year_io = 1970
    policy_year_f = 2120
    policy_year_so = 2130
    world3 = pyworld3.World3(year_max=2200) 
    sopc_ref = 0.8
    iopc_ref = 0.3
    fpc_ref = 0.7

    world3.set_world3_control(fioac_control=fioac_control, isopc_control=isopc_control, ifpc_control=ifpc_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()

    
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.fpc, world3.pop, world3.sopc],
        ["NRFR\n[]", "IOPC\n[$/py]", "FPC\n[ve kg/py]", "POP\n[p]", "SOPC\n[$/py]"],
        [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 1e3]],
        figsize=(7, 5),
        img_background="./img/STD_2200_SOPC.png",
        #img_background="./img/standard_run.jpg",
        grid=1,
        title="Control of World3 vs standard run",
    )
    plt.savefig("fig_STD_2200.png")
    

    

    
    



if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    example6()


