import re
from typing import Dict, Any, List

class HallucinationChecker:
    """
    Hallucination Checker: Audits final report markdown against ground truth data artifacts.
    """
    @staticmethod
    def audit_report(report_md: str, data_artifacts: Dict[str, Any]) -> Dict[str, Any]:
        unverified_numbers = []
        verified_numbers = []

        # Extract dollar amounts and percentages from report
        numbers = re.findall(r'\$?([\d,]+\.?\d*)', report_md)
        ground_truth_values = set()
        
        # Flatten data artifacts values
        for v in data_artifacts.values():
            if isinstance(v, (int, float)):
                ground_truth_values.add(str(v))
                ground_truth_values.add(f"{v:,.2f}")
                ground_truth_values.add(str(round(v, 2)))

        for n in numbers:
            clean_num = n.replace(",", "")
            if clean_num in ground_truth_values or len(clean_num) <= 2:
                verified_numbers.append(n)
            else:
                unverified_numbers.append(n)

        score = max(0, 100 - (len(unverified_numbers) * 10))
        return {
            "score": score,
            "hallucination_risk": "HIGH" if score < 70 else "LOW",
            "verified_count": len(verified_numbers),
            "unverified_count": len(unverified_numbers)
        }
