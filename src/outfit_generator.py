from data_loader import load_products
from data_loader import load_outfits
import os

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

    print("\n===== HERO PRODUCT =====")
    print(hero)
    print(
        "HERO IMAGE:",
        hero["image"] if hero is not None else "NONE"
    )
    print("========================\n")

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