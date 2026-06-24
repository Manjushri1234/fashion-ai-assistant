import numpy as np
import faiss

# Load embeddings
embeddings = np.load(
    "vectorstore/product_embeddings.npy"
)

print("Embeddings Shape:")
print(embeddings.shape)

# Get vector dimension
dimension = embeddings.shape[1]

# Create FAISS Index
index = faiss.IndexFlatL2(
    dimension
)

# Add vectors
index.add(
    embeddings.astype("float32")
)

print("\nTotal vectors in index:")
print(index.ntotal)

# Save index
faiss.write_index(
    index,
    "vectorstore/fashion.index"
)

print("\nIndex saved successfully!")