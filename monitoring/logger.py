import json
import logging
import time

class StructuredLogger:
    """
    Formats log entries as JSON for observability and log aggregation systems (e.g. Datadog, ELK).
    """
    def __init__(self, service_name: str = "MultiAgentOpsCrew"):
        self.service_name = service_name

    def log_event(self, event_type: str, agent: str, message: str, payload: dict = None):
        log_entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "service": self.service_name,
            "event_type": event_type,
            "agent": agent,
            "message": message,
            "payload": payload or {}
        }
        print(json.dumps(log_entry))
