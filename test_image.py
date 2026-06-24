import sys
import os

sys.path.append(
    os.path.abspath("src")
)

from outfit_generator import generate_outfit

rec = generate_outfit("outfit M4")

print("\nTOP IMAGE:")
print(rec["topwear_image"])

print("\nBOTTOM IMAGE:")
print(rec["bottomwear_image"])

print("\nFOOTWEAR IMAGE:")
print(rec["footwear_image"])

print("\nACCESSORY IMAGE:")
print(rec["accessory_image"])