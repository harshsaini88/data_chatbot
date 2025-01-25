import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from datasets import Dataset
import json

def load_config(config_path='config.json'):
    with open(config_path, 'r') as f:
        return json.load(f)

class MemoryImprovementTrainer:
    def __init__(self, config):
        self.config = config
        self.model = LlamaForCausalLM.from_pretrained(config['base_model'])
        self.tokenizer = LlamaTokenizer.from_pretrained(config['base_model'])
        
    def prepare_dataset(self, training_data):
        """Prepare and tokenize dataset for fine-tuning"""
        dataset = Dataset.from_dict({
            'input_text': [item['input'] for item in training_data],
            'target_text': [item['target'] for item in training_data]
        })
        
        def tokenize_function(examples):
            model_inputs = self.tokenizer(
                examples['input_text'], 
                max_length=self.config['training_config']['max_sequence_length'], 
                truncation=True
            )
            with self.tokenizer.as_target_tokenizer():
                labels = self.tokenizer(
                    examples['target_text'], 
                    max_length=self.config['training_config']['max_sequence_length'], 
                    truncation=True
                )
            model_inputs["labels"] = labels["input_ids"]
            return model_inputs
        
        return dataset.map(tokenize_function, batched=True)
    
    def train(self, training_data):
        processed_dataset = self.prepare_dataset(training_data)
        
        training_args = TrainingArguments(
            output_dir='./memory_model_checkpoints',
            **self.config['training_config']
        )
        
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=processed_dataset
        )
        
        trainer.train()
        trainer.save_model()

def main():
    config = load_config()
    trainer = MemoryImprovementTrainer(config)
    
    # Example training data (replace with your actual data)
    training_data = [
        {'input': 'Learn about machine learning', 'target': 'Machine learning is...'}
    ]
    
    trainer.train(training_data)

if __name__ == "__main__":
    main()