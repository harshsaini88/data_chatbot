import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig

class MemoryInference:
    def __init__(self, base_model_path, adapter_path):
        # Load base model configuration
        config = PeftConfig.from_pretrained(adapter_path)
        
        # Load base model
        self.model = AutoModelForCausalLM.from_pretrained(
            base_model_path,
            load_in_4bit=True,
            quantization_config={
                'load_in_4bit': True,
                'bnb_4bit_compute_dtype': torch.float16
            }
        )
        
        # Load LoRA adapter
        self.model = PeftModel.from_pretrained(self.model, adapter_path)
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_response(self, prompt, max_tokens=150):
        # Prepare inputs
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Generate response
        outputs = self.model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_length=max_tokens,
            num_return_sequences=1,
            temperature=0.7
        )
        
        # Decode and return response
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)