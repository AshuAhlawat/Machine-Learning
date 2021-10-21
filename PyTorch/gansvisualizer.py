import cv2
import os
from PIL import Image

ROOT = "./data/cats/gans_data/"
images = os.listdir(ROOT)


#renamer
num = 0
for i in range(len(images)):
   name = "epoch_"+str(i)+".png"

   if name in images:
      print(name)
      num+=1
      x= Image.open(ROOT + name)
      x.resize((600,600))
      x.save("./data/cats/new_data/epoch_"+str(num)+".png")

#setting frame size
frame = cv2.imread(ROOT + "/epoch_1.png")
height, width, layers = frame.shape

#insering frames into video
video = cv2.VideoWriter("./data/CatGAN.avi", 0, 1, (width, height)) 
for i in range(len(images)): 
   video.write(cv2.imread(ROOT+"epoch_"+str(i)+".png")) 
      
cv2.destroyAllWindows()
video.release()