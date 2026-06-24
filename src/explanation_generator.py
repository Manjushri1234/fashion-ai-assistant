def generate_explanation(recommendation):

    theme = recommendation["theme"]
    occasion = recommendation["occasion"]

    return (
        f"This outfit is carefully selected for a {occasion} occasion. "
        f"The combination of clothing, footwear, and accessories follows the "
        f"'{theme}' theme and creates a balanced, stylish appearance."
    )