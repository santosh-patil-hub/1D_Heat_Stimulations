import numpy as np
from HeatEquations1d import surface_left, interior, surface_right
from InitialConditions import startvalues
from SteelProperties import steelsolidusliquidus , steelcond, steelcp
from TridagSolver import tdma   
from Path import get_new_output_filename
from Writes import endofiteration

def main():
    thetaold = np.zeros(10000)
    thetanew = np.zeros(10000)
    cp = np.zeros(10000)
    thc = np.zeros(10000)
    subdag = np.zeros(10000)
    dag = np.zeros(10000)
    supdag = np.zeros(10000)
    d = np.zeros(10000)

    nodes, bumpf, delx, delt, total_time, hl, hr, t_air_left, t_air_right, rho, pctcarbon, nwrite, irow = startvalues(thetaold)
    tsolidus, tliquidus = steelsolidusliquidus(pctcarbon)
    total_iterations = round(total_time / delt)
    output_file = get_new_output_filename()

    for i in range(1, total_iterations + 1):
        steelcond(nodes, tliquidus, tsolidus, bumpf, thc, thetaold)
        steelcp(nodes, tliquidus, tsolidus, thetaold, cp)
        surface_left(hl, t_air_left, rho, delt, delx, thetaold, thc, cp, subdag, dag, supdag, d)
        interior(rho, delt, delx, nodes, thetaold, thc, cp, subdag, dag, supdag, d)
        surface_right(hr, t_air_right, rho, delt, delx, nodes, thetaold, thc, cp, subdag, dag, supdag, d)
        tdma(nodes, subdag, dag, supdag, d)
        irow = endofiteration(i, delt, nodes, total_time, delx, d, thetaold, thetanew, nwrite, irow, output_file)

    print(f"✅ Simulation complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()


