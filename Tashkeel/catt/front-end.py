from flask import Flask, render_template, request
import torch
from ed_pl import TashkeelModel
from tashkeel_tokenizer import TashkeelTokenizer
from utils import remove_non_arabic

app = Flask(__name__)

# Load the model once when the app starts
tokenizer = TashkeelTokenizer()
ckpt_path = '/Users/faisalsmac/Desktop/models/best_ed_mlm_ns_epoch_178.pt'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
max_seq_len = 1024
model = TashkeelModel(tokenizer, max_seq_len=max_seq_len, n_layers=3, learnable_pos_emb=False)
model.load_state_dict(torch.load(ckpt_path, map_location=device))
model.eval().to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    user_input = request.form['text_input']
    x = [remove_non_arabic(user_input)]
    batch_size = 16
    verbose = True
    x_tashkeel = model.do_tashkeel_batch(x, batch_size, verbose)
    
    # Return the diacritized text to the webpage
    return render_template('index.html', original_text=user_input, tashkeel_text=x_tashkeel[0])

if __name__ == '__main__':
    app.run(debug=True)
