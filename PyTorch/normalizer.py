# after passing path to the training set, it returns mean, deviation across RGB channels

import torch
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor
import numpy as np

def stats(root):
    train_ds = ImageFolder(root,ToTensor())
    size = len(train_ds)

    r_mean= 0
    g_mean= 0
    b_mean= 0
    r_dev= 0
    g_dev= 0
    b_dev= 0

    tenth = size/10
    x = 0

    for image,label in train_ds:
        x+=1
        r_img,g_img,b_img = image
        
        r_mean += r_img.mean().item()
        g_mean += g_img.mean().item()
        b_mean += b_img.mean().item()

        r_dev += r_img.std().item()
        g_dev += g_img.std().item()
        b_dev += b_img.std().item()

        if x%tenth == 0:
            print(int(x*100/size),"% done")


    r_avg = r_mean/size
    g_avg = g_mean/size
    b_avg = b_mean/size


    mean_tup = (round(r_avg,6), round(g_avg,6), round(b_avg,6))
    print(mean_tup)
    
    r_dev = r_dev/size
    g_dev = g_dev/size
    b_dev = b_dev/size

    dev_tup = (round(r_dev,6), round(g_dev,6), round(b_dev,6))
    print(dev_tup)
    
stats("./data/human/train")
