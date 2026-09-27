import json
import pandas as pd
from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class DataAgent(BaseAgent):
    """
    Data Agent: Cleans datasets, executes statistical profiling, and calculates KPI metrics.
    """
    def __init__(self, llm_provider=None, tools=None):
        super().__init__(
            name="DataAgent",
            role="Data Analytics Specialist",
            goal="Process raw sales telemetry and customer feedback to compute accurate statistical summaries.",
            llm_provider=llm_provider,
            tools=tools
        )

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        sales_file = state.get("sales_file_path", "phase_1_problem_definition/sample_data/sales_metrics.csv")
        feedback_file = state.get("feedback_file_path", "phase_1_problem_definition/sample_data/customer_feedback.json")

        self.logger.info(f"Analyzing datasets: {sales_file}, {feedback_file}")

        # Ingest and process CSV data
        try:
            df_sales = pd.read_csv(sales_file)
            total_revenue = float(df_sales["revenue_usd"].sum())
            total_marketing = float(df_sales["marketing_spend_usd"].sum())
            avg_cac = float(df_sales["customer_acquisition_cost"].mean())
            avg_churn = float(df_sales["churn_rate"].mean())
            avg_nps = float(df_sales["net_promoter_score"].mean())
            
            # Regional aggregation
            region_summary = df_sales.groupby("region").agg({
                "revenue_usd": "sum",
                "marketing_spend_usd": "sum",
                "customer_acquisition_cost": "mean",
                "churn_rate": "mean"
            }).to_dict(orient="index")

            # Ingest JSON feedback
            with open(feedback_file, "r") as f:
                feedback_data = json.load(f)
                
            sentiment_counts = {}
            for item in feedback_data:
                s = item.get("sentiment", "Neutral")
                sentiment_counts[s] = sentiment_counts.get(s, 0) + 1

            data_artifacts = {
                "total_revenue_usd": total_revenue,
                "total_marketing_spend_usd": total_marketing,
                "overall_roi": round((total_revenue - total_marketing) / total_marketing * 100, 2),
                "avg_cac_usd": round(avg_cac, 2),
                "avg_churn_rate_pct": round(avg_churn * 100, 2),
                "avg_nps": round(avg_nps, 1),
                "regional_metrics": region_summary,
                "feedback_sentiment_summary": sentiment_counts,
                "row_count": len(df_sales)
            }

            state["data_artifacts"] = data_artifacts
            return state

        except Exception as e:
            self.logger.error(f"Error reading dataset files: {e}")
            raise e
