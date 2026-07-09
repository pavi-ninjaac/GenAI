# Routing - Revision Notes 🧭

## 🔀 Logical Routing
- Uses **function calling** to classify which data source to use based on the user's question.
- Creates a structured output (like choosing between python_docs, js_docs, golang_docs) to route the query to the right place.
- Works like a smart traffic cop 🚦 - reads the question and sends it to the most relevant data source.

## 🎯 Semantic Routing
- Uses **embeddings and cosine similarity** to match questions with the best prompt template.
- Pre-embeds different prompt templates (like physics expert, math expert) and compares them with the question embedding.
- Picks the template with the highest similarity score - finds the closest match automatically without explicit rules! 📊

## 🏷️ Query Structuring for Metadata Filters
- Converts natural language questions into **structured database queries** with filters.
- Extracts metadata filters from user questions (like view count, publish date, video length) and creates a search query.
- Helps you search smarter by combining text search with specific filters - like asking "find videos on RAG published in 2023 under 5 minutes" 🔍

---

## Quick Comparison 🆚

| Method | How It Works | Best For |
|--------|-------------|----------|
| 🔀 **Logical Routing** | Function calling → picks a category | Routing to different data sources |
| 🎯 **Semantic Routing** | Embedding similarity → finds closest match | Choosing between different prompt styles |
| 🏷️ **Query Structuring** | LLM → extracts filters from text | Searching databases with metadata |
