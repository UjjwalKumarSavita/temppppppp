from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class State:
    problem: str
    domain: str = "unknown"
    assumptions: List[str] = field(default_factory=list)
    approach: str = ""
    solution: Any = None
    verified: bool = False
    explanation: str = ""
    meta: Dict[str, Any] = field(default_factory=dict)
