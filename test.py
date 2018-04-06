import numpy as np
import scipy.io as io
from scipy.io import loadmat

x = np.random.rand(1,64,64,64)

io.savemat("test",{"voxels":x})

mats = loadmat("chair_demo.mat")
io.savemat("new_chair",{"voxels":mats["voxels"][4:5]})
