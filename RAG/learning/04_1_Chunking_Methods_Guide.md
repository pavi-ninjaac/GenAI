# Complete Guide to Chunking Methods 📦

## What is Chunking? 🤔

Chunking is the process of breaking down large documents into smaller pieces (chunks) before storing them in a vector database. Think of it like cutting a pizza into slices - easier to handle and serve! 🍕

**Why do we need chunking?**
- Embedding models have **token limits** (usually 512-8192 tokens) 🚫
- Smaller chunks = more **precise retrieval** 🎯
- Better **context matching** between query and documents 🔍
- Cheaper and faster processing ⚡

---

## 1. Fixed-Size Chunking ✂️

### How It Works
- Splits text into chunks of a **fixed number of characters or tokens**
- Can add **overlap** between chunks to preserve context

### Example
```
Chunk size: 500 characters
Overlap: 50 characters
```

### Pros ✅
- **Simple and fast** to implement
- Works with any type of text

### Cons ❌
- May **break sentences** or paragraphs awkwardly
- Can split important context across chunks

### When to Use 🎯
- Quick prototyping and testing
- When document structure doesn't matter much
- Processing mixed or unstructured content


### use can use it with overlap for better context 

### Parameters to Tune 🔧
- **Chunk size**: 200-1000 tokens (depends on your use case)
- **Overlap**: 10-20% of chunk size (helps preserve context)

---

## 2. Recursive Character Text Splitting 🔄 (default in LangChain)

### How It Works
- Tries to split on **natural boundaries** in order of priority:
  1. Double newlines `\n\n` (paragraphs)
  2. Single newlines `\n` (lines)
  3. Spaces ` ` (words)
  4. Individual characters (last resort)
- Keeps trying until chunks fit the size limit

### Example
```python
separators = ["\n\n", "\n", " ", ""]
chunk_size = 1000
overlap = 200
```

### Pros ✅
- **Respects natural text structure** 📖
- Keeps paragraphs and sentences together when possible
- More readable chunks

### Cons ❌
- Slightly more complex than fixed-size
- Chunk sizes can vary
- May not work well with code or structured data

### When to Use 🎯
- **General text documents** (articles, books, reports)
- When readability matters
- Most RAG applications (this is the go-to method!)

### Parameters to Tune 🔧
- **Chunk size**: 500-2000 tokens
- **Overlap**: 100-200 tokens
- **Separators**: Customize for your content type

---

## 3. Document-Specific Splitting 📄 (👉 Best chunking method if structure exists)

### How It Works
- Uses **document structure** to create chunks:
  - **Markdown**: Split by headers (`#`, `##`, `###`)
  - **HTML**: Split by tags (`<p>`, `<div>`, `<section>`)
  - **Code**: Split by functions, classes
  - **PDF**: Split by pages, sections

### Examples

#### Markdown Splitter
```
Split by: # Headers, ## Subheaders, ### Sub-subheaders
Keeps hierarchy: Parent headers included in child chunks
```

#### HTML Splitter
```
Split by: <h1>, <p>, <div>, <article>
Preserves semantic structure
```

#### Code Splitter
```python
Split by: Functions, classes, methods
Language-aware: Python, JavaScript, Java, etc.
```

### Pros ✅
- **Preserves document structure** 🏗️
- Chunks are semantically meaningful
- Better context for specialized content
- Includes metadata (like headers, file names)

### Cons ❌
- Requires knowing document format
- Different splitter for each format
- More complex implementation

### When to Use 🎯
- **Markdown/HTML documentation** 📝
- **Code repositories** 💻
- **Structured PDFs** 📋
- When document hierarchy matters

### Parameters to Tune 🔧
- **Header levels** to split on (H1, H2, H3...)
- **Minimum chunk size** before splitting
- **Include parent headers** or not

---

## 4. Semantic Chunking 🧠

