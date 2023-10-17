
from scipy.ndimage import gaussian_filter as gf
import matplotlib.pyplot as plt

image_read = plt.imread("Alvin_Data_Science/images/alvin.jpg")
blur_image = gf(image_read, 2)
prefix = 'blurred'

plt.subplot(121)
plt.imshow(image_read)
plt.title('original image')

plt.subplot(122)
plt.imshow(blur_image)
plt.title('blurred image')


blur_image_name = prefix + '_img.jpg'
plt.imsave(blur_image_name, blur_image)
plt.show()