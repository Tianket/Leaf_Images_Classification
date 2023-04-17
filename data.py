import pathlib
import random


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

folder="datasets"
whole_datasets={}

for categories in imgLabel:
    each_data_dir=pathlib.Path(folder,categories)
    for each_image in each_data_dir.glob("*.jpg"):
        whole_datasets[each_image]=imgLabel[categories]

transformations = transforms.Compose([
        transforms.Resize((256,256)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(30),
        transforms.ToTensor(),
        transforms.Normalize((0.5),(0.5))
])


class Dataset(Dataset):
    def __init__(self, whole_datasets, transform=None):
        super().__init__()

        self.whole_datasets=whole_datasets
        self.transform = transform

    def __len__(self):
        return len(self.base_dir)

    def __getitem__(self, i):
        imagePath = self.base_dir[i]
        Img = Image.open(imagePath)
        labelName = imagePath.split('/')[-2]
        label = self.df_labels[labelName]

        if self.transform is not None:
            Img = self.transform(Img)
        return (Img, label)

