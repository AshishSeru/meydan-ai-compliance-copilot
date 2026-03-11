import streamlit as st
import os
from openai import OpenAI
import faiss
import numpy as np

# UI
st.title("Meydan Free Zone AI Compliance Copilot")
st.write("Ask questions about business setup, visas, compliance and licensing.")

# API key input
api_key = st.text_input("Enter OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # Load documents
    docs = []
    doc_folder = "docs"

    for file in os.listdir(doc_folder):
        if file.endswith(".txt"):
            with open(os.path.join(doc_folder, file), "r", encoding="utf-8") as f:
                docs.append(f.read())

    text = "\n".join(docs)

    # Simple chunking
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    # Create embeddings
    embeddings = []
    for chunk in chunks:
        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(emb.data[0].embedding)

    embeddings = np.array(embeddings).astype("float32")

    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    query = st.text_input("Ask a question")

    if query:
        q_emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        ).data[0].embedding

        q_emb = np.array([q_emb]).astype("float32")

        distances, indices = index.search(q_emb, 3)

        context = "\n".join([chunks[i] for i in indices[0]])

        prompt = f"""
Use the following UAE free zone information to answer the question.

Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"You are a UAE business setup assistant."},
                {"role":"user","content":prompt}
            ]
        )

        st.write(response.choices[0].message.content)