import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math

class Image():
   
    def __init__(self, file):
        self.x = 0
        self.y = 0
        self.colorB = 0
        self.colorG = 0
        self.colorR = 0
        self.label = 'image'

        self.editR = 0
        self.editG = 0
        self.editB = 0

        vid = cv.VideoCapture(file)
        ret, self.img = vid.read()

    def mouseMove(self, event, x, y, flags, params):
        if event == cv.EVENT_MOUSEMOVE:
            self.x = x
            self.y = y
            self.colorB = self.img[y, x, 0]
            self.colorG = self.img[y, x, 1]
            self.colorR = self.img[y, x, 2]

        if event == cv.EVENT_LBUTTONDOWN:
            self.img[y, x] = [self.editB, self.editG, self.editR]
            cv.imshow(self.label, self.img)

    def set_callback(self):
        cv.setMouseCallback(self.label, self.mouseMove)

    def show_image(self):
        cv.imshow(self.label, self.img)

    def upscale(self, scale):
        width = self.img.shape[1] * scale
        height = self.img.shape[0] * scale
        dim = (width, height)
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_NEAREST)
        cv.imshow(self.label, self.img)

    def downscale(self, scale):
        width = int(self.img.shape[1] / scale)
        height = int(self.img.shape[0] / scale)
        dim = (width, height)
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_NEAREST)
        cv.imshow(self.label, self.img)

    def save(self, name):
        cv.imwrite(name, self.img)

    def histogram(self):
        color = ('b', 'g', 'r')
        med = 0.0
        for i, col in enumerate(color):
            histr = cv.calcHist([self.img], [i], None, [256], [0,256])
            med += histr
            plt.plot(histr, color = col)
            plt.xlim([0,256])

        med = med/3
        plt.plot(med, color = 'black')
        plt.show()

    def equalize(self):
        ycrcb = cv.cvtColor(self.img, cv.COLOR_BGR2YCR_CB)
        channels = cv.split(ycrcb)
        cv.equalizeHist(channels[0], channels[0])
        cv.merge(channels, ycrcb)
        cv.cvtColor(ycrcb, cv.COLOR_YCR_CB2BGR, self.img)
        cv.imshow(self.label, self.img)

    def stretch(self, a, b):
        self.img = cv.normalize(self.img, self.img, a, b, cv.NORM_MINMAX)
        lab = cv.cvtColor(self.img, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit= 3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl, a, b))
        self.img = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        cv.imshow(self.label, self.img)

    def brightness(self, mode):
        
        new_image = np.zeros(self.img.shape, self.img.dtype)
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                for k in range(self.img.shape[2]):
                    if mode == 1:
                        self.img[i, j, k] = np.clip((self.img[i, j, k]/255)**0.5*255, 0, 255)
                    else:
                        self.img[i, j, k] = np.clip((self.img[i, j, k]/255)**2*255, 0, 255)
        cv.imshow(self.label, self.img)

    def manual_bin(self, threshold):
        grayscale = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        ret, self.img = cv.threshold(grayscale, threshold, 255, cv.THRESH_BINARY)
        cv.imshow(self.label, self.img)

    def auto_bin(self):
        grayscale = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        ret, self.img = cv.threshold(grayscale, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
        cv.imshow(self.label, self.img)

    def local_bin(self, window, k):
        grayscale = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.img = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
            cv.THRESH_BINARY, window, k)
        cv.imshow(self.label, self.img)