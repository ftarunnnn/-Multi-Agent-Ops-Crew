from typing import List, Dict, Any
from src.memory.vector_store import VectorStore

class RAGEngine:
    """
    RAG Engine: Ingests documents, chunks content, and retrieves context for agents.
    """
    def __init__(self):
        self.vector_store = VectorStore()
        # Seed default benchmark knowledge base
        self._seed_knowledge_base()

    def _seed_knowledge_base(self):
        docs = [
            ("kb_01", "B2B SaaS metric standard: Top quartile SaaS companies maintain NPS above 55 and monthly churn below 1.5%."),
            ("kb_02", "Customer Acquisition Cost (CAC) payback period benchmark for Enterprise segment is 12 months, SMB is 8 months."),
            ("kb_03", "Revenue forecasting model baseline accuracy (R2) must exceed 0.90 for enterprise financial planning."),
            ("kb_04", "North America region delivers highest Average Revenue Per User (ARPU) across global SaaS tiers.")
        ]
        for doc_id, text in docs:
            self.vector_store.add_document(doc_id=doc_id, content=text, metadata={"category": "saas_benchmarks"})

    def retrieve_context(self, query: str, top_k: int = 2) -> List[str]:
        results = self.vector_store.search(query, top_k=top_k)
        return [res["content"] for res in results]
