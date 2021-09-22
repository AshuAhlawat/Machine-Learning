import cv2
import os
# import sys 

# sys.path.append('/usr/local/lib/python3.9/site-packages')

frame = cv2.imread("./data/fashion/gans_data/fake_images_1.png")

height, width, layers = frame.shape
  
video = cv2.VideoWriter("./data/FashionGANS.avi", 0, 1, (width, height)) 

images = os.listdir("./data/fashion/gans_data")

for image in images: 
   video.write(cv2.imread("./data/fashion/gans_data/"+image)) 
      
cv2.destroyAllWindows() 
video.release()