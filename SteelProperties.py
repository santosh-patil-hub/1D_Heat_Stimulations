# ================== STEEL PROPERTIES =======================

def steelsolidusliquidus(pctcarbon):
    if pctcarbon < 0.1:
        tsolidus = 1534.0 - 410.0 * pctcarbon
    elif pctcarbon <= 0.1 and pctcarbon < 0.18:
        tsolidus = 1493
    else:
        tsolidus = 1527 - 189.07 * pctcarbon

    if pctcarbon < 0.51:
        tliquidus = 1534 - 80.39 * pctcarbon
    else:
        tliquidus = 1540.82 - 93.77 * pctcarbon

    return tsolidus, tliquidus

def steelcond(nodes, tliquidus, tsolidus, bumpf, thc, thetaold):
    for i in range(1, nodes + 1):
        if thetaold[i] < 801:
            thc[i] = (59.4 - 0.0418 * thetaold[i]) * 0.01
        elif thetaold[i] < tsolidus:
            thc[i] = (18.4 + 0.0094 * thetaold[i]) * 0.01
        elif thetaold[i] < tliquidus:
            zzz = 18.4 + 0.0094 * tsolidus
            thc[i] = (zzz + (43 - zzz) * (thetaold[i] - tsolidus) / (tliquidus - tsolidus)) * 0.01
        else:
            thc[i] = (43 * bumpf) * 0.01

def steelcp(nodes, tliquidus, tsolidus, thetaold, cp):
    for i in range(1, nodes + 1):
        T = thetaold[i]
        if T < 114.3:
            cp[i] = 0.498970
        elif T < 491.4:
            cp[i] = 0.456 + 2.0 * 0.0001888 * T
        elif T < 697.1:
            cp[i] = 0.268 + 2.0 * 0.0004180 * T
        elif T < 742.9:
            cp[i] = 1.431
        elif T < 868.6:
            cp[i] = 3.849 - 2.0 * 0.0001883 * T
        elif T < 1142.9:
            cp[i] = 0.648
        elif T < tsolidus:
            cp[i] = 0.268 + 2.0 * 0.000167 * T
        elif T < tliquidus:
            cp[i] = 0.268 + 2.0 * 0.0001888 * T + 272 / (tliquidus - tsolidus)
        else:
            cp[i] = 0.787

