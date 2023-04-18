import torch
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision.datasets as datasets
from torch.utils.data import DataLoader

import pandas as pd
import numpy as np

import pathlib
import os
import copy
import random
import time

#from net import Net
from data import Dataset
from train_and_test import test,train

################# Trash can #################

lr=
batch_size=64
epoch=10
folder="datasets"
imgLabel = {
    'Apta' : 0,
    'Indian Rubber Tree' : 1,
    'Karanj' : 2,
    'Kashid' : 3,
    'Nilgiri': 4,
    'Pimpal': 5,
    'Sita Ashok': 6,
    'Sonmohar': 7,
    'Vad': 8,
    'Vilayati Chinch': 9
}

################# Data into list #################

whole_datasets=[]

for categories in imgClass:
    each_data_dir=pathlib.Path(folder,categories)
    for each_image in each_data_dir.glob("*.jpg"):
        whole_datasets.append(each_image)

random.shuffle(whole_datasets)


################# Data into list #################

train_part=whole_datasets[:2500]
test_part=whole_datasets[2500:]

train_data=Dataset(imgLabel,train_part)
test_data=Dataset(imgLabel,test_part)

train_dataloader=DataLoader(train_data,batch_size,shuffle=True)
test_dataloader=DataLoader(test_data,batch_size,shuffle=True)

