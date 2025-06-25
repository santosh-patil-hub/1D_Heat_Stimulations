# ================= INITIAL CONDITIONS ======================

import os
import csv


def startvalues(thetaold):
    input_path = os.path.join("input", "input.csv")
    with open(input_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)[0]  

    billet_length = float(data["L"]) * 100  # convert m to cm
    theta_initial = float(data["Tinitial"])
    hl = float(data["hl"]) * 0.01*.01
    hr = float(data["hr"]) * 0.01*.01
    t_air_left = float(data["air left"])
    t_air_right = float(data["air right"])
    rho = float(data["rho"])
    pctcarbon = float(data["Carbon"])
    nodes = int(data["nodes"])
    delt = float(data["del t"])
    total_time = float(data["total_time"])
    bumpf = float(data["bumpf"])
    nwrite = int(data["nwrite"])
    irow = 0

    delx = billet_length / (nodes - 1)

    for i in range(1, nodes + 1):
        thetaold[i] = theta_initial

    return nodes, bumpf, delx, delt, total_time, hl, hr, t_air_left, t_air_right, rho, pctcarbon, nwrite, irow
