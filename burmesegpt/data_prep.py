# to preps data
from datasets import load_dataset
from torch.utils.data import Dataset


class Data(Dataset):
    def __init__(self):
        super().__init__()
        self.texts = None
        self.data

    def __len__(self):
        return None
    
    def __getitem__(self, index):
        return self.trainset[index]
    
    
    