### How It Works
- Uses **embeddings** to understand content similarity
- Groups sentences with similar meanings together
- Splits when topic/meaning changes significantly

### Process
1. Break text into sentences
2. Create embeddings for each sentence
3. Calculate similarity between consecutive sentences
4. Split when similarity drops below threshold

### Pros ✅
- **Most intelligent chunking** 🎓
- Keeps related content together
- Natural topic boundaries
- Best for complex documents

### Cons ❌
- **Slowest method** (requires embedding each sentence) 🐢
- More expensive (API calls for embeddings)
- Unpredictable chunk sizes
- Overkill for simple documents

### When to Use 🎯
- High-value documents where accuracy is critical
- Multi-topic documents
- When you need the **best possible** retrieval quality
- Academic papers, research documents

### Parameters to Tune 🔧
- **Similarity threshold**: 0.5-0.8 (lower = more splits)
- **Buffer size**: How many sentences to look ahead
- **Min/max chunk size**: Set boundaries

---

## Agent based chunking:
- proposation based chunking:
  - Make small chunks maybe paragaraph chunks -> send to LLM
  - This LLM makes the chunks stand alone - means each chunk will be having its full meaning. chunks are independant.
- then agentic chunk:
  - we give this indepentent chunks to the agent with the prombt to group the same meaning chunks together.
  - we get the chunks - one chunks having all the information about the particular topic.


## 5. Sentence Splitting 📝

### How It Works
- Splits text by **sentence boundaries** (periods, question marks, etc.)
- Can combine multiple sentences into one chunk

### Example
```
Split by: . ! ?
Combine: 3-5 sentences per chunk
```

### Pros ✅
- Preserves **complete thoughts** 💭
- Natural reading flow
- Good balance between precision and context

### Cons ❌
- Sentence detection can be tricky (abbreviations, names)
- Chunk sizes can vary a lot
- May split related sentences

### When to Use 🎯
- **Q&A systems** where complete answers matter
- Legal documents, contracts
- When each sentence is important

---

## 6. Token-Based Splitting 🔢

### How It Works
- Splits based on **actual token count** (what the model sees)
- Uses the tokenizer from your embedding model

### Example
```
Max tokens: 512
Uses: tiktoken for OpenAI, HuggingFace tokenizers
```

### Pros ✅
- **Exact control** over token count ✅
- Matches embedding model limits perfectly
- No wasted space or overflow

### Cons ❌
- Requires specific tokenizer
- May split mid-sentence or mid-word
- Slower than character-based splitting

### When to Use 🎯
- When you need **exact token control**
- Working with token limits (OpenAI, etc.)
- Maximizing chunk information density

---

## How to Choose the Right Chunking Method? 🤷

### Decision Tree 🌳

```
Start Here
    ↓
Do you have structured documents (Markdown/HTML/Code)?
    ├─ YES → Use Document-Specific Splitting 📄
    └─ NO ↓
         ↓
Is retrieval quality critical & you have time/budget?
    ├─ YES → Use Semantic Chunking 🧠
    └─ NO ↓
         ↓
Do you need exact token control?
    ├─ YES → Use Token-Based Splitting 🔢
    └─ NO ↓
         ↓
Is it general text (articles, books, docs)?
    ├─ YES → Use Recursive Character Splitting 🔄 (RECOMMENDED!)
    └─ NO ↓
         ↓
Quick prototype or simple use case?
    └─ YES → Use Fixed-Size Chunking ✂️
```

---

## Best Practices & Tips 💡

### 1. Chunk Size Guidelines 📏
- **Small chunks (100-300 tokens)**:
  - More precise matching 🎯
  - Better for specific facts, Q&A
  - More chunks = slower search

- **Medium chunks (300-800 tokens)**:
  - **SWEET SPOT** for most use cases! ⭐
  - Good balance of context and precision
  - Recommended starting point

- **Large chunks (800-2000 tokens)**:
  - More context in each chunk
  - Better for summarization tasks
  - Fewer chunks = faster search

