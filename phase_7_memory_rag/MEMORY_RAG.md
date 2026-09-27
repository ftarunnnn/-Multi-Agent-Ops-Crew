# Phase 7 — Memory & RAG (Retrieval-Augmented Generation) System

## Overview
Phase 7 adds persistent memory and document retrieval capabilities to the Multi-Agent Ops Crew.

---

## Memory Subsystems

```
┌─────────────────────────────────────────────────────────────┐
│                       AGENT MEMORY ENGINE                   │
├──────────────────────────────┬──────────────────────────────┤
│    Short-Term Memory        │      Long-Term RAG Vector    │
│  (Conversation Buffer)       │          (VectorStore)       │
├──────────────────────────────┼──────────────────────────────┤
│ - Sliding window context     │ - In-memory vector embeddings│
│ - Intermediate agent logs    │ - Document chunking (500 tok)│
│ - Rapid state lookup         │ - Cosine similarity ranking  │
└──────────────────────────────┴──────────────────────────────┘
```

---

## RAG Retrieval Workflow
1. **Document Ingestion**: Ingests markdown, CSV, and text reports.
2. **Text Chunking**: Splits documents into overlapping passages (size=300 chars, overlap=50 chars).
3. **Embedding Generation & Indexing**: Calculates term vectors and indexes into `VectorStore`.
4. **Agent Semantic Search**: Research & Reviewer agents query the vector store for benchmark retrieval.
