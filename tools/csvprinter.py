import numpy as np

testarray = np.array([[0, -0.500000, -0.574707, -0.261158, 0],
[1, 0.500000, -0.655886, -0.763522, 1],
[2, -0.500000, -0.598257, -0.398858, 0],
[3, 0.500000, -0.067006, -0.457549, 1],
[4, -0.500000, -0.680920, -0.420982, 0]])

np.savetxt("tracer.csv",testarray,delimiter=',')