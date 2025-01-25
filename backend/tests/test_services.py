import pytest
from services.linking_methods import MemoryLinkingService
from services.analytics import PerformanceAnalytics

def test_memory_linking_service():
    service = MemoryLinkingService()
    
    context = service.retrieve_context("AI learning")
    assert isinstance(context, list)
    
    service.store_interaction("Test user message", "Test AI response")
    assert len(service.interaction_history) > 0

def test_performance_analytics():
    analytics = PerformanceAnalytics()
    
    progress = analytics.get_overall_progress()
    assert all(0 <= val <= 100 for val in progress.values())
    
    retention = analytics.analyze_memory_retention()
    assert "trend" in retention
    assert "volatility" in retention