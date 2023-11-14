# utils 

def get_stats():
    pass

def merge():
    pass

def upload_model(model, name="", token=""):
    print("Uploading model...")
    model.save_pretrained(name)
    print(f"Model saved locally as '{name}'")
    model.push_to_hub(name)
    print(f"Model '{name}' uploaded to the Hugging Face Model Hub")

def save_model(model, name="gpt"):
    print("Saving model...")
    model.save_pretrained(name)
    print(f"Model saved locally as '{name}'")

def load_model(model_name):
    print("Loading model...")
    model = model.from_pretrained(model_name)
    print(f"Model '{model_name}' loaded successfully")
    return model