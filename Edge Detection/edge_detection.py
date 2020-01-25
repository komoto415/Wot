# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

vertical_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
horizontal_filter = [[-1, 0, -1], [-2, 0, 2], [-1, 0 , 1]]

img = plt.imread('C:/Users/Jeffrey/Documents/GitHub/Wot/Edge Detection/HongKongSkyline.jpg')
n, m, d = img.shape

edges_img = img.copy()
for row in range(3, n-2):
    for col in range(3, m-2):
        local_pixels = img[row - 1 : row + 2, col - 1 : col + 2, 0]

        vertical_transformed_pixels = vertical_filter * local_pixels
        vertical_score = vertical_transformed_pixels.sum() / 4

        horizontal_transformed_pixels = horizontal_filter * local_pixels
        horizontal_score = horizontal_transformed_pixels.sum() / 4

        edge_score = (vertical_score ** 2 + horizontal_score ** 2) ** .5
        edges_img[row, col] = [edge_score] * 3

edges_img = edges_img / edges_img.max()
plt.imshow(edges_img, cmap='gray')
plt.show()
# edges_img.savefig('edges.png')
