# Phase 1 — Problem Definition: AI Data Analysis Automation

## 1. Executive Summary
Modern enterprises generate massive volumes of tabular metrics, telemetry, and qualitative customer feedback daily. Manual data analysis, feature engineering, predictive modeling, and executive report synthesis are slow, error-prone, and bottlenecked by data science availability.

**Goal**: Build an autonomous **Multi-Agent Ops Crew** that automates the end-to-end data science lifecycle:
1. **Problem & Data Ingestion**: Parsing raw tabular and qualitative metrics.
2. **Exploratory Data Analysis (EDA)**: Statistical profiling, anomaly detection, and correlation analysis.
3. **Machine Learning Insights**: Automated predictive modeling (forecasting, churn risk scoring, regression).
4. **External Knowledge & Context Retrieval**: Augmenting raw data with industry benchmarks and context.
5. **Quality & Hallucination Review**: Rigorous verification of agent findings against source ground truth.
6. **Executive Report Generation**: Formatting human-readable executive summaries with clear visualizations and action items.

---

## 2. Input Data Specifications

### Primary Dataset 1: `sales_metrics.csv`
- **Fields**:
  - `date` (YYYY-MM-DD)
  - `region` (North America, Europe, Asia Pacific, Latin America)
  - `revenue_usd` (Numeric)
  - `marketing_spend_usd` (Numeric)
  - `active_users` (Integer)
  - `customer_acquisition_cost` (CAC in USD)
  - `churn_rate` (Percentage 0.0 - 1.0)
  - `net_promoter_score` (NPS -100 to 100)

### Primary Dataset 2: `customer_feedback.json`
- **Fields**:
  - `ticket_id`
  - `customer_segment` (Enterprise, SMB, Consumer)
  - `sentiment` (Positive, Neutral, Negative)
  - `feedback_text`
  - `category` (Pricing, Product Features, Performance, Support)

---

## 3. Expected Outputs & Deliverables

1. **Analytical Summary**: Statistical distribution, key performance indicators (KPIs), trends, anomalies.
2. **Predictive Models**: Revenue prediction, churn driver analysis, CAC efficiency scoring.
3. **Executive Dashboard & Markdown Report**: Synthesized markdown report with recommendations.
4. **Verification & Audit Logs**: Quality scoring matrix and hallucination check logs.

---

## 4. Multi-Agent Ops Crew Roles

| Agent Role | Primary Function | Input | Output |
| :--- | :--- | :--- | :--- |
| **Planner Agent** | Decomposes business goal into agent execution DAG | Problem Statement + Data Schema | Task Execution Plan |
| **Data Agent** | Cleans, profiles, executes SQL/Pandas code | `sales_metrics.csv`, `feedback.json` | Statistical Profiles + Cleaned Data |
| **ML Agent** | Trains predictive models & identifies drivers | Cleaned Data + Target Variables | ML Model Metrics & Feature Importances |
| **Research Agent**| Fetches industry benchmarks & external context | Domain Query | Contextual Knowledge & Benchmarks |
| **Reviewer Agent**| Validates calculations, checks hallucinations | Intermediate Agent Outputs | Verification Matrix & Fix Directives |
| **Report Agent**  | Synthesizes final executive report | Verified Agent Artifacts | Comprehensive Executive Report |

---

## 5. Constraints & Compliance Criteria
- **Zero Hallucination Tolerance**: All numbers in final reports must strictly trace back to verified Data Agent or ML Agent outputs.
- **Latency & Scalability**: Complete execution workflow must finish cleanly within target SLA.
- **Extensibility**: Modular architecture supporting swapped LLM backends (Gemini, OpenAI, Claude, Local models).
