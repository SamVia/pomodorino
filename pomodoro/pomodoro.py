import streamlit as st
from pygame import mixer

mixer.init()

music = st.file_uploader("choose a song")

try:
    mixer.music.load(music)
except Exception:
    st.write("choose a song")
if st.button("play"):
    mixer.music.play()
elif st.button("stop"):
    mixer.music.stop()
elif st.button("Resume"):
    mixer.music.unpause()
elif st.button("pause"):
    mixer.music.pause()