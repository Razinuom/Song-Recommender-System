import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv("spotify-tracks-dataset-detailed.csv")


# -----------------------------
# Clean dataset
# -----------------------------

df = df.dropna(subset=["artists", "track_name"])

df = df.drop_duplicates()

df = df.drop_duplicates(subset="track_id")

df = df.reset_index(drop=True)


# -----------------------------
# Select features
# -----------------------------

features = df[
    [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]
]


# -----------------------------
# Scale features
# -----------------------------

scaler = StandardScaler()

features_scaled = scaler.fit_transform(features)


# -----------------------------
# Recommendation function
# -----------------------------

def recommend_songs(song_name = None, track_id = None):
    if track_id is not None:
        song = df[df["track_id"] == track_id]
    else:
        song = df[df["track_name"] == song_name]
    if song.shape[0] == 0:
        return "Song Does Not Exist"
    if track_id is None and song.shape[0] > 1:
        return song[["track_name", "artists", "track_id"]]
    song = song.iloc[0]
    song_index = song.name
    song_features = features_scaled[song_index].reshape(1, -1)
    similarities = cosine_similarity(song_features, features_scaled)[0]
    similarities[song_index] = -np.inf
    recommended_indices = np.argsort(similarities)[::-1]
    recommended_scores = similarities[recommended_indices]
    recommendations = df.iloc[recommended_indices].copy()
    recommendations["Similarity"] = recommended_scores
    recommendations["Similarity"] = recommendations["Similarity"].round(3)
    recommendations = recommendations.drop_duplicates(subset=["track_name", "artists"])
    recommendations = recommendations[~((recommendations["track_name"] == song["track_name"]) & (recommendations["artists"] == song["artists"]))]
    return recommendations[["track_name", "artists", "Similarity"]][:5]