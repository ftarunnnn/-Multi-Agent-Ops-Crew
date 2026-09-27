import math
import re
from typing import List, Dict, Any

class VectorStore:
    """
    Lightweight, in-memory vector database using TF-IDF term frequencies and cosine similarity.
    """
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r'\w+', text.lower())

    def _get_vector(self, tokens: List[str]) -> Dict[str, float]:
        freq = {}
        for t in tokens:
            freq[t] = freq.get(t, 0) + 1
        length = math.sqrt(sum(v ** 2 for v in freq.values()))
        if length == 0:
            return {}
        return {k: v / length for k, v in freq.items()}

    def _cosine_similarity(self, vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
        intersection = set(vec1.keys()) & set(vec2.keys())
        return sum(vec1[x] * vec2[x] for x in intersection)

    def add_document(self, doc_id: str, content: str, metadata: Dict[str, Any] = None):
        tokens = self._tokenize(content)
        vector = self._get_vector(tokens)
        self.documents.append({
            "id": doc_id,
            "content": content,
            "vector": vector,
            "metadata": metadata or {}
        })

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        query_tokens = self._tokenize(query)
        query_vector = self._get_vector(query_tokens)
        
        results = []
        for doc in self.documents:
            sim = self._cosine_similarity(query_vector, doc["vector"])
            results.append({
                "id": doc["id"],
                "content": doc["content"],
                "score": round(sim, 4),
                "metadata": doc["metadata"]
            })
            
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]
