from src.outfit_generator import generate_outfit

rec = generate_outfit("outfit_M4")

print(rec["topwear_image"])
print(rec["bottomwear_image"])
print(rec["footwear_image"])
print(rec["accessory_image"])