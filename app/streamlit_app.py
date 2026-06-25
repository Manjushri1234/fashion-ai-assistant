import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from data_loader import load_outfits
from intent_parser import parse_query
from retrieval import retrieve_outfits
from ranking import rank_outfits
from outfit_generator import generate_outfit

st.set_page_config(
    page_title="AI Fashion Assistant",
    layout="wide"
)

# Sidebar
st.sidebar.title("👗 Fashion AI")
st.sidebar.write("Powered by NLP + FAISS")
st.sidebar.markdown("---")
st.sidebar.write("Top-3 Outfit Recommendation System")

st.title("👗 AI Fashion Assistant")

st.write(
    "Ask for outfit recommendations naturally."
)

query = st.text_input(
    "Enter your fashion request:",
    placeholder="I need a formal outfit for office"
)

if st.button("Recommend Outfit"):

    if query:

        intent = parse_query(query)

        outfits = load_outfits()

        results = retrieve_outfits(
            outfits,
            intent["gender"],
            intent["occasion"]
        )

        ranked = rank_outfits(
            results,
            intent["gender"],
            intent["occasion"],
            intent["style"]
        )

        if len(ranked) == 0:

            st.error(
                "No matching outfit found."
            )

        else:

            top_outfits = ranked.head(3)

            st.success(
                "Top 3 Recommendations Generated!"
            )

            for i, (_, row) in enumerate(
                top_outfits.iterrows(),
                start=1
            ):

                recommendation = generate_outfit(
                    row["outfit_id"]
                )

                score = row["score"]

                st.subheader(
                    f"🏆 Outfit {i}"
                )

                st.metric(
                    "Compatibility Score",
                    f"{score}%"
                )

                st.write(
                    f"**Theme:** {recommendation['theme']}"
                )

                st.write(
                    f"**Occasion:** {recommendation['occasion']}"
                )

                st.markdown("---")

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.markdown("### Topwear")

                    if recommendation["topwear_image"]:

                        st.image(
                            recommendation["topwear_image"],
                            use_container_width=True
                        )

                    st.write(
                        recommendation["topwear"]
                    )

                with col2:

                    st.markdown("### Bottomwear")

                    if recommendation["bottomwear_image"]:

                        st.image(
                            recommendation["bottomwear_image"],
                            use_container_width=True
                        )

                    st.write(
                        recommendation["bottomwear"]
                    )

                with col3:

                    st.markdown("### Footwear")

                    if recommendation["footwear_image"]:

                        st.image(
                            recommendation["footwear_image"],
                            use_container_width=True
                        )

                    st.write(
                        recommendation["footwear"]
                    )

                with col4:

                    st.markdown("### Accessory")

                    if recommendation["accessory_image"]:

                        st.image(
                            recommendation["accessory_image"],
                            use_container_width=True
                        )

                    st.write(
                        recommendation["accessory"]
                    )

                st.markdown("---")

                st.subheader(
                    "Why This Outfit?"
                )

                st.write(
                    recommendation["reason"]
                )

                st.markdown("---")

    else:

        st.warning(
            "Please enter a query."
        )