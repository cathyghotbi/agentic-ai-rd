
## Agentic AI Platform for Scientific R&D
This project demonstrates how agentic AI can be deployed as a reliable, 
auditable platform for scientific R&D, inspired by real drug discovery workflows.

The project demonstrates a production-oriented agentic AI platform
for orchestrating scientific workflows.

The project was developed with the assistance of AI, which helped in:

- Designing the architecture of an agentic AI platform
- Writing example Python code for agents, tools, and workflows
- Creating tests and documentation

All final design decisions, engineering integrations, and testing were performed and verified by the developer to ensure a production-ready, reliable, and auditable system.



## Key Capabilities

- Multi-agent orchestration using a CoordinatorAgent
- Human-in-the-loop workflow with automatic approvals for testing
- Structured logging and provenance
- Cloud-native deployment (GCP Cloud Run)
- Model Context Protocol (MCP) integration for tool/context standardization
- Fully tested workflow with logs and JSON outputs
- Designed for bioinformatics and drug discovery R&D


## Example Use Case
Automated protein target analysis for early-stage drug discovery.


## Design Philosophy
This system prioritizes:
- Reliability over demos
- Explicit control over autonomy
- Platform engineering over experimentation

## Example Run Output

Below is the actual output produced by running the agent workflow locally
using a mock protein target (`TP53`).
The system produces structured JSON outputs, which can be stored, versioned, audited, or consumed by downstream systems.

```bash
PS C:\Users\Cathy\PycharmProjects\pythonProject1\agent-platform> python run.py

[HITL] Approve step 'literature_review'? (y/n): y
INFO:root:tool_call
[HITL] Approve step 'analysis'? (y/n): y
INFO:root:tool_call
INFO:root:tool_call
[HITL] Approve step 'reporting'? (y/n): y


=== FINAL REPORT ===
{
  "target": "TP53",
  "summary": "Automated discovery report",
  "qc_status": "PASS",
  "structure_confidence": 0.87
}
```

## Example Test Run Output

```bash
{
PS C:\Users\Cathy\PycharmProjects\pythonProject1\agent-platform> python -m pytest -s
============================================================================================ test session starts =============================================================================================
platform win32 -- Python 3.11.4, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\Cathy\PycharmProjects\pythonProject1\agent-platform
collected 1 item                                                                                                                                                                                              

tests\test_agents.py
[TEST] Starting full agent workflow test
[TEST] Monkeypatching input() to auto-approve all steps
[TEST] Initializing CoordinatorAgent
[TEST] Running workflow with task: {'target': 'TP53'}
[HITL] Approve step 'literature_review'? (y/n): [HITL] Approve step 'analysis'? (y/n): [HITL] Approve step 'reporting'? (y/n): [TEST] Workflow completed successfully
[TEST] Final result:
{'target': 'TP53', 'summary': 'Automated discovery report', 'qc_status': 'PASS', 'structure_confidence': 0.87}
[TEST] Validating results
[TEST] All assertions passed
.

============================================================================================= 1 passed in 0.02s ============================================================================================== 
PS C:\Users\Cathy\PycharmProjects\pythonProject1\agent-platform> 
}
```

## Screenshots from PyCharm Terminal


<img width="313" height="192" alt="{3F365DBF-7A64-4AC7-B111-28CEBA684978}" src="https://github.com/user-attachments/assets/ba85124c-4d4f-4aaa-ad30-cd53e3c8fed3" />

<img width="751" height="272" alt="{2A091E0D-B997-436A-8ED6-982D1E168A45}" src="https://github.com/user-attachments/assets/66bc711d-4b16-4074-82cf-0228d081880e" />



## Using real molecular weight
We start with a simple function calculate_molecular_weight in bio_tools,
in which we assue average amino acid ≈ 110 Da,

```bash
"molecular_weight": len(sequence) * 110,
```

The result will be:  29*110 = 3190

```bash
=== FINAL REPORT ===
{
  "target": "TP53",
  "summary": "Automated discovery report",
  "qc_status": "PASS",
  "structure_confidence": 0.87,
  "molecular_weight": 3190
}
```

<img width="486" height="119" alt="{3C6350A2-C762-42E2-ACFE-048D6D6C2BE3}" src="https://github.com/user-attachments/assets/51559110-5d51-42d2-b269-65fa989f0cb5" />


To use the real molecular weight, requires BioPython: pip install biopython (install in PycCharm Terminal)
By using the real calculation of molecular weight from Bio.SeqUtils,

```bash
mw = molecular_weight(sequence, seq_type='protein')
```
the result will be:

```bash
=== FINAL REPORT ===
{
  "target": "TP53",
  "summary": "Automated discovery report",
  "qc_status": "PASS",
  "structure_confidence": 0.87,
  "molecular_weight": 3343.623600000001
}
```

<img width="336" height="120" alt="{5D3BB9EA-6804-4594-A349-1BE3B47378E9}" src="https://github.com/user-attachments/assets/f8388f4b-9076-4af5-940c-92bca5c7c320" />