### 2. Overlap is Your Friend 🤝
- **Always use overlap** (except for semantic chunking)
- Typical overlap: 10-20% of chunk size
- Prevents important info from being split across chunks
- Example: 500 token chunks with 100 token overlap

### 3. Consider Your Use Case 🎪

| Use Case | Best Method | Chunk Size |
|----------|-------------|------------|
| 📚 General documents | Recursive Character | 500-1000 tokens |
| 💬 Chatbots | Recursive Character | 300-600 tokens |
| 📖 Long-form content | Semantic or Recursive | 800-1500 tokens |
| 💻 Code search | Code Splitter | By function/class |
| 📝 Documentation | Markdown/HTML Splitter | By section |
| ❓ Q&A systems | Sentence Splitting | 200-400 tokens |
| 🔬 Research papers | Semantic Chunking | 600-1000 tokens |

| Use case    | Best method         |
| ----------- | ------------------- |
| PDFs / docs | Section + recursive |
| Blogs       | Paragraph + overlap |
| FAQs        | Q+A per chunk       |
| Code        | Function / class    |
| Logs        | Fixed-size          |
| Legal       | Semantic / section  |
| Mixed docs  | Recursive           |


### 4. Test and Iterate 🔄
- Start with **Recursive Character Splitting** with 500 tokens and 100 overlap
- Test retrieval quality
- Adjust based on results:
  - Getting irrelevant results? → Try smaller chunks
  - Missing context? → Try larger chunks or more overlap
  - Wrong topic? → Try semantic chunking

### 5. Metadata is Powerful 🏷️
- Always add metadata to chunks:
  - Source document name
  - Page number or section
  - Creation date
  - Document type
  - Headers/titles
- Helps with filtering and ranking results

### 6. Monitor Chunk Quality 📊
- Check average chunk size
- Look for very small or very large outliers
- Review sample chunks manually
- Measure retrieval accuracy

---

## Code Examples 💻

### Recursive Character Splitting (Recommended Starting Point)
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,           # Target size
    chunk_overlap=100,        # 20% overlap
    length_function=len,      # How to measure length
    separators=["\n\n", "\n", " ", ""]  # Priority order
)

chunks = splitter.split_text(your_document)
```

### Markdown Splitting
```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

chunks = splitter.split_text(markdown_document)
```

### Semantic Chunking
```python
from langchain.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",  # or "standard_deviation"
    breakpoint_threshold_amount=95
)

chunks = splitter.split_text(your_document)
```

---

## Common Mistakes to Avoid ⚠️

1. **❌ No overlap**: Context gets lost at chunk boundaries
2. **❌ Chunks too small**: Not enough context for meaningful answers
3. **❌ Chunks too large**: Irrelevant information dilutes results
4. **❌ Ignoring document structure**: Missing semantic boundaries
5. **❌ Not testing**: What works for one dataset may not work for another
6. **❌ Forgetting metadata**: Harder to trace back to source documents

---

## Quick Reference Cheat Sheet 📋

| Priority | Method | Speed | Quality | Complexity | Best Use |
|----------|--------|-------|---------|------------|----------|
| 🥇 | Recursive Character | ⚡⚡⚡ | ⭐⭐⭐⭐ | Easy | General text (START HERE!) |
| 🥈 | Document-Specific | ⚡⚡ | ⭐⭐⭐⭐⭐ | Medium | Structured docs |
| 🥉 | Semantic | ⚡ | ⭐⭐⭐⭐⭐ | Hard | Critical quality needs |
| 4️⃣ | Token-Based | ⚡⚡ | ⭐⭐⭐ | Medium | Exact token control |
| 5️⃣ | Fixed-Size | ⚡⚡⚡ | ⭐⭐ | Easy | Prototyping |
| 6️⃣ | Sentence | ⚡⚡ | ⭐⭐⭐ | Easy | Q&A systems |

