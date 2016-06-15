import cv2
import numpy as np


def stdChar(array, center):

    canvas = np.zeros((27, 27), np.uint8)
    for x, y in array:
        xx = x - center[0] + 13
        yy = y - center[1] + 13
        if xx > -1 and xx < 27 and yy > -1 and yy < 27:
            canvas[xx][yy] = 255

    return canvas


def separate(img):

    samples = []
    row, col = img.shape[:2]

    for i in range(row):
        for j in range(col):
            if (img[i, j] == [153, 0, 0]).all():
                samples.append([i, j])

    Z = np.float32(samples)

    criteria = (cv2.TERM_CRITERIA_EPS +
                cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(
        Z, 4, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.int8(center)
    Z = np.int8(Z)
    char = []
    for k in np.argsort(center[:, 1]):
        char.append(stdChar(Z[label.ravel() == k], center[k]))

    return char[0], char[1], char[2], char[3]
