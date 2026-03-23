import cv2 as cv
import numpy as np

kernel_size = 9
sigma_color = 35
sigma_space = 50

n_iterations = 10
threshold1 = 200
threshold2 = 2500
aperture_size = 5

img_name = 'cosplay2'
# Load the image
img = cv.imread(img_name +'.jpg')
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Apply gausian blur to reduce noise
gray = cv.GaussianBlur(gray, (3,3), 0)
# Detect edges using adaptive thresholding
edges = cv.Canny(gray, threshold1, threshold2, apertureSize= aperture_size)

# Convert the image to color
color = img.copy()
for itr in range(n_iterations):
    color = cv.bilateralFilter(color, kernel_size, sigma_color, sigma_space)

kernel = np.ones((3,3), dtype= np.uint8)
#edges = cv.dilate(edges, kernel, iterations=1)

edges_inv = cv.bitwise_not(edges)
# Combine the color image with the edges mask
cartoon = cv.bitwise_and(color, color, mask = edges_inv)
# Display the cartoon image
cv.imshow("Original", img)
cv.imshow("Cartoon Rendering", cartoon)
cv.waitKey(0)
cv.destroyAllWindows()
