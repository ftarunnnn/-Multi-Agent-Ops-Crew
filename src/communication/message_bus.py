import logging
from typing import Dict, Any, List, Callable

class MessageBus:
    """
    Publish-Subscribe Message Bus for agent events and asynchronous communications.
    """
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
        self.logger = logging.getLogger("MessageBus")

    def subscribe(self, topic: str, handler: Callable):
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(handler)
        self.logger.info(f"Subscribed handler to topic '{topic}'")

    def publish(self, topic: str, payload: Dict[str, Any]):
        self.logger.info(f"Publishing event to topic '{topic}'")
        handlers = self._subscribers.get(topic, [])
        for handler in handlers:
            try:
                handler(payload)
            except Exception as e:
                self.logger.error(f"Error handling event on topic '{topic}': {e}")
