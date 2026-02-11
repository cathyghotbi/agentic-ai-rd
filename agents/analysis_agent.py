"""
Analysis Agent

Runs computational analysis steps.
In real drug discovery pipelines this might include:
- Sequence QC
- Structure prediction
- Feature extraction
"""

from tools.registry import ToolRegistry


def analysis_agent(context: dict) -> dict:
    # ---- Validate inputs ----
    literature = context.get("literature")
    if literature is None:
        raise ValueError("Missing 'literature' in context")

    sequence = literature.get("sequence")
    if not sequence:
        raise ValueError("No sequence found in literature data")

    registry = ToolRegistry()

    # ---- Run tools ----
    # Quality control on the protein sequence
    qc_result = registry.execute(
        tool_name="run_sequence_qc",
        params={"sequence": sequence},
    )

    # Structure prediction (mocked)
    structure_result = registry.execute(
        tool_name="predict_structure",
        params={"sequence": sequence},
    )

    mw_result = registry.execute(
        tool_name="calculate_molecular_weight",
        params={"sequence": sequence},
    )

    # Store structured analysis outputs
    # context["analysis"] = {
    #     "qc": qc,
    #     "structure": structure,
    # }
    context["analysis"] = {
        "sequence": {
            "length": len(sequence),
        },
        "qc": qc_result,
        "structure": structure_result,
        "molecular_weight": mw_result,
    }

    return context
