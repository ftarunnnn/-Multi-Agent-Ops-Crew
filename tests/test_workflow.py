import unittest
from src.orchestration import CrewRunner
from src.eval import QualityEvaluator

class TestWorkflow(unittest.TestCase):
    def test_full_crew_workflow(self):
        runner = CrewRunner(provider_name="gemini")
        final_state = runner.kickoff("AI Data Analysis Automation")
        
        self.assertIsNotNone(final_state.final_report)
        self.assertGreaterEqual(final_state.review_results["quality_score"], 90)
        
        eval_res = QualityEvaluator.evaluate(final_state.to_dict())
        self.assertTrue(eval_res["all_phases_completed"])

if __name__ == "__main__":
    unittest.main()
