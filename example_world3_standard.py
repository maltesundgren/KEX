# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from pyworld3 import World3
from pyworld3.utils import plot_world_variables

params = {"lines.linewidth": "3"}
plt.rcParams.update(params)

world3 = World3(year_max=2200)
world3.set_world3_control()
world3.init_world3_constants()
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

plot_world_variables(
    world3.time,
    [world3.nrfr, world3.iopc, world3.fcaor,],
    ["NRFR\n[]", "IOPC\n[$/py]", "FCAOR\n[]"],
    [[0, 1.05], [0,0.6e3], [0,1.05]],
    #img_background="./img/fig7-7.png",
    figsize=(7, 5),
    #title="World3 standard run - POP",
)
plt.savefig("fig_world3_standard_Cost_of_Resources.pdf")

"""
plot_world_variables(
    world3.time,
    [world3.nrfr, world3.iopc, world3.ppolx,],
    ["NRFR\n[]", "IOPC\n[$/py]", "PPOLX\n[]"],
    [[0, 1], [0,0.6e3] ,[0,16]],
    #img_background="./img/fig7-7.png",
    figsize=(7, 5),
    #title="World3 standard run - POP",
)
plt.savefig("fig_world3_standard_POP_IO_PPOLX.pdf")
"""
"""
plot_world_variables(
    world3.time,
    [world3.fpc, world3.sopc, world3.pop],
    ["FPC\n      [ve kg/py]", "SOPC\n[$/py]", "POP\n[p]"],
    [[0,0.6e3], [0,1e3], [0, 9e9]],
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
    [[0,1], [0, 9e9]],
    #img_background="./img/fig7-7.png",
    figsize=(7, 5),
    #title="World3 standard run - POP",
)
plt.savefig("fig_world3_standard_2500_POP_NRFR.pdf")
"""
"""
plot_world_variables(
    world3.time,
    [world3.fcaor, world3.io, world3.tai, world3.aiph, world3.fioaa],
    ["FCAOR", "IO", "TAI", "AI", "FIOAA"],
    [[0, 1], [0, 4e12], [0, 4e12], [0, 2e2], [0, 0.201]],
    img_background="./img/fig7-8.png",
    figsize=(7, 5),
    title="World3 standard run - Capital sector",
)
plt.savefig("fig_world3_standard_capital.pdf")

plot_world_variables(
    world3.time,
    [world3.ly, world3.al, world3.fpc, world3.lmf, world3.pop],
    ["LY", "AL", "FPC", "LMF", "POP"],
    [[0, 4e3], [0, 4e9], [0, 8e2], [0, 1.6], [0, 16e9]],
    img_background="./img/fig7-9.png",
    figsize=(7, 5),
    title="World3 standard run - Agriculture sector",
)
plt.savefig("fig_world3_standard_agriculture.pdf")
"""