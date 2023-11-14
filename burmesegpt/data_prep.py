# to preps data
from datasets import load_dataset
from torch.utils.data import Dataset

dataset = load_dataset("")

class Data(Dataset):
    def __init__(self,trainset):
        super().__init__()
        self.trainset = trainset

    def __len__(self):
        return None
    
    def __getitem__(self, index):
        return self.trainset[index]
    
    
    