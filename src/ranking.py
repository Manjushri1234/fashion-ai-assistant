from compatibility import calculate_score


def rank_outfits(
    results_df,
    user_gender=None,
    user_occasion=None,
    user_style=None
):

    results_df = results_df.copy()

    results_df["score"] = results_df.apply(
        lambda row: calculate_score(
            row,
            user_gender,
            user_occasion,
            user_style
        ),
        axis=1
    )

    results_df = results_df.sort_values(
        by="score",
        ascending=False
    )

    return results_df