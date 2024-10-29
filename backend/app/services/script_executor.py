# app/services/script_executor.py
from typing import List, Dict

def execute_script(code: str) -> List[Dict]:
    # Simulate step-by-step output
    steps = [
        {"step": 1, "output": "Initialize array"},
        {"step": 2, "output": "Update index 1"},
        {"step": 3, "output": "Find maximum sum"}
    ]
    return steps
