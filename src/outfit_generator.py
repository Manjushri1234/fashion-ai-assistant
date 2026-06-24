from data_loader import load_products
from data_loader import load_outfits
import os


def get_product(products, product_id):

    product = products[
        products["id"] == product_id
    ]

    if product.empty:
        return None

    return product.iloc[0]


def get_image_path(product):

    if product is None:
        return None

    try:

        image_path = product["image"]

        full_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "data",
                image_path
            )
        )

        if os.path.exists(full_path):
            return full_path

    except Exception:
        pass

    return None


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

    recommendation = {

        "theme":
        outfit["theme"],

        "occasion":
        outfit["occasion"],

        "topwear":
        hero["name"] if hero is not None else "N/A",

        "topwear_image":
        get_image_path(hero),

        "bottomwear":
        second["name"] if second is not None else "N/A",

        "bottomwear_image":
        get_image_path(second),

        "footwear":
        footwear["name"] if footwear is not None else "N/A",

        "footwear_image":
        get_image_path(footwear),

        "accessory":
        accessory["name"] if accessory is not None else "N/A",

        "accessory_image":
        get_image_path(accessory),

        "reason":
        outfit["stylist_rationale"],

        "similar_products":
        []
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