import numpy as np
import random

def box_muller_transform():
    u1 = random.random()
    u2 = random.random()
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    return z0, z1

def asymgaus(mean, sigma_m, sigma_p):
    z0, z1 = box_muller_transform()
    if random.random() < 0.5:
        value = mean + sigma_m * z0
    else:
        value = mean + sigma_p * z1
    return value
