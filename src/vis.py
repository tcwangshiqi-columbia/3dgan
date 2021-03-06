import visdom
import numpy as np
import scipy.io as io
from scipy.io import loadmat
import skimage.measure as sk

vis = visdom.Visdom()
#vis.text('Hello, world!')

def getVFByMarchingCubes(voxels, threshold=0.5):
    v, f =  sk.marching_cubes_classic(voxels, level=threshold)
    return v, f

def plotVoxelVisdom(voxels, visdom, title):
    v, f = getVFByMarchingCubes(voxels)
    visdom.mesh(X=v, Y=f, opts=dict(opacity=0.5, title=title))

#mats = loadmat("../../../3DShapeNets/volumetric_data/desk/30/train/desk_000000001_5.mat")
#mats = loadmat("image_chair_desk2.mat")
mats = np.load("interpolation_new1")
print mats.shape
#print (type(mats['voxels']),mats['voxels'].shape)
#plotVoxelVisdom(np.squeeze(mats['instance']>0.5), vis, 'chair')
for i in range(0,63,3):
	plotVoxelVisdom(np.squeeze(mats[i]>0.5), vis, 'image'+str(i))

#plotVoxelVisdom(np.squeeze(mats[0]>0.5), vis, 'image'+str(0))
#plotVoxelVisdom(np.squeeze(mats[49]>0.5), vis, 'image'+str(49))


#v, f = getVFByMarchingCubes(mats['instance'])
#vis.mesh(X=v, Y=f, opts=dict(opacity=0.5, title='chair_desk'))
