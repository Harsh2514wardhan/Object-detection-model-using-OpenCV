# This code is a object detection code where we are using pillars as our objects and multiple objects will be identified by different colors

import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "Pillar_Images\Pillar_img_2.jpeg" #
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found. Please check the file path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

edges = cv2.Canny(thresh, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

colored_pillars = image.copy()

for i, contour in enumerate(contours):
    color = [int(c) for c in np.random.randint(0, 255, 3)]
    cv2.drawContours(colored_pillars, [contour], -1, color, thickness=-1)

output_path = "colored_pillars.jpg"
cv2.imwrite(output_path, colored_pillars)
print(f"Output image saved as {output_path}")

cv2.imshow("Original Image", image)
cv2.imshow("Pillars Detected with Colors", colored_pillars)

cv2.waitKey(0)
cv2.destroyAllWindows()