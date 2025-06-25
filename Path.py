import os
import csv

# ============= FILE MANAGEMENT =======================

def get_new_output_filename():
    folder = "output"
    os.makedirs(folder, exist_ok=True)
    i = 1
    while os.path.exists(os.path.join(folder, f"results{i}.csv")):
        i += 1
    return os.path.join(folder, f"results{i}.csv")
