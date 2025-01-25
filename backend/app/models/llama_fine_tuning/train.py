import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from transformers import TrainingArguments
from trl import SFTTrainer
import json

class QLoRAMemoryTrainer:
    def __init__(self, config_path='config.json'):
        # Load configuration
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Quantization configuration
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True
        )
        
        # Load base model in 4-bit quantization
        self.model = AutoModelForCausalLM.from_pretrained(
            self.config['base_model'],
            quantization_config=quantization_config,
            device_map="auto"
        )
        
        # Prepare model for training
        self.model = prepare_model_for_kbit_training(self.model)
        
        # LoRA configuration
        lora_config = LoraConfig(
            r=self.config['training_config'].get('lora_rank', 16),
            lora_alpha=self.config['training_config'].get('lora_alpha', 32),
            target_modules=["q_proj", "v_proj"],
            lora_dropout=0.1,
            bias="none",
            task_type="CAUSAL_LM"
        )
        
        # Apply LoRA
        self.model = get_peft_model(self.model, lora_config)
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.config['base_model'])
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def prepare_dataset(self, dataset_path):
        dataset = load_dataset('json', data_files=dataset_path)
        
        def tokenize_function(examples):
            return self.tokenizer(
                examples['text'], 
                truncation=True, 
                max_length=512, 
                padding='max_length'
            )
        
        return dataset.map(tokenize_function, batched=True)

    def train(self, dataset_path):
        # Prepare dataset
        train_dataset = self.prepare_dataset(dataset_path)
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir='./memory_model_qlora',
            num_train_epochs=self.config['training_config'].get('epochs', 3),
            per_device_train_batch_size=self.config['training_config'].get('batch_size', 4),
            learning_rate=self.config['training_config'].get('learning_rate', 2e-4),
            weight_decay=0.001,
            fp16=True,
            logging_dir='./logs'
        )
        
        # Trainer
        trainer = SFTTrainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            dataset_text_field='text'
        )
        
        # Start training
        trainer.train()
        trainer.save_model()

def main():
    # Ensure you have a dataset prepared
    trainer = QLoRAMemoryTrainer()
    trainer.train('memory_dataset.json')

if __name__ == "__main__":
    main()