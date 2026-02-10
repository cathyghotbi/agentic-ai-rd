"""
Reporting Agent

Responsible for producing a human-readable and machine-readable
summary of all prior steps.

This agent does NOT perform tool execution.
It consumes validated results only.
"""


def reporting_agent(context: dict) -> dict:
    # Build a final report from validated upstream data
    report = {
        "target": context["task"]["target"],
        "summary": "Automated discovery report",
        "qc_status": context["analysis"]["qc"]["status"],
        "structure_confidence": context["analysis"]["structure"]["confidence"],
    }

    # Store final output in context
    context["final_report"] = report
    return context
