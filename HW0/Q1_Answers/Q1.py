# بخش الف قسمت آخر سوال
import matplotlib.pyplot as plt

img = plt.imread('Q1.jpg')
plt.ion()
plt.imshow(img)
plt.show()
plt.pause(0.001)

while True:
    if plt.waitforbuttonpress():
        break