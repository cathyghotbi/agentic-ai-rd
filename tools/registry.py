"""
Tool Registry

Acts as a controlled execution layer between agents and tools.

This mirrors Model Context Protocol (MCP) principles:
- Explicit tool registration
- Structured inputs/outputs
- Centralized logging
"""

from tools.bio_tools import (
    fetch_target_metadata,
    run_sequence_qc,
    predict_structure,
    calculate_molecular_weight,
)
from tools.logging import log_tool_call


class ToolRegistry:
    def __init__(self):
        # Map tool names to callables
        self.tools = {
            "fetch_target_metadata": fetch_target_metadata,
            "run_sequence_qc": run_sequence_qc,
            "predict_structure": predict_structure,
            "calculate_molecular_weight": calculate_molecular_weight,
        }

    def execute(self, tool_name: str, params: dict) -> dict:
        """
        Execute a registered tool in a safe, auditable way.

        Args:
            tool_name: name of the tool to run
            params: validated input parameters

        Returns:
            Tool execution result
        """
        if tool_name not in self.tools:
            raise ValueError(f"Tool not registered: {tool_name}")

        # Log every tool invocation for auditability
        log_tool_call(tool_name, params)

        # Execute the tool function
        return self.tools[tool_name](**params)
