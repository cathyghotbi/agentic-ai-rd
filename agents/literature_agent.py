"""
Literature Agent

Responsible for retrieving background information about a target.
In a real system, this might query:
- Internal databases
- Literature APIs
- Knowledge graphs
"""

from tools.registry import ToolRegistry


def literature_agent(context: dict) -> dict:
    # ToolRegistry provides a controlled interface for tool execution
    registry = ToolRegistry()

    # Execute a registered tool using structured parameters
    result = registry.execute(
        tool_name="fetch_target_metadata",
        params={"target": context["task"]["target"]},
    )

    # Store results in shared context for downstream agents
    context["literature"] = result
    return context
