"""
State Machine

Controls execution flow, error handling, and approvals.
This is where reliability guarantees live.
"""

from orchestration.checkpoints import require_approval


class StateMachine:
    def run_step(self, step_name: str, agent_fn, context: dict) -> dict:
        """
        Execute a single workflow step.

        Args:
            step_name: logical name of the step
            agent_fn: callable agent function
            context: shared workflow state

        Returns:
            Updated context
        """
        # Require explicit approval before executing the step
        require_approval(step_name)

        try:
            return agent_fn(context)
        except Exception as e:
            # Wrap errors with step context for debugging
            raise RuntimeError(f"Step failed [{step_name}]: {e}")
