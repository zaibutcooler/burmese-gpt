import torch
from .models import SelfAttention,MLP,GPT
from .tokenizer import Tokenizer
from .config import Config
from .data_prep import Data

device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = Tokenizer()

class BurmeseGpt:
    def __init__(self,tk=tokenizer):
        self.attention = SelfAttention().to(device)
        self.mlp = MLP().to(device)
        self.config = Config().to(device)
        self.train_data = Data().to(device)
        self.tokenizer = tk

    def train(self):
        pass

    def generate(self,entry=''):
        result = None
        
        return result

    def save_trained(self):
        pass

    def load_pretrained(self,name=""):
        pass

    