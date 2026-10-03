# Song-Recommender-System

A content-based music recommender. Enter a song and it suggests similar tracks based on audio features like energy, danceability and tempo. Built with Python, pandas, scikit-learn and Streamlit.

## How it works

- Cleaned a Spotify tracks dataset ([dataset name + link]).
- Each song is described by 9 audio features: danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo.
- Features are standardised so large-valued ones (tempo, loudness) don't dominate.
- The chosen song is compared to every other song with cosine similarity, and the closest matches are returned.
- The seed song and duplicate versions of the same song are removed from the results.

## Evaluation

Measured genre agreement@10: the fraction of a song's top 10 recommendations that share its genre label. The model never sees genre, so it works as an independent check.

Results over 300 random seed songs:

- This recommender: 15.2%
- Random baseline: 0.8%
- About 19x better than random

Genres overlap (e.g. rock vs hard-rock), so exact-label matching undercounts good recommendations. Full evaluation is in `Song_Recommendation.ipynb`.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Limitations

- Audio features only, so no personalisation from listening history.
- Doesn't capture lyrics, language or cultural context.
- Search needs an exact, case-sensitive song title.

## Future ideas

- Fuzzy search
- Genre filters
- Recommend from several songs at once
- Compare scaled vs unscaled features
