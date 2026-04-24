#image content

#pillow 
from PIL import Image
image=Image.open("python-logo.png")
image.show()


#opencv
import cv2
photo=cv2.imread("python-logo.png")
cv2.imshow("Image",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()


#matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread("python-logo.png")
plt.show(img)
plt.axis("off")
plt.show()


#
import cv2
img = cv2.imread("python-logo.png")
if img is None:
    print("Image not found")
    exit()

# Prep grayscale & blur
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
g = cv2.medianBlur(g, 5)

# Edges
e = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                          cv2.THRESH_BINARY, 9, 9)

# Smooth color
c = cv2.bilateralFilter(img, 9, 250, 250)

# Combine
cartoon = cv2.bitwise_and(c, c, mask=e)

cv2.imshow("Cartoon", cartoon)
cv2.imwrite("cartoon_output.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()




