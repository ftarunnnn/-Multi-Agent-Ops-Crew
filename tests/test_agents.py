import unittest
from src.agents import PlannerAgent, DataAgent, MLAgent, ResearchAgent, ReviewerAgent, ReportAgent

class TestAgents(unittest.TestCase):
    def test_planner_agent(self):
        agent = PlannerAgent()
        state = {"user_request": "AI Data Analysis Automation"}
        result = agent.run(state)
        self.assertIn("plan", result)
        self.assertEqual(len(result["plan"]["steps"]), 5)

    def test_data_agent(self):
        agent = DataAgent()
        state = {
            "sales_file_path": "phase_1_problem_definition/sample_data/sales_metrics.csv",
            "feedback_file_path": "phase_1_problem_definition/sample_data/customer_feedback.json"
        }
        result = agent.run(state)
        self.assertIn("data_artifacts", result)
        self.assertGreater(result["data_artifacts"]["total_revenue_usd"], 0)

    def test_ml_agent(self):
        agent = MLAgent()
        state = {"sales_file_path": "phase_1_problem_definition/sample_data/sales_metrics.csv"}
        result = agent.run(state)
        self.assertIn("ml_artifacts", result)
        self.assertIn("q2_projected_revenue_usd", result["ml_artifacts"])

    def test_reviewer_agent(self):
        agent = ReviewerAgent()
        state = {
            "data_artifacts": {"total_revenue_usd": 100000, "total_marketing_spend_usd": 20000, "overall_roi": 400.0},
            "ml_artifacts": {},
            "research_artifacts": {}
        }
        result = agent.run(state)
        self.assertIn("review_results", result)
        self.assertEqual(result["review_results"]["quality_score"], 100)

if __name__ == "__main__":
    unittest.main()
