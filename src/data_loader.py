import pandas as pd
from config import PRODUCTS_PATH, OUTFITS_PATH


def load_products():
    return pd.read_csv(PRODUCTS_PATH)


def load_outfits():
    return pd.read_csv(OUTFITS_PATH)