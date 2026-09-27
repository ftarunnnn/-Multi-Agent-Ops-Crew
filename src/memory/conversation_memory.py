from typing import List, Dict, Any

class ConversationMemory:
    """
    Short-Term Agent Conversation Memory buffer.
    """
    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self.history: List[Dict[str, Any]] = []

    def add_message(self, sender: str, content: str, metadata: Dict[str, Any] = None):
        self.history.append({
            "sender": sender,
            "content": content,
            "metadata": metadata or {}
        })
        if len(self.history) > self.max_messages:
            self.history.pop(0)

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
