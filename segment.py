import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage.io as io
import os

# def Segment(test_path):

# get structure elements
# ac=[]
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# for i in range(4):
#     gt = io.imread(os.path.join("evaluation", "%d_label.png" % i), 0)
#     src = io.imread(os.path.join("evaluation", "%d.png" % i), 0)
#     # contrast enhanced
#     img_enhance = cv2.equalizeHist(src)
#     for j in range(99, 102):
#         for k in range(9, 12):
#             BiGaussian = cv2.bilateralFilter(img_enhance, 0, j, k)
#             # thresholding & subtract
#             for l in range(98, 101):
#                 for m in range(57, 60):
#                     retg, thg = cv2.threshold(BiGaussian, l, 255, cv2.THRESH_BINARY_INV)
#                     retg2, thg2 = cv2.threshold(BiGaussian, m, 255, cv2.THRESH_BINARY_INV)
#                     skeleton = thg - thg2
#                     # filtering
#                     median2 = cv2.medianBlur(skeleton, 3)
#                     d = cv2.morphologyEx(median2, cv2.MORPH_DILATE, kernel)
#                     mask = 255 - d
#                     # normalize
#                     gt =gt/255
#                     mask =mask/255
#                     r = gt - mask
#                     r[r < 0] = 1
#                     acc = (262144 - r.sum()) / 262144  # single accuracy
#                     record = [j, k, l, m, acc]
#                     ac.append(record)
# accuracy = np.array(ac)
# fac = []
# for j in range(99, 102):
#     for k in range(9, 12):
#         for l in range(98, 101):
#             for m in range(57, 60):
#                 sac = np.mean(accuracy[:, 4])
#                 fac = append([j, k, l, m, sac])
# fac = np.array(fac)
# maxac = fac[:, 4]
# coordinate = maxac.index(max(maxac))
# print(fac[coordinate, :])








#     return mask
#
# def SegmentTest(test_path,num_image = 30):
#     for i in range(num_image):
#         img = io.imread(os.path.join(test_path,"%d.png"%i),)
#         gt = cv2.imread("%d_label.png" % i, 0)
#         img=Segment(img)
#         io.imsave(os.path.join(test_path, "%d_process.png" % i), img)


# SegmentTest("evaluation")

#delete
# targetDir="evaluation"
# num_image=30
# for i in range(num_image):
#     targetFile = os.path.join(targetDir,"%d_process.png" % i)
#     if os.path.isfile(targetFile):
#         os.remove(targetFile)



combination=[]
ma = []

def Segment(src,j,k):
    # get structure elements
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # contrast enhanced
    img_enhance = cv2.equalizeHist(src)
    BiGaussian = cv2.bilateralFilter(img_enhance, 0, 88, 13)

    # thresholding & subtract
    retg, thg = cv2.threshold(BiGaussian,k, 255, cv2.THRESH_BINARY_INV)
    retgl, thg2 = cv2.threshold(BiGaussian,j, 255, cv2.THRESH_BINARY_INV)
    skeleton = thg - thg2

    # filtering
    median2 = cv2.medianBlur(skeleton, 3)
    d = cv2.morphologyEx(median2, cv2.MORPH_DILATE, kernel)
    mask = 255 - d
    plt.imshow(mask)
    return mask

def SegmentTest(test_path,gt_path,j,k,num_image = 30):
    accuracy = []

    for i in range(num_image):
        img = io.imread(os.path.join(test_path,"%d.png"%i),)
        img=Segment(img,j,k)
        io.imsave(os.path.join(test_path, "%d_process.png" % i), img)
        gt = io.imread(os.path.join(gt_path, "%d.png" % i), )
        img=img/255
        gt=gt/255
        r=gt-img
        r[r<0]=1
        acc=(262144-r.sum())/262144
        accuracy.append(acc)
    mean_acc = np.mean(accuracy)
    print("Accuracy of segmentation is",mean_acc)
    return mean_acc



