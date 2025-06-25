# ================= TDMA SOLVER =====================

def tdma(nodes, subdag, dag, supdag, d):
    for k in range(2, nodes + 1):
        subdag[k] /= dag[k - 1]
        dag[k] -= subdag[k] * supdag[k - 1]
        d[k] -= subdag[k] * d[k - 1]

    d[nodes] /= dag[nodes]
    for i in range(nodes - 1, 0, -1):
        d[i] = (d[i] - supdag[i] * d[i + 1]) / dag[i]
