# cell_segmentation
------------------------------------------------------------------------------------------------------------------------------------------
This project compares two different methods on an automated cell segmentation including conventional image processing method based on thresholding and morphological operation as well as overwhelming deep learning method based on u-net architecture.
(The architecture was inspired by http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/)

# data
The original dataset is available from IEEE ISBI challenge 2012.

It has been downloaded and pre-processed and you can find them in data folder

# segmentation algorithm

1.deep learning prediction

![image](http://github.com/Wxy-24/cell_segmentation/raw/master/img/unet_model_architecture.png)

2.Image processing based on thresholding

![image](http://github.com/Wxy-24/cell_segmentation/raw/master/img/thresholding.png)

# HOW to use?

This project depends on the following libraries:

1.Tensorflow

2.Keras >= 1.0

3.opencv

After ensuring necessary packages have been installed you can run main.py to have the result.

# example of results

![image](http://github.com/Wxy-24/cell_segmentation/raw/master/img/segmentation_exmaple.png)

