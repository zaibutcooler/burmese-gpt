# sample the texts
from burmesegpt import BurmeseGpt

gpt = BurmeseGpt()

model_name = ''

gpt.load_pretrained(model_name)

gpt.sample()
