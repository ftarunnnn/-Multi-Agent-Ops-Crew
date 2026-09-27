import copy
from typing import Dict, Any, List

class StateMachine:
    """
    Manages workflow state snapshots and checkpoints for replayability.
    """
    def __init__(self):
        self.checkpoints: List[Dict[str, Any]] = []

    def checkpoint(self, node_name: str, state: Dict[str, Any]):
        snapshot = {
            "node": node_name,
            "state_snapshot": copy.deepcopy(state)
        }
        self.checkpoints.append(snapshot)

    def get_last_checkpoint((self) -> Dict[str, Any]:
        return self.checkpoints[-1] if self.checkpoints else {}
