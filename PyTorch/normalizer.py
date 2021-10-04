# after passing path to the training set, it returns mean, deviation across RGB channels

from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor
import numpy as np

def stats(root):
    train_ds = ImageFolder(root,ToTensor())
    
    r_arr =[]
    g_arr =[]
    b_arr =[]

    for image,label in train_ds:
        r_img,g_img,b_img = image
        r_arr.append(np.array(r_img))
        g_arr.append(np.array(g_img))
        b_arr.append(np.array(b_img))

    r_arr = np.array(r_arr)
    g_arr = np.array(g_arr)
    b_arr = np.array(b_arr)
    
    r_avg = r_arr.mean()
    g_avg = g_arr.mean()
    b_avg = b_arr.mean()

    mean_tup = (round(r_avg,4), round(g_avg,4), round(b_avg,4))
    print(mean_tup)
    
    r_dev = np.std(r_arr)
    g_dev = np.std(g_arr)
    b_dev = np.std(b_arr)

    dev_tup = (round(r_dev,4), round(g_dev,4), round(b_dev,4))
    print(dev_tup)
    
stats("./data/gender/train")
