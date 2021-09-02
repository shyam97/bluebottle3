import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

import os 
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(dir_path)
  
myPath = dir_path+"/sim/output/tracer"
n = len([f for f in os.listdir(myPath) 
     if f.endswith('.csv') and os.path.isfile(os.path.join(myPath, f))])
# print(n)

for i in range(n):
    csvname = myPath+"/tracer-%d.csv" %i 
    tracerarray = np.array(pd.read_csv(csvname,header=None))
    count=0
    for j in range(len(tracerarray)):
        if tracerarray[j,1]>0.1:
            count+=1
    print(i,count)

