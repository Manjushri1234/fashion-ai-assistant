from data_loader import load_products
from data_loader import load_outfits


def get_product(products, product_id):

    product = products[
        products["id"] == product_id
    ]

    if product.empty:
        return None

    return product.iloc[0]


def generate_outfit(outfit_id):

    products = load_products()
    outfits = load_outfits()

    outfit = outfits[
        outfits["outfit_id"] == outfit_id
    ].iloc[0]

    hero = get_product(
        products,
        outfit["hero_id"]
    )

    second = get_product(
        products,
        outfit["second_id"]
    )

    footwear = get_product(
        products,
        outfit["footwear_id"]
    )

    accessory = get_product(
        products,
        outfit["accessory_1_id"]
    )

    # FAISS removed for Streamlit deployment
    similar_products = []

    recommendation = {

        "theme": outfit["theme"],

        "occasion": outfit["occasion"],

        "topwear":
        hero["name"] if hero is not None else None,

        "topwear_image":
        "data/" + hero["image"]
        if hero is not None else None,

        "bottomwear":
        second["name"] if second is not None else None,

        "bottomwear_image":
        "data/" + second["image"]
        if second is not None else None,

        "footwear":
        footwear["name"] if footwear is not None else None,

        "footwear_image":
        "data/" + footwear["image"]
        if footwear is not None else None,

        "accessory":
        accessory["name"] if accessory is not None else None,

        "accessory_image":
        "data/" + accessory["image"]
        if accessory is not None else None,

        "reason":
        outfit["stylist_rationale"],

        "similar_products":
        similar_products
    }

    return recommendation


if __name__ == "__main__":

    recommendation = generate_outfit(
        "outfit_M4"
    )

    print("\nRecommended Outfit\n")

    for key, value in recommendation.items():

        print(
            f"{key}: {value}"
        )