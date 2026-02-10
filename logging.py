"""
Centralized logging utilities.

In production, this would integrate with Cloud Logging
or another observability platform.
"""

import logging

# Configure root logger
logging.basicConfig(level=logging.INFO)


def log_tool_call(tool_name: str, params: dict):
    """
    Log structured tool execution events.

    This is critical for:
    - Auditing
    - Debugging
    - Scientific provenance
    """
    logging.info(
        "tool_call",
        extra={
            "tool": tool_name,
            "params": params,
        },
    )
