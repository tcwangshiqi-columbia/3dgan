# 3dgan

## Data:
Training data in /3DShapeNets/volumetric_data/

## Files:
/python: code for visulization of objects
/src: code for model training and testing
3dgan_mit_biasfree1.py:	3dgan model 
dataIO.py:	data input output and plotting utilities.
utils.py:	tensorflow utils like leaky_relu and batch_norm layer.

chair_demo.mat: a mat file of chair object generated from a trained 3dgan model's generator (input for visualization)
test.py: 




## References:
[1]
[Tensorflow implementation of 3D Generative Adversarial Network.](https://meetshah1995.github.io/gan/deep-learning/tensorflow/visdom/2017/04/01/3d-generative-adverserial-networks-for-volume-classification-and-generation.html "")
[[Github]](https://github.com/meetshah1995/tf-3dgan "")


[2]
[MIT Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling](http://3dgan.csail.mit.edu "")
[[Github]](https://github.com/zck119/3dgan-release "")


[3]
[Princeton 3D ShapeNets: A Deep Representation for Volumetric Shapes](http://3dshapenets.cs.princeton.edu "")



