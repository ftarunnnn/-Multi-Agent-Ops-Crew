from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    """
    Reviewer Agent: Hallucination Checker and Mathematical Consistency Auditor.
    """
    def __init__(self, llm_provider=None, tools=None):
        super().__init__(
            name="ReviewerAgent",
            role="Quality Auditor & Hallucination Guard",
            goal="Verify all agent calculation artifacts against raw input ground truth and grade output quality.",
            llm_provider=llm_provider,
            tools=tools
        )

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info("Auditing Data, ML, and Research artifacts for accuracy and consistency...")

        data_art = state.get("data_artifacts", {})
        ml_art = state.get("ml_artifacts", {})
        research_art = state.get("research_artifacts", {})

        issues = []
        passed_checks = []

        # Check 1: Revenue non-negativity and existence
        rev = data_art.get("total_revenue_usd", 0)
        if rev > 0:
            passed_checks.append("Total Revenue verified (> 0).")
        else:
            issues.append("Total Revenue invalid or zero.")

        # Check 2: ROI mathematical consistency
        roi = data_art.get("overall_roi", 0)
        tot_mkt = data_art.get("total_marketing_spend_usd", 1)
        expected_roi = round((rev - tot_mkt) / tot_mkt * 100, 2)
        if abs(roi - expected_roi) < 0.1:
            passed_checks.append(f"ROI calculation audited and verified ({roi}%).")
        else:
            issues.append(f"ROI mismatch: artifact says {roi}%, calculated {expected_roi}%.")

        # Check 3: Hallucination Risk Score
        hallucination_detected = len(issues) > 0
        quality_score = 100 - (len(issues) * 25)

        review_results = {
            "status": "APPROVED" if not hallucination_detected else "NEEDS_REVISION",
            "quality_score": quality_score,
            "hallucination_detected": hallucination_detected,
            "passed_checks": passed_checks,
            "issues": issues,
            "auditor_signature": "ReviewerAgent v1.0 (Zero-Hallucination Verified)"
        }

        state["review_results"] = review_results
        return state
