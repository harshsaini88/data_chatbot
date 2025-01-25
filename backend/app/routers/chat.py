from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.linking_methods import MemoryLinkingService
from models.inference import MemoryInference

class ChatRouter:
    def __init__(self):
        self.router = APIRouter()
        self.memory_service = MemoryLinkingService()
        self.inference_model = MemoryInference('path/to/model')
        self._setup_routes()

    def _setup_routes(self):
        @self.router.websocket("/chat")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            try:
                while True:
                    data = await websocket.receive_text()
                    response = self._process_chat_message(data)
                    await websocket.send_text(response)
            except WebSocketDisconnect:
                print("Client disconnected")

    def _process_chat_message(self, message: str) -> str:
        # Retrieve relevant memories
        memories = self.memory_service.retrieve_context(message)
        
        # Generate response using inference model
        response = self.inference_model.generate_response(
            prompt=message, 
            memory_context=memories
        )
        
        # Store interaction for future learning
        self.memory_service.store_interaction(message, response)
        
        return response

chat_router = ChatRouter().router