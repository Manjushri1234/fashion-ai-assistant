from data_loader import load_products

products = load_products()

print(
    products[
        [
            "id",
            "name",
            "image"
        ]
    ].head(10)
)