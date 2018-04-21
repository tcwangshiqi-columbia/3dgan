import numpy as np
import scipy.io as io
from scipy.io import loadmat

np.set_printoptions(threshold=np.nan)

x = np.random.rand(1,64,64,64)

io.savemat("test",{"voxels":x})

mats = np.load("biasfree_600")
print mats.shape
#mats = loadmat("chair_demo.mat")
#print mats['voxels'].shape
mats = np.transpose(mats, (0,4,1,2,3))
io.savemat("new_chair",{"voxels":mats[0:1]})
