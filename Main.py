from numpy import array
from Data import pi
from PIL import Image

from cv2 import imshow, waitKey

pi = pi()

img = []

for x in range(100):
    img.append([])
    for y in range(100):
        img[x].append([])

        img[x][y] = [pi[int(f"{x}{y}")]*int(255/10) for _ in range(3)]

img = array(img).astype("uint8")

Image.fromarray(array(img)).save("pi.png")

while True:
    imshow("pi", img)
    waitKey(1)