import numpy as np
import torch
from typing import List, Dict, Any

class MemoryUtils:
    @staticmethod
    def calculate_embedding_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors"""
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    @staticmethod
    def preprocess_text(text: str, max_length: int = 512) -> str:
        """Basic text preprocessing"""
        return text.lower().strip()[:max_length]
    
    @staticmethod
    def augment_training_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Simple data augmentation for memory improvement"""
        augmented_data = []
        for item in data:
            # Add variations to increase dataset diversity
            augmented_data.append(item)
            augmented_data.append({
                'input': item['input'].replace('Learn', 'Understand'),
                'target': item['target']
            })
        return augmented_data

def log_training_metrics(metrics: Dict[str, Any]):
    """Log training metrics for tracking"""
    print("Training Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value}")