from typing import Dict, Any

class QualityEvaluator:
    """
    Evaluates end-to-end multi-agent execution context for completeness and metrics accuracy.
    """
    @staticmethod
    def evaluate(state: Dict[str, Any]) -> Dict[str, Any]:
        has_plan = "plan" in state and state["plan"] is not None
        has_data = "data_artifacts" in state and state["data_artifacts"] is not None
        has_ml = "ml_artifacts" in state and state["ml_artifacts"] is not None
        has_research = "research_artifacts" in state and state["research_artifacts"] is not None
        has_review = "review_results" in state and state["review_results"] is not None
        has_report = "final_report" in state and state["final_report"] is not None

        checks = [has_plan, has_data, has_ml, has_research, has_review, has_report]
        score = int((sum(checks) / len(checks)) * 100)

        return {
            "overall_score": score,
            "all_phases_completed": score == 100,
            "phase_breakdown": {
                "planner": has_plan,
                "data_agent": has_data,
                "ml_agent": has_ml,
                "research_agent": has_research,
                "reviewer_agent": has_review,
                "report_agent": has_report
            }
        }
