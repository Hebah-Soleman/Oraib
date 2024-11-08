import torch
import json
from transformers import AutoTokenizer, AutoModelForTokenClassification
from ibm_watsonx_ai.foundation_models import Model

class TokenClassificationTester:
    def __init__(self, model_path, model_id, project_id, api_url, api_key):
        self.model_path = model_path
        self.model_id = model_id
        self.project_id = project_id
        self.credentials = {"url": api_url, "apikey": api_key}
        self.parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "repetition_penalty": 1
        }
        self.model = Model(
            model_id=self.model_id,
            params=self.parameters,
            credentials=self.credentials,
            project_id=self.project_id
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.arabert_model = AutoModelForTokenClassification.from_pretrained(model_path)
        self.label2id, self.id2label = self.load_label_mappings()

    def load_label_mappings(self):
        with open(f"{self.model_path}/label_mappings.json", "r", encoding="utf-8") as f:
            label_mappings = json.load(f)
        return label_mappings["label2id"], label_mappings["id2label"]

    def predict_labels(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", is_split_into_words=False)
        with torch.no_grad():
            outputs = self.arabert_model(**inputs).logits
        predicted_ids = torch.argmax(outputs, dim=2).squeeze().tolist()
        predicted_labels = [self.id2label[str(id)] for id in predicted_ids]
        tokens = self.tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze().tolist())
        return tokens, predicted_labels

    @staticmethod
    def tokens_to_sentence_with_hashes(tokens):
        tokens = tokens[1:-1]  # Remove special tokens (e.g., [CLS], [SEP])
        sentence = " ".join(tokens)
        return sentence.strip()

    def detect_errors(self, tokens):
        input_text = self.tokens_to_sentence_with_hashes(tokens)
        detected_errors = [word for word in input_text.split() if "##" in word]
        return detected_errors, input_text

    def generate_prompt(self, input_text, detected_errors):
        prompt = (
            f"<s> [INST] في النص التالي:{input_text}. "
            f"قم بتعديل الكلمات التي تحتوي على # وهي:{detected_errors} "
            "وأرجع النص بعد التعديل مرة واحدة فقط [/INST]"
        )
        return prompt

    def generate_correction(self, prompt):
        # This method should call the model to generate corrected text (mock-up for demonstration)
        # For instance:
        corrected_text = self.model.generate_text(prompt) # Replace with actual model generation call
        return corrected_text

    def run_test(self, test_sentence):
        tokens, predicted_labels = self.predict_labels(test_sentence)
        detected_errors, input_text = self.detect_errors(tokens)
        
        if detected_errors:
            prompt = self.generate_prompt(input_text, detected_errors)
            corrected_text = self.generate_correction(prompt)
            return corrected_text
        else:
            return "No errors detected."
