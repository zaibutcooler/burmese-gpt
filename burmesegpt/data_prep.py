# to preps data
from datasets import load_dataset
from torch.utils.data import Dataset

dataset = load_dataset("")

class Data(Dataset):
    def __init__(self) -> None:
        super().__init__()

    def forward(self,x):
        pass
    