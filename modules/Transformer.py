from transformers import AutoModelForCausalLM, AutoTokenizer

class Transformer:
    def __init__(self):
        self.model_name = "microsoft/DialoGPT-medium"
        # self.model_name = "EleutherAI/gpt-neo-1.3B"
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name, pad_token_id=50256)
        # self.model = AutoModelForCausalLM.from_pretrained("gpt2", pad_token_id=50256)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
    
    def askTransformer(self, text):
        input_ids = self.tokenizer.encode(text + self.tokenizer.eos_token, return_tensors='pt')
        response = self.model.generate(input_ids=input_ids, max_length=150, do_sample=True)
        return (self.tokenizer.decode(response[0], skip_special_tokens=True))[(len(text)-1):]