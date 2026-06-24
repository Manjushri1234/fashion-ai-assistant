import pandas as pd
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
from tqdm import tqdm

# Load products dataset
products = pd.read_csv("data/products.csv")

print("Loading CLIP model...")

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

embeddings = []

print("\nGenerating embeddings...")

for _, row in tqdm(
    products.iterrows(),
    total=len(products)
):

    try:

        image_path = "data/" + row["image"]

        image = Image.open(
            image_path
        ).convert("RGB")

        inputs = processor(
            images=image,
            return_tensors="pt"
        )

        with torch.no_grad():

            outputs = model.vision_model(
                pixel_values=inputs["pixel_values"]
            )

        vector = (
            outputs.pooler_output
            .cpu()
            .numpy()[0]
        )

        embeddings.append(vector)

    except Exception as e:

        print(f"\nError loading: {image_path}")
        print(e)

        embeddings.append(None)

print("\n" + "=" * 50)
print(f"Generated {len(embeddings)} embeddings")

valid_embeddings = sum(
    1 for e in embeddings
    if e is not None
)

print(f"Valid embeddings: {valid_embeddings}")
print("=" * 50)

# Save embeddings
embedding_matrix = np.array(
    [e for e in embeddings if e is not None]
)

np.save(
    "vectorstore/product_embeddings.npy",
    embedding_matrix
)

print("\nEmbeddings saved successfully!")
print("File: vectorstore/product_embeddings.npy")