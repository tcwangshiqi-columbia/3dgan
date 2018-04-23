import visdom
import numpy as np
import scipy.io as io
from scipy.io import loadmat
import skimage.measure as sk

vis = visdom.Visdom()
#vis.text('Hello, world!')

def getVFByMarchingCubes(voxels, threshold=0.9):
    v, f =  sk.marching_cubes_classic(voxels, level=threshold)
    return v, f

def plotVoxelVisdom(voxels, visdom, title):
    v, f = getVFByMarchingCubes(voxels)
    visdom.mesh(X=v, Y=f, opts=dict(opacity=0.5, title=title))

#mats = loadmat("../../../3DShapeNets/volumetric_data/desk/30/train/desk_000000001_5.mat")
#mats = loadmat("biasfree_9900")
#mats = np.load("./train_sample_new/biasfree_30")
#print (type(mats),mats.shape)
#plotVoxelVisdom(np.squeeze(mats['instance']>0.5), vis, 'chair')
#plotVoxelVisdom(np.squeeze(mats[0]>0.9), vis, 'biasfree_30.mat')

mats = np.load("./train_sample_new/biasfree_30")
#mats = np.transpose(mats, (0,4,1,2,3))
print (type(mats),mats.shape)
for i in range(32):	
	if mats[i].max() > 0.5:
		plotVoxelVisdom(np.squeeze(mats[i]>0.99), vis, '_'.join(map(str,[32,i])))          



#v, f = getVFByMarchingCubes(mats['instance'])
#vis.mesh(X=v, Y=f, opts=dict(opacity=0.5, title='chair_desk'))
