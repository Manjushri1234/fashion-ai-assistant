from data_loader import load_products
from data_loader import load_outfits
import os

def get_image_path(product):

    if product is None:
        return None

    try:

        image_path = str(product["image"]).strip()

        current_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        project_root = os.path.dirname(
            current_dir
        )

        full_path = os.path.join(
            project_root,
            "data",
            image_path
        )

        print("IMAGE:", image_path)
        print("FULL PATH:", full_path)
        print("EXISTS:", os.path.exists(full_path))

        if os.path.exists(full_path):
            return full_path

        return None

    except Exception as e:

        print("ERROR:", e)

        return None