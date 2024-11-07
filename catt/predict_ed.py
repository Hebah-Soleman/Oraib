
import torch
from ed_pl import TashkeelModel
from tashkeel_tokenizer import TashkeelTokenizer
from utils import remove_non_arabic

tokenizer = TashkeelTokenizer()
ckpt_path = '/Users/faisalsmac/Desktop/models/best_ed_mlm_ns_epoch_178.pt'

print('ckpt_path is:', ckpt_path)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('device:', device)

max_seq_len = 1024
print('Creating Model...')
model = TashkeelModel(tokenizer, max_seq_len=max_seq_len, n_layers=3, learnable_pos_emb=False)

model.load_state_dict(torch.load(ckpt_path, map_location=device))
model.eval().to(device)

# Prompt user to enter the text for tashkeel
user_input = input("Enter the undiacritized Arabic text: ")

# Process the user input
x = [remove_non_arabic(i) for i in user_input]
batch_size = 16
verbose = True
x_tashkeel = model.do_tashkeel_batch(x, batch_size, verbose)

print(x)
print('-'*85)
print(x_tashkeel)
