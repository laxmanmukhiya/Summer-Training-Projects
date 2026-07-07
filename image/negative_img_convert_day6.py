import numpy as np 
from PIL import Image
import matplotlib.pyplot as pl 

img = Image.open('butterfly.jpg')
img = np.array(img)

#create a negative image

negative_img = 255 - img 
negative_img = np.clip(negative_img,0,255)
pl.imshow(negative_img)
pl.axis('off')
pl.show()