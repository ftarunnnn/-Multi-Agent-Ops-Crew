import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
from src.orchestration import CrewRunner
from monitoring.metrics import TelemetryMetrics

app = FastAPI(
    title="Multi-Agent Ops Crew API",
    description="REST API for automated multi-agent data analytics and reporting.",
    version="1.0.0"
)

# Enable CORS for localhost frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metrics = TelemetryMetrics()

class CrewRunRequest(BaseModel):
    user_request: Optional[str] = "AI Data Analysis Automation"
    llm_provider: Optional[str] = "gemini"

@app.get("/")
def read_root():
    return {
        "system": "Multi-Agent Ops Crew API",
        "status": "ONLINE",
        "version": "1.0.0",
        "phases": 10
    }

@app.post("/api/v1/crew/run")
def run_crew(request: CrewRunRequest):
    start_time = time.time()
    try:
        runner = CrewRunner(provider_name=request.llm_provider or "gemini")
        final_state = runner.kickoff(user_request=request.user_request or "AI Data Analysis Automation")
        duration = time.time() - start_time
        
        quality_score = final_state.review_results.get("quality_score", 100) if final_state.review_results else 100
        metrics.record_run(task_id=final_state.task_id, duration=duration, quality_score=quality_score)

        return {
            "status": "SUCCESS",
            "task_id": final_state.task_id,
            "duration_seconds": round(duration, 3),
            "quality_score": quality_score,
            "final_report": final_state.final_report,
            "artifacts": {
                "data": final_state.data_artifacts,
                "ml": final_state.ml_artifacts,
                "research": final_state.research_artifacts,
                "review": final_state.review_results
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/metrics")
def get_metrics():
    return metrics.get_summary()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
