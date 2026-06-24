def retrieve_outfits(outfits_df, gender, occasion):

    results = outfits_df.copy()

    if gender:

        results = results[
            results["gender"] == gender
        ]

    if occasion:

        results = results[
            results["occasion"] == occasion
        ]

    return results