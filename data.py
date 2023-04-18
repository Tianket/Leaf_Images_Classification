import pathlib
import random
import torchvision.transforms as transforms
from torch.utils.data import Dataset

transformations = transforms.Compose([
        transforms.Resize((256,256)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(30),
        transforms.ToTensor(),
        transforms.Normalize((0.5),(0.5))
])

class Dataset(Dataset):
    def __init__(self, imgLabel ,whole_datasets, transform=None):
        super().__init__()
        self.imgLabel=imgLabel
        self.whole_datasets=whole_datasets
        self.transform = transform

    def __len__(self):
        return len(self.whole_datasets)

    def __getitem__(self, i):
        imagePath = self.whole_datasets[i]
        Img = Image.open(imagePath)
        labelName = imagePath.split('/')[-2]
        label = self.imgLabel[labelName]
        if self.transform is not None:
            Img = self.transform(Img)
        return (Img, label)