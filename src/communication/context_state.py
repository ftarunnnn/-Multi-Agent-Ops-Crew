import uuid
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

@dataclass
class ContextState:
    """
    Centralized, serializable workflow context state object shared across agents.
    """
    task_id: str = field(default_factory=lambda: f"task_{uuid.uuid4().hex[:8]}")
    user_request: str = "AI Data Analysis Automation"
    sales_file_path: str = "phase_1_problem_definition/sample_data/sales_metrics.csv"
    feedback_file_path: str = "phase_1_problem_definition/sample_data/customer_feedback.json"
    plan: Optional[Dict[str, Any]] = None
    data_artifacts: Optional[Dict[str, Any]] = None
    ml_artifacts: Optional[Dict[str, Any]] = None
    research_artifacts: Optional[Dict[str, Any]] = None
    review_results: Optional[Dict[str, Any]] = None
    final_report: Optional[str] = None
    execution_logs: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "user_request": self.user_request,
            "sales_file_path": self.sales_file_path,
            "feedback_file_path": self.feedback_file_path,
            "plan": self.plan,
            "data_artifacts": self.data_artifacts,
            "ml_artifacts": self.ml_artifacts,
            "research_artifacts": self.research_artifacts,
            "review_results": self.review_results,
            "final_report": self.final_report,
            "execution_logs": self.execution_logs
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ContextState":
        return cls(
            task_id=data.get("task_id", f"task_{uuid.uuid4().hex[:8]}"),
            user_request=data.get("user_request", "AI Data Analysis Automation"),
            sales_file_path=data.get("sales_file_path", "phase_1_problem_definition/sample_data/sales_metrics.csv"),
            feedback_file_path=data.get("feedback_file_path", "phase_1_problem_definition/sample_data/customer_feedback.json"),
            plan=data.get("plan"),
            data_artifacts=data.get("data_artifacts"),
            ml_artifacts=data.get("ml_artifacts"),
            research_artifacts=data.get("research_artifacts"),
            review_results=data.get("review_results"),
            final_report=data.get("final_report"),
            execution_logs=data.get("execution_logs", [])
        )
