#import libraries
import numpy as np 
from PIL import Image
import matplotlib.pyplot as pl 

#open image
img = Image.open('download.jpg')

#convert image into array
img  = np.array(img)
 

img [:,:,0] = np.clip(img[:,:,0] + 10,100,200)

pl.imshow(img)
pl.axis('off')
pl.show()

