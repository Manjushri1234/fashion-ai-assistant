from data_loader import load_outfits

outfits = load_outfits()

for _, row in outfits.iterrows():

    print("\n" + "=" * 80)

    print("OUTFIT ID:", row["outfit_id"])
    print("THEME:", row["theme"])
    print("PALETTE:", row["palette"])
    print("ITEMS:", row["items_count"])

    print("\nSTYLIST RATIONALE:")
    print(row["stylist_rationale"])

    print("=" * 80)