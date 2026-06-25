def parse_query(query):

    query = query.lower()

    gender = None
    occasion = None
    style = None

    # =========================
    # Gender Detection
    # =========================

    if any(word in query for word in [
        "female",
        "women",
        "woman",
        "girl",
        "ladies",
        "lady",
        "her"
    ]):
        gender = "women"

    elif any(word in query for word in [
        "male",
        "men",
        "man",
        "boy",
        "gentlemen",
        "gentleman",
        "his"
    ]):
        gender = "men"

    # =========================
    # Occasion Detection
    # =========================

    occasion_keywords = {
        "office": "office",
        "interview": "office",
        "meeting": "office",
        "party": "party",
        "wedding": "wedding",
        "vacation": "vacation",
        "beach": "vacation",
        "sports": "sports",
        "gym": "sports",
        "festive": "festive",
        "festival": "festive",
        "casual": "casual"
    }

    for word, value in occasion_keywords.items():

        if word in query:
            occasion = value
            break

    # =========================
    # Style Detection
    # =========================

    if "formal" in query:
        style = "formal"

    elif "casual" in query:
        style = "casual"

    elif "party" in query:
        style = "party"

    return {
        "gender": gender,
        "occasion": occasion,
        "style": style
    }