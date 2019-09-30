import cv2
import numpy as np

def readImage(image_name):
    img = cv2.imread(image_name)
    return img

def showImage(image):
    cv2.imshow('image',img)
    cv2.waitKey(0)

def computeKeypoints(image):    #Extract keypoints of the given image
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(image)
    return kp

def computeDescriptors(image, keypoints):   #Compute descriptor for the keypoints provided
    sift = cv2.xfeatures2d.SIFT_create()
    kp, descriptors = sift.compute(image, keypoints)
    return kp, descriptors

def featureExtraction(image):
    #Extract features (keypoints and descriptors) from the given image
    #Make use of the computeKeypoints() and computeDescriptors() function
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kp = computeKeypoints(gray_img)
    kp, desc = computeDescriptors(gray_img, kp)
    return kp, desc
