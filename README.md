# 3dgan

## Data:
Download the training data from the 3D Shapenet [website](http://3dshapenets.cs.princeton.edu/3DShapeNetsCode.zip "")

## Files:
#### /python:  
Code for visulization of objects.

| File          | Description  |
| ------------- | ------------ |
| visualize.py   |visualize object represented as voxels using vtk  |


#### /src:  
Code for model training and testing. 

| File          | Description  |
| ------------- | ------------ |
| 3dgan_mit_biasfree.py|3d-GAN model training and testing file                               |
| dataIO.py            |data input output                                                    |

#### /

| File          | Description  |
| ------------- | ------------ |
| chair_demo.mat|a mat file of chair object generated from the trained 3dgan model's generator |
| test.py.      |Transform .mat file into voxels for visualization input|


## References:
[1]
[Tensorflow implementation of 3D Generative Adversarial Network.](https://meetshah1995.github.io/gan/deep-learning/tensorflow/visdom/2017/04/01/3d-generative-adverserial-networks-for-volume-classification-and-generation.html "")
[[Github]](https://github.com/meetshah1995/tf-3dgan "")


[2]
[MIT Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling](http://3dgan.csail.mit.edu "")
[[Github]](https://github.com/zck119/3dgan-release "")


[3]
[Princeton 3D ShapeNets: A Deep Representation for Volumetric Shapes](http://3dshapenets.cs.princeton.edu "")



