import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as scipyd
from scipy.cluster import hierarchy
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def readImage(image_name):
    """
    Function to read a given image name
    :param image_name: A string representing the name of the image
    :return: The image represented in a numpy.ndarray type
    """
    return cv2.imread(str(image_name))

def showImage(image):
    """
    Function to display the image to the user. Closes the image window when user presses any key
    :param image: An image of type numpy.ndarray
    :return: None
    """
    image = imutils.resize(image, width=600)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def computeKeypoints(image):
    """
    Function to compute keypoints of the given image
    :param image: An image of type numpy.ndarray
    :return: A list of keypoints
    """
    sift = cv2.xfeatures2d.SIFT_create()
    return sift.detect(image)


def computeDescriptors(image, keypoints):
    """
    Function to compute the descriptors for each keypoint provided
    :param image: An image of type numpy.ndarray
    :param keypoints: A list of keypoints in the image
    :return: A tuple (keypoints, descriptors) whereby keypoints is a list of keypoints in an image and descriptors is a
             2d array consisiting of the shape (n, 128), whereby n is the number of keypoints. The number of columns is
             128 due to the use of the SIFT algorithm
    """
    sift = cv2.xfeatures2d.SIFT_create()
    kp, descriptors = sift.compute(image, keypoints)
    return kp, descriptors


def featureExtraction(image):
    """
    Function to extract the key features (keypoints and descriptors) of an image. Makes use of the computeKeypoints()
    and computeDescriptors() function.
    :param image: An image of type numpy.ndarray
    :return: A tuple (keypoints, descriptors)
    """
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kp = computeKeypoints(gray_img)
    kp, desc = computeDescriptors(gray_img, kp)
    return kp, desc


def featureMatching(keypoints, descriptors):
    """
    Function to perform feature matching. Makes use of brute force matcher.
    :param keypoints: A list of keypoints
    :param descriptors: A 2-dimensional array of shape (n, 128), whereby n is the number of keypoints
    :return: A tuple (a, b) where a and b represents a 2-d array of keypoints
    """
    norm = cv2.NORM_L2  # cv2.NORM_L2 is used since we are using the SIFT algorithm
    k = 10  # number of closest match we want to find for each keypoint

    matcher = cv2.BFMatcher(norm)
    matches = matcher.knnMatch(descriptors, descriptors, k)

    # Apply ratio test to get good matches
    ratio = 0.5
    good_matches_1 = []
    good_matches_2 = []

    for match in matches:
        k = 1   # Ignore the first element in the matches array (distance to itself is always 0)

        while match[k].distance < ratio * match[k + 1].distance:  # d_i/d_(i+1) < T (threshold)
            k += 1

        for i in range(1, k):
            # Compute pairwise distance between the two points to ensure they are spatially separated
            if hierarchy.distance.pdist(np.array([keypoints[match[i].queryIdx].pt, keypoints[match[i].trainIdx].pt])) > 10:
                good_matches_1.append(keypoints[match[i].queryIdx])
                good_matches_2.append(keypoints[match[i].trainIdx])

    points_1 = []   # Shape (n, 2)
    for i in range(np.shape(good_matches_1)[0]):
        points_1.append(good_matches_1[i].pt)

    points_2 = []  # Shape (n, 2)
    for i in range(np.shape(good_matches_2)[0]):
        points_2.append(good_matches_2[i].pt)

    if len(points_1) > 0 or len(points_2) > 0:
        # Combine 2d array points_1 (n, 2) and points_2 (n, 2) by their column -> (n, 4)
        p = np.hstack((points_1, points_2))

        # Remove any duplicated points
        unique_p = np.unique(p, axis=0)

        # Get back normal shape: (n, 4) -> (n, 2) and (n, 2)
        return np.float32(unique_p[:, 0:2]), np.float32(unique_p[:, 2:4])

    else:
        return None, None


def dbscan(points1, points2):   # Density based spatial clustering
    points = np.vstack((points1, points2))
    scaled_hist = StandardScaler().fit_transform(points)

    dist_matrix = scipyd.cdist(scaled_hist, scaled_hist, "cosine")
    eps_value = 0.45 * dist_matrix.max()

    db = DBSCAN(eps=eps_value, min_samples=10).fit(scaled_hist)
    clusters = db.labels_

    outliers_idx = np.where(clusters == -1)
    outliers_idx = outliers_idx[::-1]

    for i in range(len(outliers_idx)):
        points = np.delete(points, outliers_idx[i], axis=0)

    clusters = clusters[clusters != -1]

    n = int(np.shape(points)[0]/2)
    points1 = points[:n]
    points2 = points[n:]
    return clusters, points1, points2


def plotImage(img, p1, p2, C):
    plt.imshow(img)
    plt.axis('off')

    colors = C[:np.shape(p1)[0]]
    plt.scatter(p1[:, 0], p1[:, 1], c=colors, s=30)

    for item in zip(p1, p2):
        x1 = item[0][0]
        y1 = item[0][1]

        x2 = item[1][0]
        y2 = item[1][1]

        plt.plot([x1, x2],[y1, y2], 'c')

    plt.savefig("results.png")

    plt.clf()


def detect_copy_move(image):
    kp, desc = featureExtraction(image)
    p1, p2 = featureMatching(kp, desc)
    # showImage(image)

    if p1 is None:
        # print("No tampering was found")
        return False, image

    clusters, p1, p2 = dbscan(p1, p2)

    if len(clusters) == 0:
        # print("No tampering was found")
        return False,  image

    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plotImage(image, p1, p2, clusters)
    return True, image


if __name__ == "__main__":
    img = readImage("sample.png")
    detect_copy_move(img)
