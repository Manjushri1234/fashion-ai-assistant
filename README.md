# AI Fashion Outfit Recommendation System

## Overview

This project is an AI-powered Fashion Outfit Recommendation System developed as part of the DareXAI AI/ML Engineer Assignment.

The system understands natural language fashion queries and recommends complete outfit combinations based on:

* Gender
* Occasion
* Style Preferences
* Outfit Compatibility
* Fashion Metadata
* Image Similarity Search

The application provides explainable recommendations along with compatibility scores and outfit details.

---

## Features

### Natural Language Query Understanding

Example Queries:

* I need a formal outfit for an interview
* Suggest a casual outfit for college
* I am attending a wedding next weekend

---

### Outfit Compatibility Engine

The system ranks outfits using:

* Gender Match
* Occasion Match
* Style Match
* Outfit Completeness
* Accessory Bonus

---

### Top 3 Recommendations

Returns the best three outfits with:

* Compatibility Score
* Outfit Components
* Fashion Explanation

---

### Explainable AI

Each recommendation includes reasoning explaining why the outfit was selected.

---

### CLIP + FAISS Similarity Search

Fashion images are converted into embeddings using CLIP.

FAISS is used to perform fast vector similarity search and retrieve visually similar fashion products.

---

## Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* CLIP
* FAISS
* Scikit-Learn

---

## Project Architecture

User Query
→ Intent Parser
→ Outfit Retrieval
→ Compatibility Ranking
→ Top-3 Recommendations
→ Outfit Generator
→ CLIP Embeddings
→ FAISS Similarity Search
→ Explainable Recommendation
→ Streamlit UI

---

## Folder Structure

fashion-ai-assistant/

* app/

  * streamlit_app.py

* src/

  * data_loader.py
  * intent_parser.py
  * retrieval.py
  * ranking.py
  * outfit_generator.py
  * embeddings.py
  * faiss_index.py
  * similarity_search.py

* data/

* vectorstore/

---

## Installation

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app/streamlit_app.py
```

---

## Future Improvements

* FashionCLIP Integration
* Personalized User Profiles
* Multi-modal Search
* LLM-based Stylist Assistant
* Real-time Fashion Trends

---

## Author

Manjushri Shetty


