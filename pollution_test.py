
"""A testfile for the poll sector"""
import pyworld3 

if __name__ == '__main__':
    
    pol = Pollution()
    pol.set_pollution_control()
    pol.init_pollution_constants()
    pol.init_pollution_variables()
    pol.init_exogenous_inputs()
    pol.set_pollution_delay_functions()
    pol.set_pollution_table_functions()
    pol.run_pollution()
    
   
    plot_world_variables(
            pol.time,
            [pol.ppgao, pol.ppgr, pol.ppgio, pol.ppgf],
            ["PPGAO", "PPGR", "PPGIO", "PPGF"],
            [[0.9*min(pol.ppgao), 1.1*max(pol.ppgao)], [0.9*min(pol.ppgr), 1.1*max(pol.ppgr)], 
            [0.9*min(pol.ppgio), 1.1*max(pol.ppgio)], [0.9*min(pol.ppgf), 1.1*max(pol.ppgf)]],
            figsize=(7, 5),
            grid=1,
            title='pollution',
        )
    plt.show()
