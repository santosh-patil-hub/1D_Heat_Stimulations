import csv
import os

def endofiteration(i, delt, nodes, total_time, delx, d, thetaold, thetanew, nwrite, irow, output_file):
    for k in range(1, nodes + 1):
        thetaold[k] = d[k]

    current_time = i * delt

    if i % nwrite == 0:
        first_node = 1
        second_node = 2
        third_node = 3
        center = nodes // 2
        mid_left = center - 1
        mid_right = center + 1
        third_last_node = nodes - 2
        second_last_node = nodes - 1
        last_node = nodes

        write_header = not os.path.exists(output_file)
        with open(output_file, 'a', newline='') as file:
            writer = csv.writer(file)

            if write_header:
                writer.writerow([
                    "Time(s)",
                    f"Node {first_node}",
                    f"Node {second_node}",
                    f"Node {third_node}",
                    f"Node {mid_left}",
                    f"Node {center} (Center)",
                    f"Node {mid_right}",
                    f"Node {third_last_node} (Third Last)",
                    f"Node {second_last_node} (Second Last)",
                    f"Node {last_node} (Last)"
                ])

            writer.writerow([
                round(current_time, 2),
                round(thetaold[first_node], 2),
                round(thetaold[second_node], 2),
                round(thetaold[third_node], 2),
                round(thetaold[mid_left], 2),
                round(thetaold[center], 2),
                round(thetaold[mid_right], 2),
                round(thetaold[third_last_node], 2),
                round(thetaold[second_last_node], 2),
                round(thetaold[last_node], 2)
            ])

    return irow + 1
