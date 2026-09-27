from typing import Dict, Any

class TelemetryMetrics:
    """
    Collects performance telemetry: latency, token counts, error rates, quality scores.
    """
    def __init__(self):
        self.metrics_history: List[Dict[str, Any]] = []

    def record_run(self, task_id: str, duration: float, quality_score: int, agent_count: int = 6):
        record = {
            "task_id": task_id,
            "duration_seconds": round(duration, 3),
            "quality_score": quality_score,
            "agent_count": agent_count,
            "status": "SUCCESS" if quality_score >= 90 else "WARNING"
        }
        self.metrics_history.append(record)

    def get_summary(self) -> Dict[str, Any]:
        if not self.metrics_history:
            return {"total_runs": 0, "avg_duration_sec": 0, "avg_quality_score": 100}
        
        avg_dur = sum(m["duration_seconds"] for m in self.metrics_history) / len(self.metrics_history)
        avg_score = sum(m["quality_score"] for m in self.metrics_history) / len(self.metrics_history)
        return {
            "total_runs": len(self.metrics_history),
            "avg_duration_sec": round(avg_dur, 2),
            "avg_quality_score": round(avg_score, 1)
        }
