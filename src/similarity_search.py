import pandas as pd


def get_similar_product_ids(
    product_index,
    top_k=5
):
    """
    Dummy similarity function for Streamlit deployment.
    Returns first few product indices without using FAISS.
    """

    products = pd.read_csv(
        "data/products.csv"
    )

    total_products = len(products)

    return list(
        range(
            min(top_k, total_products)
        )
    )