"""
Coordinator Agent

This agent is responsible for:
- Owning the overall workflow
- Executing agents in the correct order
- Managing shared context between agents

the "control plane" for the agent system.
"""

from orchestration.state_machine import StateMachine
from agents.literature_agent import literature_agent
from agents.analysis_agent import analysis_agent
from agents.reporting_agent import reporting_agent


class CoordinatorAgent:
    def __init__(self):
        # StateMachine encapsulates execution logic such as:
        # - step ordering
        # - approvals
        # - error handling
        self.state_machine = StateMachine()

    def run(self, task_input: dict) -> dict:
        """
        Entry point for running the full agent workflow.

        Args:
            task_input: user-provided task definition (e.g. target name)

        Returns:
            Final structured report produced by the agents
        """
        # Shared context object passed between agents
        context = {"task": task_input}

        # Step 1: literature and metadata gathering
        context = self.state_machine.run_step(
            "literature_review",
            literature_agent,
            context,
        )

        # Step 2: computational analysis
        context = self.state_machine.run_step(
            "analysis",
            analysis_agent,
            context,
        )

        # Step 3: reporting and summarization
        context = self.state_machine.run_step(
            "reporting",
            reporting_agent,
            context,
        )

        # Return only the final output, not internal state
        return context["final_report"]
