import torch
from huggingface_hub import login

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

    def save_pretrained(self, name="burmese-gpt"):
        print("Uploading model...")
        self.model.save_pretrained(name)
        print(f"Model saved locally as '{name}'")
        self.model.push_to_hub(name)
        print(f"Model '{name}' uploaded to the Hugging Face Model Hub")

    def load_pretrained(self, model_id="zaibutcooler/burmese-gpt"):
        print("Loading model...")
        model = model.from_pretrained(model_id)
        print(f"Model '{model_id}' loaded successfully")
        return model
    
    def huggingface_login(self,token):
        login(token)
    
    def pretrain(self):
        pass

    def fine_tune(self):
        pass

    def generate(self,entry=''):
        result = None
        
        return result