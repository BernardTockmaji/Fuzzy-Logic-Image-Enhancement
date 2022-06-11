import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def enhance_image(fileName):
    # Reading the image
    rgb = cv.imread(fileName, cv.IMREAD_UNCHANGED)
    cv.imshow('RGB', rgb)

    # Converting the image to HSV
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)

    # Calculating the histogram from the V component
    hist = cv.calcHist([hsv], [2], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # Initializing K as 128
    K = 128
    print('K = ' + str(K))

    # Initializing E as 255
    E = 255
    print('E = ' + str(E))

    # Calculating M using equation 1
    M = 0
    hist_list = [j[0] for j in hist]
    numerator = 0
    denominator = sum(hist_list)

    for i, j in zip(hist_list, range(0, 256)):
        numerator = numerator + i * j
    M = int(numerator / denominator)
    print('M = ' + str(M))

    # Divide pixel values into 2 classes C1 and C2
    C1 = range(0, M)
    print('Class 1 = ' + str(C1))

    C2 = range(M, 256)
    print('Class 2 = ' + str(C2))

    # Calculate fuzzy membership values muC1 and muC2 using equations 2 and 4
    # Calculate the enhanced intensity values using equations 3 and 5
    def enhance(X):
        if X in C1:
            # Equation 2
            muC1 = (1 - (M - X)) / M
            # Equation 3
            X = X + (muC1 * K)
            if X < 0:
                X = 0
        elif X in C2:
            # Equation 4
            muC2 = (E - X) / (E - M)
            # Equation 5
            X = (X * muC2) + (E - (muC2 * K)) - K
            if X > 255:
                X = 255
        return X

    # Modify the pixel values' V component
    # Combine H and S components with the enhanced V component
    enhanced_V = np.vectorize(enhance)(hsv[:, :, 2])
    enhanced_hsv = hsv
    enhanced_hsv[:, :, 2] = enhanced_V

    # Convert the HSV image to RGB for the enhanced RGB image
    enhanced_rgb = cv.cvtColor(enhanced_hsv, cv.COLOR_HSV2RGB)
    cv.imshow('Enhanced RGB', enhanced_rgb)

    key = cv.waitKey(0)
    if key == 'q':
        cv.destroyAllWindows()
