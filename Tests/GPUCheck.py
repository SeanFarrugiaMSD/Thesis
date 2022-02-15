import cv2

print("CV2 Version: ", cv2.__version__)
print("Num CV2 GPUs Available: ", cv2.cuda.getCudaEnabledDeviceCount())

import keras

print("Keras Version: ", keras.__version__)

import tensorflow as tf

print("TF Version: ", tf.__version__)
print("Num TF GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

cv2.cuda.printCudaDeviceInfo(0)