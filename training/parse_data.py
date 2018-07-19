import numpy as np
import os

def get_data():
    path = "../profils/"
    data = []
    label = []
    prof_id = -1
    profils = []
    a = -1
    img = 28
    n = 0
    for f in os.listdir(path):        
        content = open(path + f, "r").read().splitlines()
        prof_id += 1
        profils.append(f[:-3])
        for i in range(len(content)):
            if img == 28:
                data.append([])
                img = 0
                n = 0
                a += 1
                label.append(prof_id)       
            data[a].append([])
            line = content[i].split()    
            for j in range(len(line)):
                data[a][n].append(int(line[j]))
            img += 1
            n += 1
    return data, label, profils