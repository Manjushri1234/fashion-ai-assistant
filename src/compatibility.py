def calculate_score(
    outfit,
    user_gender=None,
    user_occasion=None,
    user_style=None
):

    score = 0

    # Occasion Match
    if (
        user_occasion
        and str(outfit["occasion"]).lower() == user_occasion.lower()
    ):
        score += 40

    # Gender Match
    if (
        user_gender
        and str(outfit["gender"]).lower() == user_gender.lower()
    ):
        score += 20

    # Style Match
    theme = str(outfit["theme"]).lower()

    if user_style:

        if user_style == "formal":

            if (
                "formal" in theme
                or "office" in theme
                or "tailored" in theme
            ):
                score += 30

        elif user_style == "casual":

            if (
                "casual" in theme
                or "day" in theme
            ):
                score += 30

        elif user_style == "party":

            if (
                "party" in theme
                or "cocktail" in theme
                or "evening" in theme
            ):
                score += 30

    # More complete outfits score higher
    score += min(
        int(outfit["items_count"]) * 5,
        25
    )

    # Accessories bonus
    accessories = 0

    if str(outfit["accessory_1"]) != "nan":
        accessories += 1

    if str(outfit["accessory_2"]) != "nan":
        accessories += 1

    score += accessories * 5

    # Prevent score from exceeding 100
    score = min(score, 100)

    return score