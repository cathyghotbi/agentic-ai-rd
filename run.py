import json
from agents.coordinator import CoordinatorAgent

if __name__ == "__main__":
    agent = CoordinatorAgent()

    # Example "research task"
    task = {"target": "TP53"}

    result = agent.run(task)

    print("\n=== FINAL REPORT ===")
    #print(result) # one-line results
    print(json.dumps(result, indent=2)) # formatted into multiline output
    """
    # to write the output to a file:
    with open("report.json", "w") as f:
        json.dump(result, f, indent=2)
    """

"""
How to run:
PS C:\\Users\\Cathy\\PycharmProjects\\pythonProject1\\agentic-ai-rd> python run.py

When the code is run:
A coordinator agent orchestrates multiple domain agents via a state machine.
Each step requires human approval, executes registered tools with logging, and passes structured context forward.
The result is a reproducible, auditable scientific report.

Q: Why human-in-the-loop?
→ Cost control, safety, and regulatory requirements.

Q: Why a tool registry?
→ Prevents hallucinated tool usage and enables auditability.

Q: Why not fully autonomous?
→ R&D requires trust, reproducibility, and oversight.
"""
