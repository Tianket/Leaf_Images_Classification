import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms as transforms
import torchvision.datasets as datasets

import pandas as pd
import numpy as np

import pathlib
import os
import copy
import random
import time

#from net import Net

data_dir=pathlib.Path("./datasets")
print(data_dir)

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

'''
    'apta': [list(data_dir.glob('Apta/*'))[:1][0]] ,
    'indian_rubber_tree': [list(data_dir.glob('Indian Rubber Tree/*'))[:1][0]] ,
    'karanj': [list(data_dir.glob('Karanj/*'))[:1][0]] ,
    'kashid': [list(data_dir.glob('Kashid/*'))[:1][0]] ,
    'nilgiri': [list(data_dir.glob('Nilgiri/*'))[:1][0]],
    'pimpal': [list(data_dir.glob('Pimpal/*'))[:1][0]],
    'sita_ashok': [list(data_dir.glob('Sita Ashok/*'))[:1][0]],
    'sonmohar': [list(data_dir.glob('Sonmohar/*'))[:1][0]],
    'vad': [list(data_dir.glob('Vad/*'))[:1][0]],
    'vilayati_chinch': [list(data_dir.glob('Vilayati Chinch/*'))[:1][0]]
    '''