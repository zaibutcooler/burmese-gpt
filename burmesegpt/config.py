import torch

class Config:
    def __init__(self) -> None:
        pass

config = Config()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
