from PIL import Image
import os


u_dir = "./data/Gender/val/male"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+"/"+i)
    i = i.resize((64,96))
    i.save("./data/Gender2/val/male/"+str(x)+".jpg")
    print(x)


u_dir = "./data/Gender/val/female"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+"/"+i)
    i = i.resize((64,96))
    i.save("./data/Gender2/val/female/"+str(x)+".jpg")
