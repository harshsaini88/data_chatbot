from fastapi import APIRouter, Depends
from services.analytics import PerformanceAnalytics

class AnalyticsRouter:
    def __init__(self):
        self.router = APIRouter()
        self.analytics_service = PerformanceAnalytics()
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/learning-progress")
        async def get_learning_progress():
            return self.analytics_service.get_overall_progress()

        @self.router.get("/memory-retention")
        async def get_memory_retention():
            return self.analytics_service.analyze_memory_retention()

analytics_router = AnalyticsRouter().router