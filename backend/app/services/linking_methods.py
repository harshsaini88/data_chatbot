from models.models import MemoryLinkingModel
from typing import List, Dict

class MemoryLinkingService:
    def __init__(self):
        self.memory_model = MemoryLinkingModel()
        self.interaction_history = []

    def retrieve_context(self, query: str, top_k: int = 3) -> List[Dict]:
        # Use memory linking model to retrieve relevant memories
        related_memories = self.memory_model.retrieve_related_memories(query, top_k)
        return related_memories

    def store_interaction(self, user_message: str, ai_response: str):
        # Store interaction for future learning and context
        interaction = {
            'user_message': user_message,
            'ai_response': ai_response,
            'timestamp': datetime.now()
        }
        self.interaction_history.append(interaction)
        
        # Optionally store in memory model for future reference
        self.memory_model.store_memory(
            text=f"User: {user_message}\nAI: {ai_response}",
            metadata={'type': 'interaction'}
        )