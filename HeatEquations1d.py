# ================= HEAT EQUATIONS ======================

def surface_left(hl, t_air_left, rho, delt, delx, thetaold, thc, cp, subdag, dag, supdag, d):
    kr = (2.0 * thc[1] * thc[2]) / (thc[1] + thc[2])
    subdag[1] = 0.0
    dag[1] = - (1 + (2.0 * hl) * delt / (rho * cp[1] * delx) + 2.0 * kr * delt / (rho * cp[1] * delx ** 2))
    supdag[1] = 2.0 * kr * delt / (rho * cp[1] * delx ** 2)
    d[1] = - (thetaold[1] + 2.0 * delt * hl * t_air_left / (rho * cp[1] * delx))

def interior(rho, delt, delx, nodes, thetaold, thc, cp, subdag, dag, supdag, d):
    for i in range(2, nodes):
        kl = 2.0 * thc[i] * thc[i - 1] / (thc[i] + thc[i - 1])
        kr = 2.0 * thc[i] * thc[i + 1] / (thc[i] + thc[i + 1])
        subdag[i] = kl * delt / (rho * cp[i] * delx ** 2)
        dag[i] = - (1 + kl * delt / (rho * cp[i] * delx ** 2) + kr * delt / (rho * cp[i] * delx ** 2))
        supdag[i] = kr * delt / (rho * cp[i] * delx ** 2)
        d[i] = -thetaold[i]

def surface_right(hr, t_air_right, rho, delt, delx, nodes, thetaold, thc, cp, subdag, dag, supdag, d):
    kl = 2.0 * thc[nodes - 1] * thc[nodes] / (thc[nodes - 1] + thc[nodes])
    subdag[nodes] = 2.0 * kl * delt / (rho * cp[nodes] * delx ** 2)
    dag[nodes] = - (1 + 2.0 * hr * delt / (rho * cp[nodes] * delx) + 2.0 * kl * delt / (rho * cp[nodes] * delx ** 2))
    supdag[nodes] = 0.0
    d[nodes] = - (thetaold[nodes] + 2.0 * delt * hr * t_air_right / (rho * cp[nodes] * delx))
