import streamlit as st
from Song_Recommendation import recommend_songs

if "candidates" not in st.session_state:
    st.session_state.candidates = None

def format_song(row):
    return row["track_name"] + " — " + row["artists"]

st.title("Song Recommender")

song = st.text_input("Enter a song")

button_pressed = st.button("Recommend")

if button_pressed:
    st.session_state.candidates = None
    if song == "":
        st.error("No Song Included")
    else:
        recommendations = recommend_songs(song_name = song)

        if isinstance(recommendations, str):
            st.error(recommendations)
        else: 
            if "track_id" in recommendations.columns:
                st.session_state.candidates =  recommendations
            else:
                st.dataframe(recommendations, hide_index=True)

if st.session_state.candidates is not None:
    options = st.session_state.candidates.apply(format_song, axis=1)
    selected_song = st.radio("Choose a song:", options)
    selected_row = st.session_state.candidates[st.session_state.candidates.apply(format_song, axis=1) == selected_song]
    track_id = selected_row.iloc[0]["track_id"]
    recommendations = recommend_songs(track_id=track_id)
    st.dataframe(recommendations, hide_index=True)