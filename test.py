import numpy as np
import scipy.io as io
from scipy.io import loadmat
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan)

#x = np.random.rand(1,64,64,64)

#io.savemat("test",{"voxels":x})

mats = np.load("src/interpolation3")
print mats.shape

batch_size = 200
#mats = mats>0.5
d = []
for i in range(0,200, 10):
	d.append(np.sum(np.absolute(mats[i]-mats[0])))
	#print np.sum(np.absolute(mats[i]-mats[100]))

plt.plot(range(20),d)
plt.show()
#mats = loadmat("chair_demo.mat")
#print mats['voxels'].shape
#mats = np.transpose(mats, (0,4,1,2,3))
#io.savemat("new_chair",{"voxels":mats[0:1]})
