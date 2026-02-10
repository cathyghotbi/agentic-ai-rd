"""
Human-in-the-loop checkpoints.

Used to prevent expensive or irreversible actions
from running without approval.
"""


def require_approval(step_name: str):
    """
    Simple CLI-based approval gate.
    """
    print(f"[HITL] Approve step '{step_name}'? (y/n): ", end="")
    response = input().strip().lower()
    if response != "y":
        raise RuntimeError(f"Step '{step_name}' rejected by human")
