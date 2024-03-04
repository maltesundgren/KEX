
"""A testfile for the poll sector"""
import pyworld3
from pyworld3.pollution import *
import numpy as np

if __name__ == '__main__':
    
    pol = Pollution(1900, 2100)
    pol.set_pollution_control()
    pol.init_pollution_constants()
    pol.init_pollution_variables()
    pol.init_exogenous_inputs()
    pol.set_pollution_delay_functions()
    pol.set_pollution_table_functions()
    pol.run_pollution()
    
   
    plot_world_variables(
            pol.time,
            [pol.ppgao, pol.ppgr, pol.ppgio, pol.ppgf, pol.pop ],
            ["PPGAO", "PPGR", "PPGIO", "PPGF", "POP"],
            [[0.9*min(pol.ppgao), 1.1*max(pol.ppgao)], [0.9*min(pol.ppgr), 1.1*max(pol.ppgr)], 
            [0.9*min(pol.ppgio), 1.1*max(pol.ppgio)], [0.9*min(pol.ppgf), 1.1*max(pol.ppgf)], [0.9*min(pol.pop), 1.1*max(pol.pop)]],
            figsize=(7, 5),
            grid=1,
            title='pollution',
        )
    plt.show()
    
    """Plots ahlm as function of ppolx"""
    ppolx = np.linspace(0,1001)
    plt.plot(ppolx, pol.ahlm_f(ppolx))
    plt.show()

    print(pol.ahlm_f(0))
    print(pol.ahlm_f(0.5))
    print(pol.ahlm_f(1))
    print(pol.ahlm_f(2))
