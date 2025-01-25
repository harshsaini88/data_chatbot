from models.models import LearningProgressTracker
import pandas as pd

class PerformanceAnalytics:
    def __init__(self):
        self.progress_tracker = LearningProgressTracker()

    def get_overall_progress(self):
        analytics = self.progress_tracker.get_learning_analytics()
        return {
            'avg_recall_accuracy': round(analytics['avg_recall_accuracy'] * 100, 2),
            'avg_concept_retention': round(analytics['avg_concept_retention'] * 100, 2),
            'learning_progress': round(analytics['learning_progress'] * 100, 2)
        }

    def analyze_memory_retention(self):
        # More advanced memory retention analysis
        retention_data = self.progress_tracker.performance_metrics
        df = pd.DataFrame(retention_data)
        
        return {
            'trend': df.mean().to_dict(),
            'volatility': df.std().to_dict()
        }