import faiss
import numpy as np
import pandas as pd


def get_similar_product_ids(
    product_index,
    top_k=5
):

    products = pd.read_csv(
        "data/products.csv"
    )

    index = faiss.read_index(
        "vectorstore/fashion.index"
    )

    embeddings = np.load(
        "vectorstore/product_embeddings.npy"
    )

    query_vector = embeddings[
        product_index
    ].reshape(
        1,
        -1
    ).astype(
        "float32"
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    return indices[0]