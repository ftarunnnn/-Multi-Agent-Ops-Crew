import argparse
from src.orchestration import CrewRunner

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Ops Crew CLI Entrypoint")
    parser.add_argument("--task", type=str, default="AI Data Analysis Automation", help="Goal prompt for the crew")
    parser.add_argument("--provider", type=str, default="gemini", choices=["gemini", "openai", "claude", "local"], help="LLM Provider")
    args = parser.parse_args()

    print("=" * 70)
    print("🤖 Multi-Agent Ops Crew — 10-Phase Autonomous Data Science Pipeline")
    print("=" * 70)
    
    runner = CrewRunner(provider_name=args.provider)
    final_state = runner.kickoff(user_request=args.task)

    print("\n" + "=" * 70)
    print("📄 FINAL VERIFIED EXECUTIVE REPORT")
    print("=" * 70 + "\n")
    print(final_state.final_report)

if __name__ == "__main__":
    main()
