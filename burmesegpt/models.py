import torch 
from torch import nn
from huggingface_hub import PyTorchModelHubMixin

class SelfAttention(nn.Module,PyTorchModelHubMixin):
    def __init__(self):
        pass

    def forward(self):
        pass

class MLP(nn.Module,PyTorchModelHubMixin):
    def __init__(self):
        pass

    def forward(self):
        pass

class GPT(nn.Module,PyTorchModelHubMixin):
    def __init__(self):
        super().__init__()

    def forward(self):
        pass