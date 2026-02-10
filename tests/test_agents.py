"""
Basic integration test (system sanity test) for the agent workflow with verbose logging.

This test:
- Runs the entire agent workflow runs end-to-end
- Executes all agents in the correct order
- Automatically approves all human-in-the-loop checkpoints
- Produces a valid final report (output)
- Prints progress logs so it is easy to follow what is happening

To run the test in PyCharm Terminal:
PS C:\\Users\\Cathy\\PycharmProjects\\pythonProject1\\agentic-ai-rd> python -m pip install pytest
PS C:\\Users\\Cathy\\PycharmProjects\\pythonProject1\\agentic-ai-rd> python -m pytest -s (-s means show me all prints)
"""

from agents.coordinator import CoordinatorAgent


def test_full_run_with_logs(monkeypatch):
    print("\n[TEST] Starting full agent workflow test")

    # Automatically approve all HITL checkpoints
    print("[TEST] Monkeypatching input() to auto-approve all steps")
    monkeypatch.setattr("builtins.input", lambda: "y")

    # Initialize the coordinator agent
    print("[TEST] Initializing CoordinatorAgent")
    agent = CoordinatorAgent()

    # Define test task
    task = {"target": "TP53"}
    print(f"[TEST] Running workflow with task: {task}")

    # Run the full workflow
    result = agent.run(task)

    # Log final result
    print("[TEST] Workflow completed successfully")
    print("[TEST] Final result:")
    print(result)

    # Assertions (actual test checks)
    print("[TEST] Validating results")
    assert result["target"] == "TP53"
    assert result["qc_status"] == "PASS"

    print("[TEST] All assertions passed")
