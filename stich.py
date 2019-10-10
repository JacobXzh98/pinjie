# 引入必要的库
#from imutils import paths
import numpy as np
import os
#import argparse
#import imutils
import cv2


# 代码命令行用法 python image_stitching_simple.py --images images/scottsdale --output output.png
# images/scottsdale是需要拼接的图片目录
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
    help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
    help="path to the output image")
args = vars(ap.parse_args())
"""
#imagePaths = sorted(list(paths.list_images(args["images"])))
data_path = "image/"
imagePaths = []
exts = ['jpg', 'png', 'jpeg', 'JPG']
if os.path.isfile(data_path):
    imagePaths.append(data_path)
else:
    for parent, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    imagePaths.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(imagePaths)))

images = []

# 加载要拼接的图片
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)

# 开始拼接
print("[INFO] Stitching images...")
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)


# 显示和保存拼接的图片
if status == 0:
    print("[INFO] Image stitching successful")
    cv2.imwrite("output.png", stitched)
    cv2.imshow("Stitched", stitched)
    cv2.waitKey(0)
else:
    print("[INFO] Image stitching failed ({})".format(status))
