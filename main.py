import pyworld3
from pyworld3.utils import plot_world_variables
import matplotlib.pyplot as plt
import numpy as np
from pyworld3.specials import Delay3
from Pid_controller import Pid_controller


def ifpc_control(t, world3, k):
    # ifpc control with feedback from FPC normalized with 400    
    if t<=policy_year_fpc:
        return 1
    
    if not hasattr(ifpc_control, 'pid'):
        ifpc_control.pid = Pid_controller(world3.dt, 15, 0.08, 0)

    ifpc_control.pid.update(fpc_ref, (world3.fpc[k]/400),0.01)
    
    values = np.append(world3.ifpc_control_values[(k-10):k], ifpc_control.pid.val)
    val = np.mean(values)
    return val


def isopc_control(t, world3, k):
    # isopc control with feedback from SOPC normalized with 400     
    if t<=policy_year_sopc:
        return 1

    if not hasattr(isopc_control, 'pid'):
        isopc_control.pid = Pid_controller(world3.dt, 50, 0.02, 2)        
    
    isopc_control.pid.update(sopc_ref, (world3.sopc[k]/400), 0.01)
    
    values = np.append(world3.isopc_control_values[(k-10):k], isopc_control.pid.val)
    val = np.mean(values)

    return val


def fioac_control(t, world3, k):
    # fioac control with feedback from IOPC normalized with 400
    if t<=policy_year_iopc:
        return 0.43
    
    if not hasattr(fioac_control, 'pid'):
        fioac_control.pid = Pid_controller(world3.dt, 20, 0.01, 2)

    val = fioac_control.pid.update((world3.iopc[k]/400), iopc_ref, 0.01, 1)

    values = np.append(world3.fioac_control_values[(k-10):k], fioac_control.pid.val)
    val = np.mean(values)
    return val



def main():
    # Controlling POP with policy years and control signals FIOAC, IFPC and ISOPC
    global iopc_ref
    global sopc_ref
    global fpc_ref
    global policy_year_iopc
    global policy_year_fpc
    global policy_year_sopc

    policy_year_iopc = 1972
    policy_year_fpc = 2120
    policy_year_sopc = 2130     # Value * 400
    sopc_ref = 0.8              # 320
    iopc_ref = 0.3              # 120
    fpc_ref = 0.7               # 280

    world3 = pyworld3.World3(year_max=2200) 
    world3.set_world3_control(fioac_control=fioac_control, isopc_control=isopc_control, ifpc_control=ifpc_control)                                   
    world3.init_world3_constants()                                 
    world3.init_world3_variables()                              
    world3.set_world3_table_functions()                             
    world3.set_world3_delay_functions()                             
    world3.run_world3()



    params = {"lines.linewidth": "3"}
    plt.rcParams.update(params)

    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.ppolx,],
        ["NRFR\n[]", "IOPC\n[$/py]", "PPOLX\n[]"],
        [[0, 1], [0,0.6e3] ,[0,16]],
        img_background="./img/POP_IO_PPOLX_2200.png",
        figsize=(7, 5),
        #title="World3 standard run - POP",
    )
    plt.savefig("fig_control_comp_STD_nr_io_ppolx.pdf")
    """
    """
    plot_world_variables(
        world3.time,
        [world3.fpc, world3.sopc, world3.pop,],
        ["FPC\n      [ve kg/py]", "SOPC\n[$/py]", "POP\n[p]"],
        [[0,0.6e3], [0,1e3], [0, 16e9]],
        #img_background="./img/fig7-7.png",
        figsize=(7, 5),
        #title="World3 standard run - POP",
    )
    plt.savefig("fig_world3_standard_POP_SO_F.pdf")
    """
    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.pop],
        ["NRFR\n[]", "POP\n[p]"],
        [[0,1], [0, 16e9]],
        #img_background="./img/fig7-7.png",
        figsize=(7, 5),
        #title="World3 standard run - POP",
    )
    plt.savefig("fig_world3_standard_2500_POP_NRFR.pdf")
    """


    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.fpc, world3.pop, world3.sopc],
        ["NRFR", "IOPC", "FPC", "POP", "SOPC"],
        [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 1e3]],
        figsize=(7, 5),
        img_background="./img/STD_2200_SOPC.png",
        #img_background="./img/standard_run.jpg",
        grid=1,
        title="Control of World3 vs standard run",
    )
    plt.savefig("fig_STD_2200.png")
    """
    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.pop],
        ["NRFR", "IOPC", "POP"],
        [[0, 1], [0, 1e3], [0, 16e9]],
        figsize=(7, 5),
        img_background="./img/NRFR_IOPC_POP_2500.png",
        grid=1,
        title="Population of controlled World3 vs standard run",
    )
    plt.savefig("fig_STD_2500.png")
    """
    """
    plot_world_variables(
        world3.time,
        [world3.nrfr, world3.iopc, world3.fpc, world3.sopc],
        ["NRFR", "IOPC", "FPC", "SOPC"],
        [[0, 1], [0, 1e3], [0, 1e3], [0, 1e3]],
        figsize=(7, 5),
        #img_background="./img/control_2200.png",
        #img_background="./img/standard_run.jpg",
        grid=1,
        title="Control of World3")
    plt.savefig("fig_control_2200.png")
    """
    """
    plot_world_variables(
        world3.time,
        [world3.pop, world3.ppolx],
        ["POP", "PPOLX"],
        [[0, 9e9], [0,24]],
        figsize=(7, 5),
        img_background="img/PPOLX_bakgrund.png",
        #img_background="./img/standard_run.jpg",
        grid=1,
        title="PPOLX")
    plt.savefig("fig_ppolx.png")
    """
    """
    fpc_ifpc = np.linspace(0, 3)
    plt.figure("fioaa_f")
    plt.plot(fpc_ifpc, world3.fioaa_f(fpc_ifpc))
    plt.xlabel("FPC/IFPC")
    plt.ylabel("FIOAA")
    plt.savefig("fioaa_f.png")

    sopc_isopc = np.linspace(0, 2.5)
    plt.figure("fioas_f")
    plt.plot(sopc_isopc, world3.fioas_f(sopc_isopc))
    plt.xlabel("SOPC/ISOPC")
    plt.ylabel("FIOAS")
    plt.savefig("fioas_f.png")

    fpc_sfpc = np.linspace(0,6)
    plt.figure("lmf_f")
    plt.plot(fpc_sfpc, world3.lmf_f(fpc_sfpc))
    plt.xlabel("FPC/SFPC")
    plt.ylabel("LMF")
    plt.savefig("lmf_f.png")

    sopc = np.linspace(0, 2100)
    plt.figure("hsapc_f")
    plt.plot(sopc, world3.hsapc_f(sopc))
    plt.xlabel("SOPC")
    plt.ylabel("HSAPC")
    plt.savefig("hsapc_f.png")

    iopc = np.linspace(0, 1700)
    plt.figure("cmi_f")
    plt.plot(iopc, world3.cmi_f(iopc))
    plt.xlabel("IOPC")
    plt.ylabel("CMI")
    plt.savefig("cmi_f.png")
    """

    

    
    
    
    



if __name__ == "__main__":
    main()


