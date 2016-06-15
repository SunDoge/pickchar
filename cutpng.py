import cv2
import os
import numpy as np
import time
import random
import shutil
import sys

import separator

PNG_DIR = './cookedpng/'
CUT_PNG_DIR = './finished/'
SEPARATED_PNG_DIR = './char/'

files = os.listdir(PNG_DIR)
i = 0
cv2.namedWindow('captcha', cv2.WINDOW_NORMAL)
cv2.namedWindow('char', cv2.WINDOW_NORMAL)


def getChar(char_img):
    cv2.imshow('char', char_img)
    key = cv2.waitKey(0)
    if (key > 47 and key < 58) or (key > 96 and key < 123):
        key = chr(key)
        putImgToFolder(key, char_img)
    elif key == 27:
        return 2
    elif key == 32:
        return 0
    else:
        getChar(char_img)


def putImgToFolder(key, img):
    if not(os.path.exists(SEPARATED_PNG_DIR + key)):
        os.mkdir(SEPARATED_PNG_DIR + key)

    cv2.imwrite(SEPARATED_PNG_DIR + key + '/%s%s.png' %
                (int(time.time()), random.randint(10, 99)), img)
    return 0


while (True):
    file = files[i]
    img = cv2.imread(PNG_DIR + file)
    cv2.imshow('captcha', img)
    char_1, char_2, char_3, char_4 = separator.separate(img)

    if getChar(char_1) == 2:
        break

    if getChar(char_2) == 2:
        break

    if getChar(char_3) == 2:
        break

    if getChar(char_4) == 2:
        break

    shutil.move(PNG_DIR + file, CUT_PNG_DIR)
    i += 1


cv2.destroyAllWindows()
