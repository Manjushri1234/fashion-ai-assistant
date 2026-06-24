from data_loader import load_outfits
from intent_parser import parse_query
from retrieval import retrieve_outfits
from ranking import rank_outfits
from outfit_generator import generate_outfit


def main():

    query = "I need a formal outfit for office"

    # Step 1: Parse user query
    intent = parse_query(query)

    print("\n" + "=" * 50)
    print("DETECTED INTENT")
    print("=" * 50)
    print(intent)

    # Step 2: Load outfits
    outfits = load_outfits()

    # Step 3: Retrieve matching outfits
    results = retrieve_outfits(
        outfits,
        intent["gender"],
        intent["occasion"]
    )

    print("\n" + "=" * 50)
    print("RETRIEVED OUTFITS")
    print("=" * 50)

    print(
        results[
            [
                "outfit_id",
                "theme",
                "occasion"
            ]
        ]
    )

    # Step 4: Rank outfits
    ranked = rank_outfits(
        results,
        intent["gender"],
        intent["occasion"],
        intent["style"]
    )

    print("\n" + "=" * 50)
    print("RANKED RECOMMENDATIONS")
    print("=" * 50)

    print(
        ranked[
            [
                "outfit_id",
                "theme",
                "occasion",
                "score"
            ]
        ]
    )

    # Step 5: Get best outfit
    best = ranked.iloc[0]

    # Step 6: Generate complete outfit recommendation
    recommendation = generate_outfit(
        best["outfit_id"]
    )

    print("\n" + "=" * 50)
    print("FINAL RECOMMENDATION")
    print("=" * 50)

    print(f"Theme      : {recommendation['theme']}")
    print(f"Occasion   : {recommendation['occasion']}")
    print(f"Topwear    : {recommendation['topwear']}")
    print(f"Bottomwear : {recommendation['bottomwear']}")
    print(f"Footwear   : {recommendation['footwear']}")
    print(f"Accessory  : {recommendation['accessory']}")

    print("\nReason:")
    print(recommendation["reason"])


if __name__ == "__main__":
    main()