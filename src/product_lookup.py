from data_loader import load_products
from data_loader import load_outfits

products = load_products()
outfits = load_outfits()

# Select outfit M4
outfit = outfits.iloc[18]

print("\nOUTFIT:")
print(outfit["outfit_id"])
print(outfit["theme"])

product_ids = [
    outfit["hero_id"],
    outfit["second_id"],
    outfit["footwear_id"],
    outfit["accessory_1_id"]
]

print("\nPRODUCT DETAILS:\n")

for pid in product_ids:

    product = products[
        products["id"] == pid
    ]

    if not product.empty:

        row = product.iloc[0]

        print(f"Name     : {row['name']}")
        print(f"Category : {row['category']}")
        print(f"Brand    : {row['brand']}")
        print("-" * 40)