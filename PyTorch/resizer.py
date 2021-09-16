from PIL import Image
import os


u_dir = "./data/hymenoptera/train/ants/"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+i)
    i = i.resize((300,300))
    i.save("./data/hymenoptera2/train/ants/"+str(x)+".png")



u_dir = "./data/hymenoptera/train/bees/"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+i)
    i = i.resize((300,300))
    i.save("./data/hymenoptera2/train/bees/"+str(x)+".png")