import numpy as np
import os

def get_data(path):
    data = []
    label =
    a = 0
    for f in os.listdir(path):
        data.append([])
        content = open(path + f, "r").read().splitlines()    
        for i in range(len(content)):
            data[a].append([])
            line = content[i].split()
            for j in range(len(line)):
                data[a][i].append(int(line[j]))
        a += 1    
    return data, label

data label = get_data("../profils/")

print(data)
            
              

    
