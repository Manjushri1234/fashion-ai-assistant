import faiss
import numpy as np
import pandas as pd

# Load products
products = pd.read_csv(
    "data/products.csv"
)

# Load FAISS index
index = faiss.read_index(
    "vectorstore/fashion.index"
)

# Load embeddings
embeddings = np.load(
    "vectorstore/product_embeddings.npy"
)

# Use first product as test query
query_vector = embeddings[0].reshape(
    1,
    -1
).astype("float32")

# Search Top 5
distances, indices = index.search(
    query_vector,
    5
)

print("\nTop Similar Products:\n")

for idx in indices[0]:

    product = products.iloc[idx]

    print(
        f"{product['name']} | "
        f"{product['category']}"
    )