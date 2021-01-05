import numpy as np
import matplotlib.pyplot as plt
import sys

LINES_NUMBER = 50
LINES_AMPLITUDE = 10
if len(sys.argv) != 3:
    print("Incorrect arguments")
    exit(1)
filename = sys.argv[1]
pathTo = sys.argv[2]
image = plt.imread(filename)
shape = image.shape
height = shape[0]
width = shape[1]
out_img = np.ones(shape)


def decel(x):
    return 1 - (x - 1) * (x - 1)


for line in range(0, LINES_NUMBER):
    l = 0
    y = int(line * height / LINES_NUMBER)
    for x in range(0, width):
        m = np.max(image[y, x])
        if m < 1:  # *.png
            m = 1 - m
        else:  # *.jpeg
            m = 1 - m / 255
        for s in range(0, LINES_AMPLITUDE + 1):
            out_img[min(y + int(np.sin(l * np.pi / 2.0) * LINES_AMPLITUDE * decel(m)), height - 1), x] = 0
            l += m / LINES_AMPLITUDE

plt.imshow(out_img)
plt.imsave('{}_ascii_{}.{}'.format(pathTo + "result", LINES_NUMBER, "jpg"), out_img)
plt.show()
